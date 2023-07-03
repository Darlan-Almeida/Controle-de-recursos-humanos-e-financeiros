# Controle-de-recursos-humanos-e-financeiros
criação de um sistema  que auxilia no controle de recrusos humanos e financeiros em uma empresa ou organização

# Descrição da funcionalidades do software


A aplicação  permite o cadastro, visualização, atualização e remoção dos funcionários da empresa: 

| Cargo       | Nome     | E-mail       | Salário  | Informação Adicional      |
|-------------|----------|--------------|----------|---------------------------|
| Gerente     | [Nome]   | [E-mail]     | [Salário]| Nome da gerência          |
| Secretário  | [Nome]   | [E-mail]     | [Salário]|                           |
| Vendedor    | [Nome]   | [E-mail]     | [Salário]| Quantidade de vendas      |



Todos os funcionários recebem como remuneração o salário base e uma bonificação. A bonificação é aplicada, em cima do salário, da seguinte forma:
| Cargo       | Nome     | E-mail       | Salário  | Bonificação               |
|-------------|----------|--------------|----------|---------------------------|
| Gerente     | [Nome]   | [E-mail]     | [Salário]| 10% do salário + R$ 1.000 |
| Secretário  | [Nome]   | [E-mail]     | [Salário]| 10% do salário            |
| Vendedor    | [Nome]   | [E-mail]     | [Salário]| 10% do salário + 2 x Quantidade de vendas |

A aplicação será utilizada para contabilidade, necessitando realizar operações de pesquisa para os gerentes de forma extremamente rápida. As operações mais importantes são:
- Pesquisa pelo menor salário
- Pesquisa pelo maior salário
- Pesquisa pela mediana dos salários

O usuário do sistema necessita obter o máximo de desempenho nas operações de pesquisa, para isto, utilizei a **ordenação binária** do salários com o metódo **Quick sort**.


Ao iniciar a aplicação, os dados já cadastrados ao longo das últimas execuções são carregados a partir de um arquivo csv.
com isso, o usuário pode baixar a planilha e analisar os dados.


# Tutorial de uso da aplicação

O sistema funciona por linha de comando, pois a aplicação tem foco, apenas, no desenvolvimento back-end.


1- Crie um funcionário, o funcionário pode ser de três tipos:
- Vendedor
- Gerente
- Secretário

[[Clique aqui para ver, no meu canal do Youtube, a execução dessa função]](https://www.youtube.com/watch?v=ycesdyiZGRk)
