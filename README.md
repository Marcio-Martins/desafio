# Sistema Bancário em Python — Desafio

Exercício de programação em Python para praticar lógica, condicionais, laços de repetição, operações aritméticas e interação com o usuário pelo terminal.

## Funcionalidades

- Depositar valores positivos.
- Sacar respeitando o saldo disponível, o limite por saque e a quantidade máxima de saques.
- Consultar extrato e saldo atual.
- Encerrar o programa pelo menu.
- Tratar entradas numéricas inválidas sem interromper o programa.
- Aceitar vírgula ou ponto como separador decimal.

## Pré-requisitos

- Python 3
- Terminal ou Visual Studio Code

## Como executar

~~~bash
python desafio.py
~~~

## Testes automatizados

Os testes cobrem a leitura de valores com ponto ou vírgula decimal e o tratamento de entradas inválidas e infinitas.

~~~bash
python -m unittest discover -s tests -v
~~~

## Conceitos praticados

- Laços e condicionais
- Controle de estado com variáveis
- Validação de entrada e tratamento de ValueError
- Verificação de valores finitos
- Testes automatizados com unittest

## Limitações

Este é um exercício didático e utiliza float para valores monetários. Para uma aplicação financeira real, seria necessário adotar representação decimal apropriada, persistência de dados, autenticação, auditoria e testes abrangentes.

## Autor

Márcio Martins · [Perfil GitHub](https://github.com/Marcio-Martins) · [LinkedIn](https://www.linkedin.com/in/marcio-martins-eufrazio/)
