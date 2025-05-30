import streamlit as st
from auxiliares_agachamento import get_exercicios_auxiliares

def gerar_cartao_agachamento(nome, carga_atual, frequencia, barra, objetivo, experiencia):
    if experiencia == "Iniciante":
        incremento = 5
    elif experiencia == "Intermediário":
        incremento = 10
    else:
        incremento = 15

    if objetivo == "Força":
        reps = [(3, 6), (4, 5), (4, 3), (3, 2)]
    elif objetivo == "Hipertrofia":
        reps = [(4, 10), (4, 8), (4, 10), (3, 8)]
    else:
        reps = [(3, 10), (3, 8), (3, 6), (3, 5)]

    cargas = [carga_atual + i * incremento for i in range(4)]
    plano = {}

    for i in range(4):
        plano[f"Semana {i + 1}"] = [
            f"{reps[i][0]}x{reps[i][1]} com {cargas[i]:.1f} kg na barra {barra.lower()}"
        ]

    for semana, tarefas in plano.items():
        with st.expander(semana):
            for tarefa in tarefas:
                st.write("✅", tarefa)
            st.markdown("**🔧 Exercícios auxiliares da semana:**")
            auxiliares = get_exercicios_auxiliares()
            for grupo, exercicio in auxiliares.items():
                st.write(f"- {grupo}: {exercicio}")

    st.info(f"💡 Ao fim da Semana 4, você pode testar 1 repetição com até {cargas[-1] + 5:.0f} kg.")