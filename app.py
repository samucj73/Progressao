import streamlit as st

st.set_page_config(page_title="KanōPlan", layout="centered")

st.markdown("<h1 style='text-align: center;'>KanōPlan - Gerador de Cartão de Treino</h1>", unsafe_allow_html=True)

st.markdown("---")

nome = st.text_input("👤 Seu nome:")
experiencia = st.selectbox("🎯 Nível de experiência:", ["Iniciante", "Intermediário", "Avançado"])
dias_treino = st.slider("📅 Dias de treino por semana:", 1, 6, 2)
objetivo = st.selectbox("🏆 Objetivo principal:", ["Hipertrofia", "Força", "Resistência"])
barra = st.selectbox("🏋️‍♂️ Tipo de barra disponível:", ["Livre", "Guiada", "Ambas"])
exercicio = st.selectbox("💪 Exercício principal:", ["Agachamento", "Supino", "Levantamento Terra", "Bíceps", "Tríceps"])
carga_atual = st.number_input("📦 Carga atual (em kg):", min_value=0.0, step=2.5)

if st.button("🔁 Gerar plano de treino"):
    if not nome:
        st.warning("Por favor, digite seu nome.")
    else:
        if exercicio == "Agachamento":
            from agachamento import gerar_cartao_agachamento, get_variacoes, get_tecnica, get_musculos_env
            from auxiliares_agachamento import get_auxiliares

            plano = gerar_cartao_agachamento(nome, carga_atual, experiencia, objetivo, dias_treino)
            for semana, treino in plano.items():
                with st.expander(semana):
                    st.write("✅", treino)

            with st.expander("📌 Técnica de Execução"):
                st.markdown(get_tecnica())

            with st.expander("🔁 Variações do Exercício"):
                for var in get_variacoes():
                    st.markdown(f"- {var}")

            with st.expander("💪 Músculos Envolvidos"):
                musc = get_musculos_env()
                st.markdown("**Principais:** " + ", ".join(musc['principais']))
                st.markdown("**Auxiliares:** " + ", ".join(musc['auxiliares']))

            with st.expander("➕ Exercícios Auxiliares"):
                for aux in get_auxiliares():
                    st.markdown(f"- {aux}")

        if exercicio == "Supino":
            from supino import gerar_cartao_supino, get_variacoes, get_tecnica, get_musculos_env, get_auxiliares

            plano = gerar_cartao_supino(nome, carga_atual, experiencia, objetivo, dias_treino)
            for semana, treino in plano.items():
                with st.expander(semana):
                    st.write("✅", treino)

            with st.expander("📌 Técnica de Execução"):
                st.markdown(get_tecnica())

            with st.expander("🔁 Variações do Exercício"):
                for var in get_variacoes():
                    st.markdown(f"- {var}")

            with st.expander("💪 Músculos Envolvidos"):
                musc = get_musculos_env()
                st.markdown("**Principais:** " + ", ".join(musc['principais']))
                st.markdown("**Auxiliares:** " + ", ".join(musc['auxiliares']))

            with st.expander("➕ Exercícios Auxiliares"):
                for aux in get_auxiliares():
                    st.markdown(f"- {aux}")

        if exercicio == "Levantamento Terra":
            from terra import gerar_cartao_terra, get_variacoes, get_tecnica, get_musculos_env, get_auxiliares

            plano = gerar_cartao_terra(nome, carga_atual, experiencia, objetivo, dias_treino)
            for semana, treino in plano.items():
                with st.expander(semana):
                    st.write("✅", treino)

            with st.expander("📌 Técnica de Execução"):
                st.markdown(get_tecnica())

            with st.expander("🔁 Variações do Exercício"):
                for var in get_variacoes():
                    st.markdown(f"- {var}")

            with st.expander("💪 Músculos Envolvidos"):
                musc = get_musculos_env()
                st.markdown("**Principais:** " + ", ".join(musc['principais']))
                st.markdown("**Auxiliares:** " + ", ".join(musc['auxiliares']))

            with st.expander("➕ Exercícios Auxiliares"):
                for aux in get_auxiliares():
                    st.markdown(f"- {aux}")

        if exercicio == "Bíceps":
            from biceps import gerar_cartao_biceps, get_variacoes, get_tecnica, get_musculos_env, get_auxiliares

            plano = gerar_cartao_biceps(nome, carga_atual, experiencia, objetivo, dias_treino)
            for semana, treino in plano.items():
                with st.expander(semana):
                    st.write("✅", treino)

            with st.expander("📌 Técnica de Execução"):
                st.markdown(get_tecnica())

            with st.expander("🔁 Variações do Exercício"):
                for var in get_variacoes():
                    st.markdown(f"- {var}")

            with st.expander("💪 Músculos Envolvidos"):
                musc = get_musculos_env()
                st.markdown("**Principais:** " + ", ".join(musc['principais']))
                st.markdown("**Auxiliares:** " + ", ".join(musc['auxiliares']))

            with st.expander("➕ Exercícios Auxiliares"):
                for aux in get_auxiliares():
                    st.markdown(f"- {aux}")

        if exercicio == "Tríceps":
            from triceps import gerar_cartao_triceps, get_variacoes, get_tecnica, get_musculos_env, get_auxiliares

            plano = gerar_cartao_triceps(nome, carga_atual, experiencia, objetivo, dias_treino)
            for semana, treino in plano.items():
                with st.expander(semana):
                    st.write("✅", treino)

            with st.expander("📌 Técnica de Execução"):
                st.markdown(get_tecnica())

            with st.expander("🔁 Variações do Exercício"):
                for var in get_variacoes():
                    st.markdown(f"- {var}")

            with st.expander("💪 Músculos Envolvidos"):
                musc = get_musculos_env()
                st.markdown("**Principais:** " + ", ".join(musc['principais']))
                st.markdown("**Auxiliares:** " + ", ".join(musc['auxiliares']))

            with st.expander("➕ Exercícios Auxiliares"):
                for aux in get_auxiliares():
                    st.markdown(f"- {aux}")

st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 SAMUCJ TECHNOLOGY</p>", unsafe_allow_html=True)
