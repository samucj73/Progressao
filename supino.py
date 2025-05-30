def gerar_cartao_supino(nome, carga_atual, experiencia, objetivo, dias_treino):
    plano = {}
    for semana in range(1, 5):
        reps = "12-10-8" if objetivo == "Hipertrofia" else "5x5" if objetivo == "Força" else "3x12 (leve e técnico)"
        carga_prog = round(carga_atual * (1 + 0.02 * semana), 1)
        plano[f"Semana {semana}"] = (
            f"{nome}, semana {semana}:
"
            f"- Supino reto: {reps} com ~{carga_prog}kg\n"
            f"- Incluir variações e auxiliares conforme lista abaixo."
        )
    return plano

def get_variacoes():
    return [
        "Supino inclinado com barra",
        "Supino declinado com barra",
        "Supino reto com halteres",
        "Supino inclinado com halteres",
        "Supino com pegada fechada",
    ]

def get_tecnica():
    return (
        "1. Deite-se com os pés firmes no chão e a lombar levemente arqueada.\n"
        "2. Pegue a barra com uma pegada ligeiramente mais aberta que os ombros.\n"
        "3. Abaixe a barra até o meio do peito, controlando o movimento.\n"
        "4. Suba até quase estender totalmente os braços sem travar os cotovelos.\n"
        "5. Mantenha escápulas retraídas e contração no peitoral durante toda a execução."
    )

def get_musculos_env():
    return {
        "principais": ["Peitoral maior", "Tríceps braquial", "Deltoide anterior"],
        "auxiliares": ["Serrátil anterior", "Músculos do core", "Trapézio inferior"]
    }

def get_auxiliares():
    return [
        "Crossover na polia",
        "Flexão de braço (push-up)",
        "Pullover com halter",
        "Tríceps na paralela",
        "Desenvolvimento com halteres",
    ]