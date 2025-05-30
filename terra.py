def gerar_cartao_terra(nome, carga_atual, experiencia, objetivo):
    if experiencia == "Iniciante":
        incremento = 5
    elif experiencia == "Intermediário":
        incremento = 10
    else:
        incremento = 15

    if objetivo == "Força":
        reps_semana = [(3, 5), (4, 4), (4, 3), (3, 2)]
    else:
        reps_semana = [(4, 10), (4, 8), (3, 8), (3, 6)]

    cargas = [carga_atual + i * incremento for i in range(4)]
    plano = {}

    for i in range(4):
        plano[f"Semana {i + 1}"] = f"{reps_semana[i][0]}x{reps_semana[i][1]} com {cargas[i]:.1f} kg"

    return plano