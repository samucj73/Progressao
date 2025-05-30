import streamlit as st

def gerar_cartao_kano(nome, peso_atual, frequencia, barra, objetivo, experiencia):
    st.markdown(f"<h2 style='text-align: center;'>📋 Cartão Kanō – Agachamento de {nome}</h2>", unsafe_allow_html=True)

    # Definir incremento de carga por nível
    if experiencia == "Iniciante":
        incremento = 5
    elif experiencia == "Intermediário":
        incremento = 7.5
    else:  # Avançado
        incremento = 10

    # Definir volume por objetivo
    if objetivo == "Técnica":
        reps_semana = [(4, 10), (4, 8), (3, 6), (3, 5)]
    elif objetivo == "Hipertrofia":
        reps_semana = [(4, 10), (4, 8), (4, 8), (3, 10)]
    else:  # Força
        reps_semana = [(4, 6), (4, 5), (5, 5), (3, 3)]

    # Calcular cargas para 4 semanas
    cargas = [peso_atual + i * incremento for i in range(4)]
    plano = {}

    for i in range(4):  # 4 semanas
        semana = f"Semana {i + 1}"
        tarefas = []
        for d in range(frequencia):
            tipo_barra = "Agachamento livre" if (barra == "Livre" or barra == "Ambas") else "Barra guiada"
            if barra == "Ambas" and d % 2 == 1:
                tipo_barra = "Barra guiada"
            series, reps = reps_semana[i]
            carga = cargas[i] - 5 if d % 2 == 1 and objetivo == "Técnica" else cargas[i]
            tarefa = f"Dia {d + 1}: {tipo_barra} – {series}x{reps} com {carga:.0f} kg"
            tarefas.append(tarefa)
        plano[semana] = tarefas

    for semana, tarefas in plano.items():
        with st.expander(semana):
            for tarefa in tarefas:
                st.write("✅", tarefa)

    st.info(f"💡 Dica: Ao fim da Semana 4, você pode testar 1 repetição com até **{cargas[-1] + 5:.0f} kg**, se estiver confortável.")

# --- Interface Streamlit ---
st.markdown("<h1 style='text-align: center;'>🏋️ Cartão Kanō Inteligente – Agachamento</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Preencha as informações abaixo para gerar seu plano de agachamento personalizado:</p>", unsafe_allow_html=True)

nome = st.text_input("Nome:")
peso_atual = st.number_input("Carga atual do agachamento (kg):", min_value=20.0, max_value=300.0, step=2.5)
frequencia = st.selectbox("Quantos dias por semana você treina perna?", [1, 2, 3])
barra = st.selectbox("Qual tipo de barra você usa?", ["Livre", "Guiada", "Ambas"])
objetivo = st.selectbox("Qual seu objetivo principal?", ["Técnica", "Hipertrofia", "Força"])
experiencia = st.selectbox("Qual seu nível com agachamento?", ["Iniciante", "Intermediário", "Avançado"])

if st.button("Gerar Cartão Kanō"):
    if nome and peso_atual:
        gerar_cartao_kano(nome, peso_atual, frequencia, barra, objetivo, experiencia)
    else:
        st.warning("Por favor, preencha todos os campos.")

# --- Rodapé personalizado ---
st.markdown("""
<br><br><hr>
<p style='text-align: center; color: gray;'>© 2025 SAMUCJ TECHNOLOGY</p>
""", unsafe_allow_html=True)
