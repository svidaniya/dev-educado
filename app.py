from __future__ import annotations

import json
import os
import re
from datetime import datetime
from functools import wraps
from pathlib import Path

import markdown
from flask import Flask, flash, g, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

DIRETORIO_BASE = Path(__file__).resolve().parent
DIRETORIO_CONTEUDO = DIRETORIO_BASE / "content"

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "deveducado-chave-local")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class Inscricao(db.Model):
    __tablename__ = "inscricao"
    __table_args__ = (
        db.UniqueConstraint("usuario_id", "identificador_curso", name="uq_inscricao_usuario_curso"),
    )

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    identificador_curso = db.Column(db.String(120), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class ProgressoAula(db.Model):
    __tablename__ = "progresso_aula"
    __table_args__ = (
        db.UniqueConstraint(
            "usuario_id", "identificador_curso", "identificador_aula", name="uq_progresso_aula_usuario_curso_aula"
        ),
    )

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    identificador_curso = db.Column(db.String(120), nullable=False)
    identificador_aula = db.Column(db.String(120), nullable=False)
    data_conclusao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class TentativaQuiz(db.Model):
    __tablename__ = "tentativa_quiz"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    identificador_curso = db.Column(db.String(120), nullable=False)
    identificador_quiz = db.Column(db.String(120), nullable=False)
    pontuacao = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class Comentario(db.Model):
    __tablename__ = "comentario"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    identificador_curso = db.Column(db.String(120), nullable=False)
    identificador_aula = db.Column(db.String(120), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


with app.app_context():
    db.create_all()

@app.before_request
def carregar_usuario_logado() -> None:
    usuario_id = session.get("usuario_id")
    g.usuario = Usuario.query.get(usuario_id) if usuario_id else None


@app.context_processor
def disponibilizar_usuario_atual():
    return {"usuario_atual": g.usuario}


def requer_login(funcao_visualizacao):
    @wraps(funcao_visualizacao)
    def visualizacao_protegida(*args, **kwargs):
        if g.usuario is None:
            flash("Faca login para acessar essa pagina.", "warning")
            return redirect(url_for("entrar"))
        return funcao_visualizacao(*args, **kwargs)

    return visualizacao_protegida


def ler_json(caminho: Path) -> dict:
    if not caminho.exists():
        return {}
    return json.loads(caminho.read_text(encoding="utf-8"))


def obter_identificadores_cursos() -> list[str]:
    if not DIRETORIO_CONTEUDO.exists():
        return []
    identificadores = []
    for pasta_curso in DIRETORIO_CONTEUDO.iterdir():
        if pasta_curso.is_dir() and (pasta_curso / "course.json").exists():
            identificadores.append(pasta_curso.name)
    return sorted(identificadores)


def extrair_titulo_markdown(conteudo: str, titulo_padrao: str) -> str:
    correspondencia = re.search(r"^#\s+(.+)$", conteudo, flags=re.MULTILINE)
    return correspondencia.group(1).strip() if correspondencia else titulo_padrao


def obter_ordem_nome_arquivo(nome_arquivo: str) -> int:
    correspondencia = re.match(r"(\d+)", nome_arquivo)
    return int(correspondencia.group(1)) if correspondencia else 999


def listar_aulas(identificador_curso: str) -> list[dict]:
    diretorio_aulas = DIRETORIO_CONTEUDO / identificador_curso / "lessons"
    aulas = []
    if not diretorio_aulas.exists():
        return aulas

    for arquivo_aula in diretorio_aulas.glob("*.md"):
        conteudo = arquivo_aula.read_text(encoding="utf-8")
        identificador_aula = arquivo_aula.stem
        aulas.append(
            {
                "identificador": identificador_aula,
                "nome_arquivo": arquivo_aula.name,
                "titulo": extrair_titulo_markdown(
                    conteudo, identificador_aula.replace("-", " ").title()
                ),
                "ordem": obter_ordem_nome_arquivo(arquivo_aula.name),
            }
        )
    aulas.sort(key=lambda aula: (aula["ordem"], aula["nome_arquivo"]))
    return aulas


def listar_quizzes(identificador_curso: str) -> list[dict]:
    diretorio_quizzes = DIRETORIO_CONTEUDO / identificador_curso / "quizzes"
    quizzes = []
    if not diretorio_quizzes.exists():
        return quizzes

    for arquivo_quiz in diretorio_quizzes.glob("*.json"):
        dados_quiz = ler_json(arquivo_quiz)
        identificador_quiz = arquivo_quiz.stem
        quizzes.append(
            {
                "identificador": identificador_quiz,
                "nome_arquivo": arquivo_quiz.name,
                "titulo": dados_quiz.get("title", identificador_quiz.replace("-", " ").title()),
                "ordem": obter_ordem_nome_arquivo(arquivo_quiz.name),
            }
        )
    quizzes.sort(key=lambda quiz: (quiz["ordem"], quiz["nome_arquivo"]))
    return quizzes


def listar_atividades(identificador_curso: str) -> list[dict]:
    atividades = []

    for aula in listar_aulas(identificador_curso):
        atividades.append({**aula, "tipo": "aula", "prioridade": 0})

    for quiz in listar_quizzes(identificador_curso):
        atividades.append({**quiz, "tipo": "quiz", "prioridade": 1})

    atividades.sort(
        key=lambda atividade: (
            atividade["ordem"],
            atividade["prioridade"],
            atividade["nome_arquivo"],
        )
    )
    return atividades


def obter_proxima_atividade(
    identificador_curso: str,
    tipo_atual: str,
    identificador_atual: str,
) -> dict | None:
    atividades = listar_atividades(identificador_curso)

    for indice, atividade in enumerate(atividades):
        if (
            atividade["tipo"] == tipo_atual
            and atividade["identificador"] == identificador_atual
        ):
            return atividades[indice + 1] if indice + 1 < len(atividades) else None

    return None


def obter_curso(identificador_curso: str) -> dict | None:
    caminho_curso = DIRETORIO_CONTEUDO / identificador_curso / "course.json"
    if not caminho_curso.exists():
        return None

    dados_curso = ler_json(caminho_curso)
    return {
        "identificador": dados_curso.get("slug", identificador_curso),
        "titulo": dados_curso.get("title", identificador_curso.title()),
        "descricao": dados_curso.get("description", ""),
        "linguagem": dados_curso.get("language", identificador_curso.title()),
        "nivel": dados_curso.get("level", "Iniciante"),
        "imagem": dados_curso.get("imagem", ""),
        "descricao_imagem": dados_curso.get("descricao_imagem", ""),
        "quantidade_aulas": len(listar_aulas(identificador_curso)),
        "quantidade_alunos": Inscricao.query.filter_by(identificador_curso=identificador_curso).count(),
    }


def obter_todos_cursos() -> list[dict]:
    cursos = []
    for identificador_curso in obter_identificadores_cursos():
        curso = obter_curso(identificador_curso)
        if curso:
            cursos.append(curso)
    return cursos


def extrair_materiais_markdown(conteudo_markdown: str) -> list[dict]:
    secao_materiais = re.search(
        r"^##\s+Materiais complementares\s*$([\s\S]*)",
        conteudo_markdown,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if not secao_materiais:
        return []
    conteudo_secao = secao_materiais.group(1)
    proximo_titulo = re.search(r"^##\s+", conteudo_secao, flags=re.MULTILINE)
    if proximo_titulo:
        conteudo_secao = conteudo_secao[: proximo_titulo.start()]
    materiais = []
    for link_material in re.finditer(r"-\s*\[(.+?)\]\((https?://[^)]+)\)", conteudo_secao):
        materiais.append({"rotulo": link_material.group(1).strip(), "url": link_material.group(2).strip()})
    return materiais


def obter_aula(identificador_curso: str, identificador_aula: str) -> dict | None:
    caminho_aula = DIRETORIO_CONTEUDO / identificador_curso / "lessons" / f"{identificador_aula}.md"
    if not caminho_aula.exists():
        return None
    conteudo_markdown = caminho_aula.read_text(encoding="utf-8")
    conteudo_sem_titulo = re.sub(
        r"^#\s+.+$(?:\r?\n)?", "", conteudo_markdown, count=1, flags=re.MULTILINE
    )
    return {
        "identificador": identificador_aula,
        "titulo": extrair_titulo_markdown(conteudo_markdown, identificador_aula.replace("-", " ").title()),
        "conteudo": markdown.markdown(conteudo_sem_titulo, extensions=["fenced_code", "tables"]),
        "materiais": extrair_materiais_markdown(conteudo_markdown),
    }


def obter_quiz(identificador_curso: str, identificador_quiz: str) -> dict | None:
    caminho_quiz = DIRETORIO_CONTEUDO / identificador_curso / "quizzes" / f"{identificador_quiz}.json"
    if not caminho_quiz.exists():
        return None
    dados_quiz = ler_json(caminho_quiz)
    questoes = []
    for dados_questao in dados_quiz.get("questions", []):
        questoes.append(
            {
                "enunciado": dados_questao.get("question", ""),
                "opcoes": dados_questao.get("options", []),
                "resposta": dados_questao.get("answer", -1),
            }
        )
    return {
        "identificador": identificador_quiz,
        "titulo": dados_quiz.get("title", identificador_quiz.replace("-", " ").title()),
        "questoes": questoes,
    }


def esta_inscrito(usuario_id: int, identificador_curso: str) -> bool:
    inscricao = Inscricao.query.filter_by(usuario_id=usuario_id, identificador_curso=identificador_curso).first()
    return inscricao is not None


def montar_progresso(usuario_id: int, identificador_curso: str, total_aulas: int) -> dict:
    quantidade_concluida = (
        ProgressoAula.query.filter_by(
            usuario_id=usuario_id,
            identificador_curso=identificador_curso,
        )
        .with_entities(ProgressoAula.identificador_aula)
        .distinct()
        .count()
    )
    porcentagem = int((quantidade_concluida / total_aulas) * 100) if total_aulas else 0
    return {"quantidade_concluida": quantidade_concluida, "total": total_aulas, "porcentagem": porcentagem}


@app.route("/")
def pagina_inicial():
    return render_template("index.html", cursos=obter_todos_cursos())


@app.route("/register", methods=["GET", "POST"])
def cadastrar():
    if g.usuario:
        return redirect(url_for("painel"))
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        if not nome or not email or not senha:
            flash("Preencha nome, email e senha.", "error")
            return render_template("register.html")
        if Usuario.query.filter_by(email=email).first():
            flash("Esse email ja esta cadastrado.", "error")
            return render_template("register.html")
        db.session.add(Usuario(nome=nome, email=email, senha_hash=generate_password_hash(senha)))
        db.session.commit()
        flash("Cadastro realizado com sucesso. Faca login.", "success")
        return redirect(url_for("entrar"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def entrar():
    if g.usuario:
        return redirect(url_for("painel"))
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario is None or not check_password_hash(usuario.senha_hash, senha):
            flash("Email ou senha invalidos.", "error")
            return render_template("login.html")
        session.clear()
        session["usuario_id"] = usuario.id
        flash("Login realizado com sucesso.", "success")
        return redirect(url_for("painel"))
    return render_template("login.html")


@app.route("/logout")
@requer_login
def sair():
    session.clear()
    flash("Voce saiu da conta.", "success")
    return redirect(url_for("pagina_inicial"))


@app.route("/dashboard")
@requer_login
def painel():
    inscricoes = Inscricao.query.filter_by(usuario_id=g.usuario.id).all()
    cursos_inscritos = []
    for inscricao in inscricoes:
        curso = obter_curso(inscricao.identificador_curso)
        if curso:
            progresso = montar_progresso(g.usuario.id, curso["identificador"], curso["quantidade_aulas"])
            cursos_inscritos.append({"curso": curso, "progresso": progresso})
    tentativas_recentes = (
        TentativaQuiz.query.filter_by(usuario_id=g.usuario.id)
        .order_by(TentativaQuiz.data_criacao.desc())
        .limit(5)
        .all()
    )
    return render_template("dashboard.html", cursos_inscritos=cursos_inscritos, tentativas_recentes=tentativas_recentes)


@app.route("/courses")
def listar_cursos():
    return render_template("courses.html", cursos=obter_todos_cursos())


@app.route("/course/<identificador_curso>")
def detalhe_curso(identificador_curso: str):
    curso = obter_curso(identificador_curso)
    if not curso:
        flash("Curso nao encontrado.", "error")
        return redirect(url_for("listar_cursos"))
    aulas = listar_aulas(identificador_curso)
    inscrito = g.usuario is not None and esta_inscrito(g.usuario.id, identificador_curso)
    progresso = {
        "quantidade_concluida": 0,
        "total": len(aulas),
        "porcentagem": 0,
    }
    if inscrito:
        progresso = montar_progresso(g.usuario.id, identificador_curso, len(aulas))
    aulas_concluidas = set()
    if inscrito:
        registros_progresso = ProgressoAula.query.filter_by(
            usuario_id=g.usuario.id,
            identificador_curso=identificador_curso,
        ).all()
        aulas_concluidas = {registro.identificador_aula for registro in registros_progresso}
    return render_template(
        "course.html",
        curso=curso,
        aulas=aulas,
        atividades=listar_atividades(identificador_curso),
        inscrito=inscrito,
        progresso=progresso,
        aulas_concluidas=aulas_concluidas,
    )


@app.route("/course/<identificador_curso>/enroll", methods=["POST"])
@requer_login
def inscrever_curso(identificador_curso: str):
    if not obter_curso(identificador_curso):
        flash("Curso nao encontrado.", "error")
        return redirect(url_for("listar_cursos"))
    if not esta_inscrito(g.usuario.id, identificador_curso):
        db.session.add(Inscricao(usuario_id=g.usuario.id, identificador_curso=identificador_curso))
        db.session.commit()
        flash("Inscricao realizada com sucesso.", "success")
    else:
        flash("Voce ja esta inscrito nesse curso.", "warning")
    return redirect(url_for("detalhe_curso", identificador_curso=identificador_curso))


@app.route("/course/<identificador_curso>/lesson/<identificador_aula>")
@requer_login
def detalhe_aula(identificador_curso: str, identificador_aula: str):
    if not obter_curso(identificador_curso):
        flash("Curso nao encontrado.", "error")
        return redirect(url_for("listar_cursos"))
    if not esta_inscrito(g.usuario.id, identificador_curso):
        flash("Voce precisa se inscrever para acessar as aulas.", "warning")
        return redirect(url_for("detalhe_curso", identificador_curso=identificador_curso))
    aula = obter_aula(identificador_curso, identificador_aula)
    if not aula:
        flash("Aula nao encontrada.", "error")
        return redirect(url_for("detalhe_curso", identificador_curso=identificador_curso))
    aula_concluida = (
        ProgressoAula.query.filter_by(
            usuario_id=g.usuario.id,
            identificador_curso=identificador_curso,
            identificador_aula=identificador_aula,
        ).first()
        is not None
    )
    comentarios = (
        db.session.query(Comentario, Usuario)
        .join(Usuario, Usuario.id == Comentario.usuario_id)
        .filter(
            Comentario.identificador_curso == identificador_curso,
            Comentario.identificador_aula == identificador_aula,
        )
        .order_by(Comentario.data_criacao.desc())
        .all()
    )
    return render_template(
        "lesson.html",
        aula=aula,
        identificador_curso=identificador_curso,
        aula_concluida=aula_concluida,
        comentarios=comentarios,
        proxima_atividade=obter_proxima_atividade(
            identificador_curso,
            "aula",
            identificador_aula,
        ),
    )


@app.route("/course/<identificador_curso>/lesson/<identificador_aula>/complete", methods=["POST"])
@requer_login
def concluir_aula(identificador_curso: str, identificador_aula: str):
    if not esta_inscrito(g.usuario.id, identificador_curso):
        flash("Voce precisa se inscrever no curso.", "warning")
        return redirect(url_for("detalhe_curso", identificador_curso=identificador_curso))
    if not obter_aula(identificador_curso, identificador_aula):
        flash("Aula nao encontrada.", "error")
        return redirect(url_for("detalhe_curso", identificador_curso=identificador_curso))
    progresso_existente = ProgressoAula.query.filter_by(
        usuario_id=g.usuario.id,
        identificador_curso=identificador_curso,
        identificador_aula=identificador_aula,
    ).first()
    if progresso_existente is None:
        db.session.add(
            ProgressoAula(
                usuario_id=g.usuario.id,
                identificador_curso=identificador_curso,
                identificador_aula=identificador_aula,
            )
        )
        db.session.commit()
        flash("Aula marcada como concluida.", "success")
    else:
        flash("Essa aula ja esta concluida.", "warning")
    return redirect(
        url_for(
            "detalhe_aula",
            identificador_curso=identificador_curso,
            identificador_aula=identificador_aula,
        )
    )


@app.route("/course/<identificador_curso>/lesson/<identificador_aula>/comment", methods=["POST"])
@requer_login
def adicionar_comentario(identificador_curso: str, identificador_aula: str):
    if not esta_inscrito(g.usuario.id, identificador_curso):
        flash("Voce precisa se inscrever no curso.", "warning")
        return redirect(url_for("detalhe_curso", identificador_curso=identificador_curso))
    conteudo = request.form.get("conteudo", "").strip()
    if not conteudo:
        flash("O comentario nao pode estar vazio.", "error")
        return redirect(
            url_for(
                "detalhe_aula",
                identificador_curso=identificador_curso,
                identificador_aula=identificador_aula,
            )
        )
    db.session.add(
        Comentario(
            usuario_id=g.usuario.id,
            identificador_curso=identificador_curso,
            identificador_aula=identificador_aula,
            conteudo=conteudo,
        )
    )
    db.session.commit()
    flash("Comentario adicionado.", "success")
    return redirect(
        url_for(
            "detalhe_aula",
            identificador_curso=identificador_curso,
            identificador_aula=identificador_aula,
        )
    )


@app.route("/comment/<int:comentario_id>/delete", methods=["POST"])
@requer_login
def excluir_comentario(comentario_id: int):
    comentario = Comentario.query.get_or_404(comentario_id)
    if comentario.usuario_id != g.usuario.id:
        flash("Voce so pode apagar seus proprios comentarios.", "error")
        return redirect(url_for("detalhe_aula", identificador_curso=comentario.identificador_curso, identificador_aula=comentario.identificador_aula))
    identificador_curso = comentario.identificador_curso
    identificador_aula = comentario.identificador_aula
    db.session.delete(comentario)
    db.session.commit()
    flash("Comentario removido.", "success")
    return redirect(url_for("detalhe_aula", identificador_curso=identificador_curso, identificador_aula=identificador_aula))


@app.route("/course/<identificador_curso>/quiz/<identificador_quiz>", methods=["GET", "POST"])
@requer_login
def pagina_quiz(identificador_curso: str, identificador_quiz: str):
    if not obter_curso(identificador_curso):
        flash("Curso nao encontrado.", "error")
        return redirect(url_for("listar_cursos"))
    if not esta_inscrito(g.usuario.id, identificador_curso):
        flash("Voce precisa se inscrever para responder quizzes.", "warning")
        return redirect(url_for("detalhe_curso", identificador_curso=identificador_curso))
    quiz = obter_quiz(identificador_curso, identificador_quiz)
    if not quiz:
        flash("Quiz nao encontrado.", "error")
        return redirect(url_for("detalhe_curso", identificador_curso=identificador_curso))
    if request.method == "POST":
        quantidade_acertos = 0
        for indice_questao, questao in enumerate(quiz["questoes"]):
            resposta_escolhida = request.form.get(f"questao{indice_questao}")
            if resposta_escolhida is not None and int(resposta_escolhida) == int(questao["resposta"]):
                quantidade_acertos += 1
        tentativa = TentativaQuiz(usuario_id=g.usuario.id, identificador_curso=identificador_curso, identificador_quiz=identificador_quiz, pontuacao=quantidade_acertos, total=len(quiz["questoes"]))
        db.session.add(tentativa)
        db.session.commit()
        session["ultima_tentativa_id"] = tentativa.id
        return redirect(url_for("resultado_quiz", identificador_curso=identificador_curso, identificador_quiz=identificador_quiz))
    return render_template("quiz.html", quiz=quiz, identificador_curso=identificador_curso)


@app.route("/course/<identificador_curso>/quiz/<identificador_quiz>/result")
@requer_login
def resultado_quiz(identificador_curso: str, identificador_quiz: str):
    tentativa_id = session.get("ultima_tentativa_id")
    tentativa = None
    if tentativa_id:
        tentativa = TentativaQuiz.query.filter_by(id=tentativa_id, usuario_id=g.usuario.id, identificador_curso=identificador_curso, identificador_quiz=identificador_quiz).first()
    if tentativa is None:
        tentativa = TentativaQuiz.query.filter_by(usuario_id=g.usuario.id, identificador_curso=identificador_curso, identificador_quiz=identificador_quiz).order_by(TentativaQuiz.data_criacao.desc()).first()
    if tentativa is None:
        flash("Nenhum resultado encontrado para esse quiz.", "warning")
        return redirect(url_for("pagina_quiz", identificador_curso=identificador_curso, identificador_quiz=identificador_quiz))
    porcentagem = int((tentativa.pontuacao / tentativa.total) * 100) if tentativa.total else 0
    return render_template(
        "quiz_result.html",
        tentativa=tentativa,
        porcentagem=porcentagem,
        identificador_curso=identificador_curso,
        proxima_atividade=obter_proxima_atividade(
            identificador_curso,
            "quiz",
            identificador_quiz,
        ),
    )


@app.route("/ranking")
def ranking():
    identificador_curso_selecionado = request.args.get("curso", "").strip()
    todos_cursos = obter_todos_cursos()
    consulta_tentativas = TentativaQuiz.query
    if identificador_curso_selecionado:
        consulta_tentativas = consulta_tentativas.filter_by(identificador_curso=identificador_curso_selecionado)
    melhor_pontuacao_por_quiz = {}
    for tentativa in consulta_tentativas.all():
        pontuacao = int((tentativa.pontuacao / tentativa.total) * 100) if tentativa.total else 0
        chave_quiz = (tentativa.usuario_id, tentativa.identificador_curso, tentativa.identificador_quiz)
        melhor_pontuacao_por_quiz[chave_quiz] = max(melhor_pontuacao_por_quiz.get(chave_quiz, 0), pontuacao)
    pontos_por_usuario = {}
    for (usuario_id, _, _), pontuacao in melhor_pontuacao_por_quiz.items():
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            pontos_por_usuario.setdefault(usuario.id, {"nome": usuario.nome, "pontos": 0})
            pontos_por_usuario[usuario.id]["pontos"] += pontuacao
    linhas_ranking = sorted(pontos_por_usuario.values(), key=lambda linha_ranking: linha_ranking["pontos"], reverse=True)
    return render_template("ranking.html", linhas_ranking=linhas_ranking, identificador_curso_selecionado=identificador_curso_selecionado, todos_cursos=todos_cursos)


@app.route("/profile")
@requer_login
def perfil():
    quantidade_inscricoes = Inscricao.query.filter_by(usuario_id=g.usuario.id).count()
    quantidade_comentarios = Comentario.query.filter_by(usuario_id=g.usuario.id).count()
    quantidade_tentativas = TentativaQuiz.query.filter_by(usuario_id=g.usuario.id).count()
    return render_template("profile.html", quantidade_inscricoes=quantidade_inscricoes, quantidade_comentarios=quantidade_comentarios, quantidade_tentativas=quantidade_tentativas)


if __name__ == "__main__":
    app.run(debug=True)
