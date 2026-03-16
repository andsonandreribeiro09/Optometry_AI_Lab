import streamlit as st

def vision_test():

    st.title("Teste de Visão")

    st.markdown("""
        ## E
        ### F P
        #### T O Z
    """)

    answer = st.radio(
        "Qual linha você vê melhor?",
        ["Linha 1", "Linha 2", "Linha 3"]
    )

    return answer