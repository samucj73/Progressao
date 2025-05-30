def gerar_cartao_supino(nome, carga_atual, experiencia, objetivo, dias_treino):
    plano = {}
    for semana in range(1, 5):
        reps = "12-10-8" if objetivo == "Hipertrofia" else "8-6-5" if objetivo == "Força" else "3x15 (técnica e controle)"
        carga_prog = round(carga_atual * (1 + 0.015 * semana), 1)
        plano[f"Semana {semana}"] = (
            f"{nome}, semana {semana}:\n"
            f"- Supino reto: {reps} com ~{carga_prog}kg\n"
            f"- Frequência: {dias_treino}x por semana"
        )
    return plano

def get_variacoes():
    return [
        "Supino inclinado com barra",
        "Supino declinado",
        "Supino com halteres",
        "Crucifixo reto/inclinado",
        "Peck deck"
    ]

def get_tecnica():
    return (
        "1. Deite no banco com os pés firmes no chão.\n"
        "2. Segure a barra com pegada média.\n"
        "3. Abaixe a barra controladamente até o peito.\n"
        "4. Suba a barra até estender totalmente os cotovelos.\n"
        "5. Mantenha os ombros estabilizados."
    )

def get_musculos_env():
    return {
        "principais": ["Peitoral maior", "Tríceps braquial", "Deltoide anterior"],
        "auxiliares": ["Serrátil anterior", "Core"]
    }

def get_auxiliares():
    return [
        "Flexões de braço",
        "Paralelas (dips)",
        "Crossover na polia",
        "Pressão com halteres em banco inclinado",
        "Barra paralela com peso corporal"
    ]
