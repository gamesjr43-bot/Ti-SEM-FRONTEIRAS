# -*- coding: utf-8 -*-
"""
Base de dados de DEMONSTRAÇÃO para o projeto TI Sem Fronteiras.

⚠️ Valores de salário, custo de vida e demanda são ESTIMATIVAS aproximadas,
   e as empresas/vagas são FICTÍCIAS — servem apenas para demonstrar o app.

Estes dados têm dois usos:
  1. Fallback offline do app (quando o Firebase não está conectado).
  2. Fonte para o script `seed_firestore.py`, que envia tudo ao Firestore.

Em uma versão futura, serão substituídos por APIs reais (Numbeo, World Bank,
RemoteOK, WeWorkRemotely etc.) ou por raspagem de dados agendada.
"""

# ---------------------------------------------------------------------------
# MÓDULO I - MundoDev (Inteligência Geográfica)
# ---------------------------------------------------------------------------
PAISES = [
    {
        "pais": "Portugal", "regiao": "Europa", "demanda_ti": "Alta",
        "custo_vida_mensal_usd": 1100, "salario_medio_ti_usd": 2800,
        "idioma": "Português",
        "visto": "D3 (Trabalho Altamente Qualificado) / Blue Card UE",
        "dificuldade_visto": "Baixa",
        "resumo": "Idioma nativo facilita a adaptação. Forte polo de startups em Lisboa e Porto, "
                  "com custo de vida menor que a média da Europa Ocidental.",
    },
    {
        "pais": "Alemanha", "regiao": "Europa", "demanda_ti": "Muito Alta",
        "custo_vida_mensal_usd": 1500, "salario_medio_ti_usd": 4800,
        "idioma": "Alemão / Inglês (setor de tech)",
        "visto": "Blue Card UE / Chancenkarte (Cartão de Oportunidade)",
        "dificuldade_visto": "Média",
        "resumo": "Maior mercado de TI da Europa. Muitas empresas aceitam inglês como língua de trabalho, "
                  "mas o alemão ajuda muito no dia a dia.",
    },
    {
        "pais": "Canadá", "regiao": "América do Norte", "demanda_ti": "Muito Alta",
        "custo_vida_mensal_usd": 1800, "salario_medio_ti_usd": 5200,
        "idioma": "Inglês / Francês",
        "visto": "Express Entry (Federal Skilled Worker)",
        "dificuldade_visto": "Média",
        "resumo": "Programa de imigração por pontos bem estruturado, favorável a profissionais de TI. "
                  "Toronto, Vancouver e Montreal concentram as vagas.",
    },
    {
        "pais": "Irlanda", "regiao": "Europa", "demanda_ti": "Alta",
        "custo_vida_mensal_usd": 1900, "salario_medio_ti_usd": 5000,
        "idioma": "Inglês",
        "visto": "Critical Skills Employment Permit",
        "dificuldade_visto": "Baixa",
        "resumo": "Sede europeia de muitas big techs (Google, Meta, Stripe). Custo de moradia alto em Dublin.",
    },
    {
        "pais": "Espanha", "regiao": "Europa", "demanda_ti": "Média",
        "custo_vida_mensal_usd": 1200, "salario_medio_ti_usd": 2600,
        "idioma": "Espanhol",
        "visto": "Visto de Nômade Digital / Trabalho Altamente Qualificado",
        "dificuldade_visto": "Baixa",
        "resumo": "Boa qualidade de vida e proximidade cultural com o Brasil; salários abaixo da média da UE.",
    },
    {
        "pais": "Emirados Árabes Unidos", "regiao": "Oriente Médio", "demanda_ti": "Alta",
        "custo_vida_mensal_usd": 2200, "salario_medio_ti_usd": 5500,
        "idioma": "Inglês",
        "visto": "Golden Visa / Visto de Trabalho patrocinado por empresa",
        "dificuldade_visto": "Baixa",
        "resumo": "Sem imposto de renda pessoal. Alta demanda por especialistas em cloud e segurança.",
    },
    {
        "pais": "Países Baixos", "regiao": "Europa", "demanda_ti": "Muito Alta",
        "custo_vida_mensal_usd": 1900, "salario_medio_ti_usd": 5000,
        "idioma": "Inglês / Holandês",
        "visto": "Highly Skilled Migrant (Kennismigrant)",
        "dificuldade_visto": "Baixa",
        "resumo": "Inglês amplamente usado no trabalho. Amsterdã é hub de fintechs e logística; "
                  "moradia é o maior desafio.",
    },
    {
        "pais": "Reino Unido", "regiao": "Europa", "demanda_ti": "Alta",
        "custo_vida_mensal_usd": 2100, "salario_medio_ti_usd": 5300,
        "idioma": "Inglês",
        "visto": "Skilled Worker Visa (com patrocínio da empresa)",
        "dificuldade_visto": "Média",
        "resumo": "Londres é um dos maiores polos financeiros e de tecnologia do mundo; "
                  "exige empresa patrocinadora e custos de visto elevados.",
    },
    {
        "pais": "Polônia", "regiao": "Europa", "demanda_ti": "Alta",
        "custo_vida_mensal_usd": 1000, "salario_medio_ti_usd": 3300,
        "idioma": "Polonês / Inglês (setor de tech)",
        "visto": "Blue Card UE / Permissão de Trabalho Tipo A",
        "dificuldade_visto": "Média",
        "resumo": "Um dos maiores polos de outsourcing e centros de desenvolvimento da Europa Central, "
                  "com custo de vida baixo para a região.",
    },
    {
        "pais": "Estados Unidos", "regiao": "América do Norte", "demanda_ti": "Muito Alta",
        "custo_vida_mensal_usd": 2600, "salario_medio_ti_usd": 8500,
        "idioma": "Inglês",
        "visto": "H-1B (sorteio) / L-1 (transferência interna) / O-1",
        "dificuldade_visto": "Alta",
        "resumo": "Maiores salários do mundo em TI, porém com visto de acesso difícil (sorteio anual) "
                  "e alto custo de saúde e moradia.",
    },
    {
        "pais": "Austrália", "regiao": "Oceania", "demanda_ti": "Alta",
        "custo_vida_mensal_usd": 2300, "salario_medio_ti_usd": 5800,
        "idioma": "Inglês",
        "visto": "Skills in Demand Visa / Skilled Independent (subclasse 189)",
        "dificuldade_visto": "Média",
        "resumo": "Boa qualidade de vida e salários altos; sistema de pontos favorece profissionais de TI "
                  "com inglês fluente e experiência comprovada.",
    },
    {
        "pais": "Singapura", "regiao": "Ásia", "demanda_ti": "Alta",
        "custo_vida_mensal_usd": 2800, "salario_medio_ti_usd": 6000,
        "idioma": "Inglês",
        "visto": "Employment Pass (EP)",
        "dificuldade_visto": "Média",
        "resumo": "Hub financeiro e de tecnologia da Ásia, impostos baixos e inglês como língua oficial; "
                  "moradia é cara.",
    },
]

# ---------------------------------------------------------------------------
# MÓDULO II - GlobalIT Jobs (Inteligência de Mercado)
# ---------------------------------------------------------------------------
VAGAS = [
    {"titulo": "Backend Developer (Node.js)", "empresa": "TechNordic", "pais": "Portugal",
     "modalidade": "Remoto", "senioridade": "Pleno", "stack": ["Node.js", "TypeScript", "AWS"],
     "salario_faixa_usd": "2800-3600"},
    {"titulo": "Frontend Developer (React)", "empresa": "LisboaLabs", "pais": "Portugal",
     "modalidade": "Híbrido", "senioridade": "Júnior", "stack": ["React", "TypeScript", "CSS"],
     "salario_faixa_usd": "1900-2500"},
    {"titulo": "Suporte de Infraestrutura TI", "empresa": "BlueCloud GmbH", "pais": "Alemanha",
     "modalidade": "Híbrido", "senioridade": "Júnior", "stack": ["Linux", "Redes", "ITIL"],
     "salario_faixa_usd": "3200-4000"},
    {"titulo": "Software Engineer (Java)", "empresa": "Rheinware AG", "pais": "Alemanha",
     "modalidade": "Presencial", "senioridade": "Pleno", "stack": ["Java", "Spring Boot", "PostgreSQL"],
     "salario_faixa_usd": "4800-6200"},
    {"titulo": "DevOps Engineer", "empresa": "MapleStack", "pais": "Canadá",
     "modalidade": "Remoto", "senioridade": "Sênior", "stack": ["Kubernetes", "Terraform", "AWS"],
     "salario_faixa_usd": "6000-8000"},
    {"titulo": "Data Analyst", "empresa": "NorthernData", "pais": "Canadá",
     "modalidade": "Híbrido", "senioridade": "Júnior", "stack": ["SQL", "Python", "Power BI"],
     "salario_faixa_usd": "3500-4500"},
    {"titulo": "Suporte Técnico N2", "empresa": "GreenIsle IT", "pais": "Irlanda",
     "modalidade": "Presencial", "senioridade": "Júnior", "stack": ["Windows Server", "Active Directory"],
     "salario_faixa_usd": "3400-4200"},
    {"titulo": "Cloud Engineer", "empresa": "Liffey Systems", "pais": "Irlanda",
     "modalidade": "Híbrido", "senioridade": "Pleno", "stack": ["Azure", "Terraform", "Docker"],
     "salario_faixa_usd": "5200-6800"},
    {"titulo": "QA Automation Engineer", "empresa": "IberiaSoft", "pais": "Espanha",
     "modalidade": "Remoto", "senioridade": "Pleno", "stack": ["Python", "Selenium", "CI/CD"],
     "salario_faixa_usd": "2400-3200"},
    {"titulo": "Cloud Security Analyst", "empresa": "DesertSec", "pais": "Emirados Árabes Unidos",
     "modalidade": "Presencial", "senioridade": "Sênior", "stack": ["Azure", "SIEM", "ISO 27001"],
     "salario_faixa_usd": "5500-7000"},
    {"titulo": "Network Engineer", "empresa": "GulfNet Solutions", "pais": "Emirados Árabes Unidos",
     "modalidade": "Presencial", "senioridade": "Pleno", "stack": ["Cisco", "BGP", "Firewall"],
     "salario_faixa_usd": "4500-6000"},
    {"titulo": "Full Stack Developer", "empresa": "TulipTech", "pais": "Países Baixos",
     "modalidade": "Híbrido", "senioridade": "Pleno", "stack": ["Python", "Django", "React"],
     "salario_faixa_usd": "4500-5800"},
    {"titulo": "Site Reliability Engineer", "empresa": "Thames Digital", "pais": "Reino Unido",
     "modalidade": "Híbrido", "senioridade": "Sênior", "stack": ["Kubernetes", "Prometheus", "GCP"],
     "salario_faixa_usd": "6500-8500"},
    {"titulo": "Mobile Developer (Flutter)", "empresa": "VistulaApps", "pais": "Polônia",
     "modalidade": "Remoto", "senioridade": "Pleno", "stack": ["Flutter", "Dart", "Firebase"],
     "salario_faixa_usd": "3200-4200"},
    {"titulo": "Machine Learning Engineer", "empresa": "BayWorks AI", "pais": "Estados Unidos",
     "modalidade": "Remoto", "senioridade": "Sênior", "stack": ["Python", "PyTorch", "AWS"],
     "salario_faixa_usd": "10000-14000"},
    {"titulo": "IT Helpdesk Technician", "empresa": "Southern Cross IT", "pais": "Austrália",
     "modalidade": "Presencial", "senioridade": "Júnior", "stack": ["Windows", "Microsoft 365", "ITIL"],
     "salario_faixa_usd": "3800-4800"},
    {"titulo": "Cybersecurity Analyst", "empresa": "MerlionSec", "pais": "Singapura",
     "modalidade": "Presencial", "senioridade": "Pleno", "stack": ["SIEM", "Splunk", "MITRE ATT&CK"],
     "salario_faixa_usd": "5500-7500"},
    {"titulo": "Backend Developer (Python)", "empresa": "Atlantic Freelance Hub", "pais": "Portugal",
     "modalidade": "Remoto", "senioridade": "Júnior", "stack": ["Python", "FastAPI", "PostgreSQL"],
     "salario_faixa_usd": "2000-2800"},
]

RADAR_TECNOLOGIAS = [
    {"tecnologia": "Python", "categoria": "Linguagem", "demanda": 92},
    {"tecnologia": "JavaScript / TypeScript", "categoria": "Linguagem", "demanda": 88},
    {"tecnologia": "AWS", "categoria": "Cloud", "demanda": 85},
    {"tecnologia": "Docker / Kubernetes", "categoria": "DevOps", "demanda": 80},
    {"tecnologia": "Linux (Suporte/Admin)", "categoria": "Infraestrutura", "demanda": 78},
    {"tecnologia": "SQL", "categoria": "Dados", "demanda": 75},
    {"tecnologia": "Java", "categoria": "Linguagem", "demanda": 72},
    {"tecnologia": "Azure", "categoria": "Cloud", "demanda": 70},
    {"tecnologia": "React", "categoria": "Frontend", "demanda": 68},
    {"tecnologia": "CI/CD (GitHub Actions / GitLab)", "categoria": "DevOps", "demanda": 66},
    {"tecnologia": "Cibersegurança (SIEM / SOC)", "categoria": "Segurança", "demanda": 64},
    {"tecnologia": "Active Directory", "categoria": "Infraestrutura", "demanda": 60},
    {"tecnologia": "Terraform", "categoria": "DevOps", "demanda": 55},
    {"tecnologia": "Machine Learning (PyTorch / TensorFlow)", "categoria": "IA / Dados", "demanda": 52},
]

TRILHAS_QUALIFICACAO = [
    {"area": "Suporte / Redes", "competencia": "Redes e Infraestrutura",
     "certificacoes": ["CompTIA Network+", "CCNA", "ITIL Foundation"]},
    {"area": "Cloud", "competencia": "Computação em Nuvem",
     "certificacoes": ["AWS Cloud Practitioner", "AWS Solutions Architect Associate",
                       "Azure Fundamentals (AZ-900)"]},
    {"area": "Segurança", "competencia": "Cibersegurança",
     "certificacoes": ["CompTIA Security+", "ISO 27001 Foundation"]},
    {"area": "Desenvolvimento", "competencia": "Programação Backend",
     "certificacoes": ["Python Institute PCEP", "freeCodeCamp Backend", "Node.js Certification"]},
    {"area": "DevOps", "competencia": "Automação e Deploy",
     "certificacoes": ["Docker Certified Associate", "Certified Kubernetes Administrator (CKA)",
                       "HashiCorp Terraform Associate"]},
    {"area": "Dados", "competencia": "Análise e Engenharia de Dados",
     "certificacoes": ["Microsoft PL-300 (Power BI)", "Google Data Analytics", "Databricks Fundamentals"]},
    {"area": "Idiomas", "competencia": "Inglês para o mercado internacional",
     "certificacoes": ["IELTS", "TOEFL iBT", "Cambridge B2 First", "Duolingo English Test"]},
]
