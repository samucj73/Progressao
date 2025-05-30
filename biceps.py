def gerar_cartao_biceps(nome, carga_atual, experiencia, objetivo, dias_treino):
    plano = {}
    for semana in range(1, 5):
        reps = "12-10-8" if objetivo == "Hipertrofia" else "8-6-5" if objetivo == "Força" else "3x15 controle e técnica"
        carga_prog = round(carga_atual * (1 + 0.015 * semana), 1)
        plano[f"Semana {semana}"] = (
            f"{nome}, semana {semana}:\n"
            f"- Rosca direta com barra: {reps} com ~{carga_prog}kg\n"
            f"- Frequência: {dias_treino}x por semana"
        )
    return plano

def get_variacoes():
    return [
        "Rosca alternada com halteres",
        "Rosca scott",
        "Rosca concentrada",
        "Rosca 21",
        "Rosca martelo"
    ]

def get_tecnica():
    return (
        "1. Pegue a barra com as palmas voltadas para cima.\n"
        "2. Cotovelos colados ao tronco.\n"
        "3. Flexione os cotovelos até a contração total.\n"
        "4. Retorne devagar à posição inicial.\n"
        "5. Evite balanços com o corpo."
    )

def get_musculos_env():
    return {
        "principais": ["Bíceps braquial", "Braquial anterior"],
        "auxiliares": ["Braquiorradial", "Antebraço"]
    }

def get_auxiliares():
    return [
        "Rosca martelo cruzada",
        "Rosca direta na barra W",
        "Rosca com cabo na polia baixa",
        "Rosca concentrada unilateral",
        "Rosca 21 com variação de pegada"
    ]
