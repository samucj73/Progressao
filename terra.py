def gerar_cartao_terra(nome, carga_atual, experiencia, objetivo, dias_treino):
    plano = {}
    for semana in range(1, 5):
        reps = "6-5-4" if objetivo == "Força" else "10-8-6" if objetivo == "Hipertrofia" else "3x10 (leve e técnico)"
        carga_prog = round(carga_atual * (1 + 0.025 * semana), 1)
        plano[f"Semana {semana}"] = (
            f"{nome}, semana {semana}:
"
            f"- Levantamento terra: {reps} com ~{carga_prog}kg\n"
            f"- Incluir variações e auxiliares conforme lista abaixo."
        )
    return plano

def get_variacoes():
    return [
        "Levantamento terra com barra hexagonal",
        "Levantamento terra sumô",
        "Levantamento terra com halteres",
        "Levantamento terra com pausa",
        "Levantamento terra com déficit",
    ]

def get_tecnica():
    return (
        "1. Posição dos pés na largura do quadril, barra próxima das canelas.\n"
        "2. Segure a barra com pegada pronada ou alternada, ombros para trás.\n"
        "3. Coluna neutra, peito aberto, contraia o abdômen.\n"
        "4. Empurre o chão com os pés e erga o tronco até a posição ereta.\n"
        "5. Volte de forma controlada, mantendo a barra próxima ao corpo."
    )

def get_musculos_env():
    return {
        "principais": ["Glúteos", "Isquiotibiais", "Eretor da espinha", "Dorsal"],
        "auxiliares": ["Trapézio", "Antebraço", "Core", "Quadríceps"]
    }

def get_auxiliares():
    return [
        "Good Morning com barra",
        "Stiff com halteres",
        "Remada curvada",
        "Hiperextensão lombar",
        "Agachamento frontal",
    ]