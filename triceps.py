def gerar_cartao_triceps(nome, carga_atual, experiencia, objetivo, dias_treino):
    plano = {}
    for semana in range(1, 5):
        reps = "12-10-8" if objetivo == "Hipertrofia" else "8-6-5" if objetivo == "Força" else "3x15 controle e técnica"
        carga_prog = round(carga_atual * (1 + 0.015 * semana), 1)
        plano[f"Semana {semana}"] = (
            f"{nome}, semana {semana}:\n"
            f"- Tríceps testa com barra: {reps} com ~{carga_prog}kg\n"
            f"- Frequência: {dias_treino}x por semana"
        )
    return plano

def get_variacoes():
    return [
        "Tríceps na polia alta (cabo)",
        "Tríceps francês com halteres",
        "Mergulho entre bancos",
        "Tríceps coice com halteres",
        "Paralelas com peso corporal"
    ]

def get_tecnica():
    return (
        "1. Deitado no banco, segure a barra acima da cabeça.\n"
        "2. Flexione os cotovelos levando a barra para a testa.\n"
        "3. Estenda os cotovelos controladamente.\n"
        "4. Mantenha o cotovelo fixo e evite abrir os braços.\n"
        "5. Respiração constante e core ativado."
    )

def get_musculos_env():
    return {
        "principais": ["Tríceps braquial (longa, medial e lateral)"],
        "auxiliares": ["Anconeu", "Core", "Deltoide anterior"]
    }

def get_auxiliares():
    return [
        "Tríceps corda na polia",
        "Tríceps testa com halteres",
        "Kickback unilateral",
        "Tríceps banco",
        "Tríceps francês unilateral"
    ]
