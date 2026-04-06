from pathlib import Path
from string import Template

# Dados iniciais baseados no perfil informado pelo usuario.
# Se quiser, altere os campos abaixo e execute novamente para recriar o index.html.
resume_data = {
    "name": "Vander Lucio Evaristo",
    "headline": "Quality Assurance | QA focado em automacao de testes",
    "location": "Belo Horizonte/MG, Brasil",
    "email": "vanderlucioevaristo@gmail.com",
    "phone": "+55 31 99928-5680",
    "linkedin": "https://www.linkedin.com/in/vanderevaristo",
    "summary": (
        "Comecei minha carreira em tecnologia atuando como suporte tecnico aos "
        "usuarios de sistemas de backoffice. Apos concluir a pos-graduacao em "
        "engenharia de software, migrei para a area de testes e atuei em contexto "
        "agil como analista de testes e analista de negocios. Atualmente, atuo "
        "como QA com foco em automacao."
    ),
    "skills": [
        "Python",
        "Testes automatizados com Playwright",
        "Testes automatizados com Selenium",
        "Cypress",
        "Rest Assured",
        "Postman",
        "Oracle SQL",
        "Continuous Testing",
        "Cobertura de Codigo",
    ],
    "experience": [
        {
            "role": "Analista de Automacao de Testes Senior",
            "company": "Base2 Tecnologia",
            "period": "junho/2024 - Atual",
            "description": (
                "Automacoes de testes back-end com Rest Assured, automacoes "
                "front-end e execucao de testes manuais."
            ),
        },
        {
            "role": "Analista de Testes de Software / QA",
            "company": "TOTVS S/A",
            "period": "agosto/2003 - marco/2024",
            "description": (
                "Planejamento e execucao de testes funcionais, exploratorios, "
                "regressao e automatizados; rastreio de bugs; testes web com "
                "Selenium e Cypress; testes de API REST com Postman e uso de "
                "Oracle SQL para validacoes."
            ),
        },
        {
            "role": "Analista de Negocios III",
            "company": "TOTVS S/A",
            "period": "agosto/2003 - marco/2024",
            "description": (
                "Analise e documentacao de melhorias no sistema interno de "
                "automacao de testes, suporte e treinamento de usuarios, "
                "atuacao em desenvolvimento e responsabilidade por Continuous "
                "Testing e Cobertura de Codigo do produto RM."
            ),
        },
        {
            "role": "Tecnico Contabil",
            "company": "LOCALIZA RENT A CAR S/A",
            "period": "dezembro/1997 - fevereiro/2002",
            "description": (
                "Conciliacao de contas, classificacao contabil, controle de "
                "imobilizado, processamento de folha e contabilizacao de impostos."
            ),
        },
        {
            "role": "Auxiliar Administrativo",
            "company": "VITAL VARGAS TRANSPORTES LTDA",
            "period": "maio/1994 - agosto/1997",
            "description": (
                "Atuacao administrativa com classificacao contabil, conciliacao "
                "de contas, controle de imobilizado e encerramento contabil mensal."
            ),
        },
    ],
    "education": [
        {
            "course": "Pos-Graduacao em Engenharia de Software",
            "institution": "Pontificia Universidade Catolica de Minas Gerais (PUC Minas)",
            "period": "2009 - 2010",
        },
        {
            "course": "Administracao de Empresas e Gestao Hoteleira",
            "institution": "Universidade FUMEC",
            "period": "2000 - 2003",
        },
    ],
}


def build_experience_items(experience):
    return "\n".join(
        f"""
        <article class=\"item\">
            <h3>{item['role']} - {item['company']}</h3>
            <p class=\"period\">{item['period']}</p>
            <p>{item['description']}</p>
        </article>
        """.strip()
        for item in experience
    )


def build_education_items(education):
    return "\n".join(
        f"""
        <article class=\"item\">
            <h3>{item['course']}</h3>
            <p>{item['institution']}</p>
            <p class=\"period\">{item['period']}</p>
        </article>
        """.strip()
        for item in education
    )


def build_skills_items(skills):
    return "\n".join(f"<li>{skill}</li>" for skill in skills)


def generate_index_html(data):
    template = Template(
        """<!DOCTYPE html>
<html lang=\"pt-BR\">
<head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>Curriculum - $name</title>
    <style>
        :root {
            --bg1: #f6f4ef;
            --bg2: #e8f0e3;
            --paper: #fffdf8;
            --ink: #1f2937;
            --muted: #4b5563;
            --accent: #0a66c2;
            --line: #d8d9cf;
        }
        * {
            box-sizing: border-box;
        }
        body {
            margin: 0;
            font-family: Georgia, 'Times New Roman', serif;
            color: var(--ink);
            background: radial-gradient(circle at top left, var(--bg2), var(--bg1));
            min-height: 100vh;
            padding: 32px 16px;
        }
        .resume {
            max-width: 980px;
            margin: 0 auto;
            background: var(--paper);
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 32px;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
            animation: appear 600ms ease-out;
        }
        @keyframes appear {
            from {
                opacity: 0;
                transform: translateY(12px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        header h1 {
            margin: 0;
            font-size: clamp(1.8rem, 3vw, 2.6rem);
            letter-spacing: 0.4px;
        }
        .headline {
            margin: 6px 0 0;
            color: var(--muted);
            font-size: 1.1rem;
        }
        .contact {
            margin-top: 14px;
            display: flex;
            flex-wrap: wrap;
            gap: 10px 18px;
            font-size: 0.95rem;
        }
        .contact a {
            color: var(--accent);
            text-decoration: none;
            border-bottom: 1px dashed transparent;
            transition: border-color 180ms ease;
        }
        .contact a:hover {
            border-color: var(--accent);
        }
        main {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 24px;
            margin-top: 28px;
        }
        section {
            border-top: 1px solid var(--line);
            padding-top: 14px;
            margin-top: 14px;
        }
        section h2 {
            margin: 0 0 12px;
            font-size: 1.05rem;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: #111827;
        }
        .item h3 {
            margin: 0;
            font-size: 1rem;
        }
        .item p {
            margin: 6px 0;
            color: var(--muted);
            line-height: 1.5;
        }
        .period {
            font-style: italic;
            color: #6b7280;
        }
        .skills {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        .skills li {
            border: 1px solid var(--line);
            border-radius: 999px;
            padding: 6px 12px;
            background: #fff;
            font-size: 0.9rem;
        }
        footer {
            margin-top: 24px;
            font-size: 0.85rem;
            color: #6b7280;
            text-align: right;
        }
        @media (max-width: 760px) {
            .resume {
                padding: 20px;
            }
            main {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class=\"resume\">
        <header>
            <h1>$name</h1>
            <p class=\"headline\">$headline</p>
            <div class=\"contact\">
                <span>$location</span>
                <span>$phone</span>
                <span>$email</span>
                <a href=\"$linkedin\" target=\"_blank\" rel=\"noopener noreferrer\">LinkedIn</a>
            </div>
        </header>

        <main>
            <div>
                <section>
                    <h2>Resumo</h2>
                    <p>$summary</p>
                </section>

                <section>
                    <h2>Experiencia</h2>
                    $experience_items
                </section>

                <section>
                    <h2>Formacao</h2>
                    $education_items
                </section>
            </div>

            <aside>
                <section>
                    <h2>Competencias</h2>
                    <ul class=\"skills\">
                        $skills_items
                    </ul>
                </section>
            </aside>
        </main>

        <footer>
            Curriculo gerado por Python a partir de base do LinkedIn.
        </footer>
    </div>
</body>
</html>
"""
    )

    return template.substitute(
        name=data["name"],
        headline=data["headline"],
        location=data["location"],
        phone=data["phone"],
        email=data["email"],
        linkedin=data["linkedin"],
        summary=data["summary"],
        experience_items=build_experience_items(data["experience"]),
        education_items=build_education_items(data["education"]),
        skills_items=build_skills_items(data["skills"]),
    )


def main():
    html = generate_index_html(resume_data)
    output = Path(__file__).with_name("index.html")
    output.write_text(html, encoding="utf-8")
    print(f"Arquivo gerado com sucesso: {output}")


if __name__ == "__main__":
    main()
