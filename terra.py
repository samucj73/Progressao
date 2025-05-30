def gerar_cartao_terra(nome, carga_atual, experiencia, objetivo, dias_treino):
    plano = {}
    for semana in range(1, 5):
        reps = "10-8-6" if objetivo == "Hipertrofia" else "5-3-2" if objetivo == "Força" else "3x12 técnica e controle"
        carga_prog = round(carga_atual * (1 + 0.02 * semana), 1)
        plano[f"Semana {semana}"] = (
            f"{nome}, semana {semana}:\n"
            f"- Levantamento Terra: {reps} com ~{carga_prog}kg\n"
            f"- Frequência: {dias_treino}x por semana"
        )
    return plano

def get_variacoes():
    return [
        "Terra sumô",
        "Terra romeno",
        "Rack pull",
        "Stiff com halteres",
        "Terra com barra hexagonal"
    ]

def get_tecnica():
    return (
        "1. Pés na largura dos ombros, barra próxima à canela.\n"
        "2. Segure a barra com pegada firme.\n"
        "3. Mantenha a coluna reta e o core ativado.\n"
        "4. Eleve a barra estendendo quadril e joelhos simultaneamente.\n"
        "5. Retorne com controle."
    )

def get_musculos_env():
    return {
        "principais": ["Glúteos", "Isquiotibiais", "Erectores da espinha"],
        "auxiliares": ["Trapézio", "Antebraço", "Core"]
    }

def get_auxiliares():
    return [
        "Hip Thrust",
        "Boa manhã",
        "Stiff com halteres",
        "Extensão lombar (mesa romana)",
        "Kettlebell swing"
    ]
