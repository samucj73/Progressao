def gerar_cartao_agachamento(nome, carga_atual, experiencia, objetivo, dias_treino):
    plano = {}
    for semana in range(1, 5):
        reps = "12-10-8" if objetivo == "Hipertrofia" else "8-6-5" if objetivo == "Força" else "3x15 (técnica e controle)"
        carga_prog = round(carga_atual * (1 + 0.02 * semana), 1)
        plano[f"Semana {semana}"] = (
            f"{nome}, semana {semana}:\n"
            f"- Agachamento {'Livre' if experiencia != 'Iniciante' else 'na Barra Guiada'}: {reps} com ~{carga_prog}kg\n"
            f"- Frequência semanal: {dias_treino}x por semana"
        )
    return plano

def get_variacoes():
    return [
        "Agachamento frontal",
        "Agachamento sumô",
        "Agachamento búlgaro",
        "Agachamento com halteres",
        "Agachamento na máquina Smith"
    ]

def get_tecnica():
    return (
        "1. Mantenha os pés na largura dos ombros.\n"
        "2. Desça controladamente mantendo a coluna neutra.\n"
        "3. Coxas paralelas ao chão ou abaixo (se possível).\n"
        "4. Suba empurrando os calcanhares no chão.\n"
        "5. Respire corretamente durante o movimento."
    )

def get_musculos_env():
    return {
        "principais": ["Quadríceps", "Glúteos", "Posterior de coxa"],
        "auxiliares": ["Core", "Panturrilhas", "Erectores da espinha"]
    }
