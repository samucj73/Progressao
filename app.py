import streamlit as st
from agachamento import gerar_cartao_agachamento
from supino import gerar_cartao_supino
from terra import gerar_cartao_terra
from biceps import gerar_cartao_biceps
from triceps import gerar_cartao_triceps

st.markdown("<h1 style='text-align: center;'>🏋️ Cartão Kanō Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Monte seu plano de treino personalizado por exercício.</p><hr>", unsafe_allow_html=True)

exercicio = st.selectbox("Selecione o exercício:", ["Agachamento", "Supino", "Levantamento Terra", "Bíceps", "Tríceps"])

if exercicio in ["Agachamento", "Supino", "Levantamento Terra"]:
    nome = st.text_input("Nome:")
    carga_atual = st.number_input("Carga atual (kg):", min_value=10.0, max_value=300.0, step=2.5)
    experiencia = st.selectbox("Nível de experiência:", ["Iniciante", "Intermediário", "Avançado"])
    objetivo = st.selectbox("Objetivo principal:", ["Força", "Hipertrofia", "Técnica"])

    if st.button("Gerar Plano"):
        if exercicio == "Agachamento":
            frequencia = st.selectbox("Dias por semana (perna):", [1, 2, 3])
            barra = st.selectbox("Tipo de barra:", ["Livre", "Guiada", "Ambas"])
            gerar_cartao_agachamento(nome, carga_atual, frequencia, barra, objetivo, experiencia)
        elif exercicio == "Supino":
            plano = gerar_cartao_supino(nome, carga_atual, experiencia, objetivo)
            for semana, treino in plano.items():
                with st.expander(semana):
                    st.write("✅", treino)
        elif exercicio == "Levantamento Terra":
            plano = gerar_cartao_terra(nome, carga_atual, experiencia, objetivo)
            for semana, treino in plano.items():
                with st.expander(semana):
                    st.write("✅", treino)

elif exercicio == "Bíceps":
    if st.button("Gerar Plano de Bíceps"):
        plano = gerar_cartao_biceps()
        for semana, treino in plano.items():
            with st.expander(semana):
                st.write("✅", treino)

elif exercicio == "Tríceps":
    if st.button("Gerar Plano de Tríceps"):
        plano = gerar_cartao_triceps()
        for semana, treino in plano.items():
            st.write("✅", treino)

st.markdown("""
<br><hr>
<p style='text-align: center; color: gray;'>© 2025 SAMUCJ TECHNOLOGY</p>
""", unsafe_allow_html=True)