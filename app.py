import streamlit as st
import contrato
from datetime import datetime, time

def main():

    st.title('Sistema de CRM e vendas')
    email = st.text_input('Campo texto de inserção email do vendedor')
    data = st.date_input('Data da compra')
    hora = st.time_input('Hora da compra')
    valor = st.number_input('Campo numérico para inserir o valor monetário da venda realizada')
    quantidade = st.number_input('Quantidade de produtos', min_value=1, step=1)
    produto = st.selectbox('Produto', options= ['Gemini', 'ChatGPT', 'Llama3.0'])

    if st.button('Salvar'):

        data_hora = datetime.combine(data, hora)
        st.write('--Dados da venda--')
        st.write(f'Email do Vendedor:{email}')
        st.write(f'Data e hora da compra:{data_hora}')
        st.write(f'Valor da venda: R$ {valor:.2f}')
        st.write(f'Quantidade de produtos: {quantidade}')
        st.write(f'Produto: {produto}')


if __name__ == '__main__':
    main()

