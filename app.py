import streamlit as st

#----------------------- SIDEBAR
st.sidebar.image ("image.png")
st.sidebar.title (" Premium Drive - Aluguel de carros")

carros = ["Porcher", "Chevette", "Opala", "BMW"]

carro = st.sidebar.selectbox("Escolha seu carro:", carros)

#-----------------------------------------BODY
st.title("Premiun Drive - aluguel de Carros")

st.image(f'{carro}.png')
st.write(f"Voce escolheu o {carro}")

if carro == "Porcher":
    diaria = 1.500

elif carro == "Chevette":
    diaria = 500

elif carro == "opala":
    diaria = 350

elif carro == "BMW":
    diaria = 2.000

dias = st.text_input(f"Por quantos dias voce alugou o carro {carro}")
km = st.text_input(f"Quantos km voce rodou hoje com o {carro}")

if st.button("Calcular"):
    dias = float(dias)
    km = float(km)

    total = (diaria * dias) + (km* 0.15)
    st.warning(f"""Voce alugou o {carro} por {dias} dias e rodou {km} km. o total a pagar é R${total}.""")