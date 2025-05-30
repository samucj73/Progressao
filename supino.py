def gerar_cartao_supino(nome, carga_atual, experiencia, objetivo):
    if experiencia == "Iniciante":
        incremento = 2.5
    elif experiencia == "Intermediário":
        incremento = 5
    else:
        incremento = 7.5

    if objetivo == "Força":
        reps_semana = [(4, 6), (5, 5), (5, 3), (3, 2)]
    elif objetivo == "Hipertrofia":
        reps_semana = [(4, 10), (4, 8), (4, 10), (3, 8)]
    else:
        reps_semana = [(3, 10), (3, 8), (3, 6), (3, 5)]

    cargas = [carga_atual + i * incremento for i in range(4)]
    plano = {}

    for i in range(4):
        plano[f"Semana {i + 1}"] = f"{reps_semana[i][0]}x{reps_semana[i][1]} com {cargas[i]:.1f} kg"

    return plano