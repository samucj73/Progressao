import streamlit as st
from agachamento import gerar_cartao_agachamento
from supino import gerar_cartao_supino
from terra import gerar_cartao_terra
from biceps import gerar_cartao_biceps
from triceps import gerar_cartao_triceps

st.markdown("<h1 style='text-align: center;'>🏋️ Cartão Kanō Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Monte seu plano de treino personalizado por exercício.</p><hr>", unsafe_allow_html=True)

exercicio = st.selectbox("Selecione o exercício:", ["Agachamento", "Supino", "Levantamento Terra", "Bíceps", "Tríceps"])

if exercicio:
    nome = st.text_input("Nome:")
    carga_atual = st.number_input("Carga atual (kg):", min_value=10.0, max_value=300.0, step=2.5)
    experiencia = st.selectbox("Nível de experiência:", ["Iniciante", "Intermediário", "Avançado"])
    objetivo = st.selectbox("Objetivo principal:", ["Força", "Hipertrofia", "Técnica"])
    dias_treino = st.selectbox("Dias de treino por semana:", [1, 2, 3, 4, 5, 6])

    if exercicio == "Agachamento":
        barra = st.selectbox("Tipo de barra:", ["Livre", "Guiada", "Ambas"])
        if st.button("Gerar Plano"):
            gerar_cartao_agachamento(nome, carga_atual, dias_treino, barra, objetivo, experiencia)

    elif exercicio == "Supino":
        if st.button("Gerar Plano"):
            plano = gerar_cartao_supino(nome, carga_atual, experiencia, objetivo, dias_treino)

            for semana, treino in plano.items():
                with st.expander(semana):
                    st.write("✅", treino)

            with st.expander("📌 Técnica de Execução"):
                st.markdown(get_tecnica_terra())

            with st.expander("🔁 Variações do Terra"):
                for var in get_variacoes_terra():
                    st.markdown(f"- {var}")

            with st.expander("💪 Músculos Envolvidos"):
                musc = get_musculos_terra()
                st.markdown("**Principais:** " + ", ".join(musc['principais']))
                st.markdown("**Auxiliares:** " + ", ".join(musc['auxiliares']))

            with st.expander("➕ Exercícios Auxiliares"):
                for aux in get_auxiliares_terra():
                    st.markdown(f"- {aux}")


    el
    if exercicio == "Levantamento Terra":
        from terra import get_variacoes as get_variacoes_terra, get_tecnica as get_tecnica_terra, get_musculos_env as get_musculos_terra, get_auxiliares as get_auxiliares_terra

        if st.button("Gerar Plano"):
            
            plano = gerar_cartao_terra(nome, carga_atual, experiencia, objetivo, dias_treino)
            for semana, treino in plano.items():

                with st.expander(semana):
                    st.write("✅", treino)

    elif exercicio == "Bíceps":
        if st.button("Gerar Plano de Bíceps"):
            plano = gerar_cartao_biceps(dias_treino)

            for semana, treino in plano.items():
                with st.expander(semana):
                    st.write("✅", treino)

            with st.expander("📌 Técnica de Execução"):
                st.markdown(get_tecnica_terra())

            with st.expander("🔁 Variações do Terra"):
                for var in get_variacoes_terra():
                    st.markdown(f"- {var}")

            with st.expander("💪 Músculos Envolvidos"):
                musc = get_musculos_terra()
                st.markdown("**Principais:** " + ", ".join(musc['principais']))
                st.markdown("**Auxiliares:** " + ", ".join(musc['auxiliares']))

            with st.expander("➕ Exercícios Auxiliares"):
                for aux in get_auxiliares_terra():
                    st.markdown(f"- {aux}")


    elif exercicio == "Tríceps":
        if st.button("Gerar Plano de Tríceps"):
            plano = gerar_cartao_triceps(dias_treino)

            for semana, treino in plano.items():
                with st.expander(semana):
                    st.write("✅", treino)

            with st.expander("📌 Técnica de Execução"):
                st.markdown(get_tecnica_terra())

            with st.expander("🔁 Variações do Terra"):
                for var in get_variacoes_terra():
                    st.markdown(f"- {var}")

            with st.expander("💪 Músculos Envolvidos"):
                musc = get_musculos_terra()
                st.markdown("**Principais:** " + ", ".join(musc['principais']))
                st.markdown("**Auxiliares:** " + ", ".join(musc['auxiliares']))

            with st.expander("➕ Exercícios Auxiliares"):
                for aux in get_auxiliares_terra():
                    st.markdown(f"- {aux}")


st.markdown("""
<br><hr>
<p style='text-align: center; color: gray;'>© 2025 SAMUCJ TECHNOLOGY</p>
""", unsafe_allow_html=True)