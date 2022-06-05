import streamlit as st

import Controllers.ClienteConroller as clienteController
import models.Cliente as cliente

st.title("Cadastro de Clientes")

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome: ")
    input_age = st.number_input(label="Insira a sua idade: ", format='%d', step=1)
    input_occupation = st.selectbox('Selecione sua profissão: ', ['Desenvolvedor', 'Músico', 'Designer', 'Professor'])
    input_button_submit = st.form_submit_button("Enviar")

if input_button_submit:
    cliente.nome = input_name
    cliente.idade = input_age
    cliente.profissao = input_occupation

    clienteController.incluir(cliente)