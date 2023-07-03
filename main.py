from Funcionario import Funcionario
from Vendedor import Vendedor
from Secretario import Secretario
from Gerente import Gerente

#import os


#Ordena a lista
def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a


def particao(a, ini, fim):
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i].getSalario() > pivo.getSalario():
            fim += 1
        else:
            fim += 1
            ini += 1
            a[i], a[ini - 1] = a[ini - 1], a[i]
    return ini - 1


def menu():
    #os.system("clear")
    print("-" * 60)
    print("1- Cadastrar funcionário")  #def criar_funcionario():
    print("2- Salvar funcionarios")  #def salvar_dados(lista):
    print("3- Remover Funcionários"
          )  #def remover_funcionarios(lista_funcionarios, numero):
    print("4- Atualizar cadastro do funcionário")
    print("5- Buscar funcionário pelo menor sálario")
    print("6- Buscar funcionário pelo maior sálario")
    print("7- Buscar funcionário pelo sálario médio")
    print("8- Ordenar lista")
    print("-" * 60)

def criar_funcionario():
    print("informe o cargo")
    print("1- Vendedor")
    print("2- Secretário")
    print("3- Gerente")
    cargo = int(input("digite aqui: "))

    if(cargo == 1):
        nome = input("Informe o nome:  ")
        email = input("Informe o email:  ")
        salario = float(input("Informe o salário:  "))
        cargo = "Vendedor"
        quantidade_vendas = int(input("Informe a quantidade de Vendas:  "))
        funcionario = Vendedor(nome, email, salario, cargo , quantidade_vendas)
        return funcionario
    if(cargo == 2):
        nome = input("Informe o nome:  ")
        email = input("Informe o email:  ")
        salario = float(input("Informe o salário:  "))
        cargo = "Secretário"
        funcionario = Secretario(nome, email, salario, cargo)
        return funcionario
    if(cargo == 3):
        nome = input("Informe o nome:  ")
        email = input("Informe o email:  ")
        salario = float(input("Informe o salário:  "))
        cargo = "Gerente"
        nome_gerencia = input("Informe o nome da gerência:  ")
        funcionario = Gerente(nome, email, salario, cargo , nome_gerencia)
        return funcionario



def salvar_dados(lista):
    print(lista)
    with open("funcionario.csv", "w") as arquivo:
        for func in lista:
            arquivo.write(
                f"{func.getNome()}; {func.getEmail()}; {func.getSalario()}; {func.getCargo()} \n"
            )


def carregar_dados():
    funcionarios = []
    with open("funcionario.csv", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            dados = linha.split(";")
            func = Funcionario(dados[0], dados[1], float(dados[2]), dados[3])
            funcionarios.append(func)

    return funcionarios


def remover_funcionarios(lista_funcionarios):
    nome = input("Qual funcionario deseja remover: ")
    pos = 0
    for func in lista_funcionarios:
        if nome == func.getNome():
            lista_funcionarios.pop(pos)

        pos += 1


def atualizar_cadastro(lista_funcionarios):
    pos = int(input("Qual posição deseja atualizar no cadastro: "))
    print(" 1- email \n 2- salário \n 3- cargo")

    informacao = int(input("Qual informação voce deseja alterar: "))
    pos = 0

    if informacao == 1:
        lista_funcionarios[pos].setEmail(input("Digite o novo email: "))

    if informacao == 2:
        lista_funcionarios[pos].setSalario(
            float(input("Digite o novo salario: ")))

    if informacao == 3:
        lista_funcionarios[pos].setCargo(input("Digite o novo cargo: "))
    else:
        print("Digite uma das opções de atualização disponível")
    pos = 0


def menor_salario(lista_funcionarios):
    print(lista_funcionarios[0])


def maior_salario(lista_funcionarios):
    print(lista_funcionarios[-1])


def salario_mediano(lista_funcionarios):
    tamanho = len(lista_funcionarios)
    mediana_salarios = tamanho // 2
    print(lista_funcionarios[mediana_salarios])


def print_funcionarios(funcionarios):
    for f in funcionarios:
        print(
            f"{f.getNome()}; {f.getEmail()}; {f.getSalario()}; {f.getCargo()} "
        )


def main():
    opcao = 0
    funcionarios = carregar_dados()
    quick_sort(funcionarios)
    #print(quick_sort(funcionarios))

    while opcao != 7:
        menu()
        print("Dados dos funcionários:")
        print_funcionarios(funcionarios)
        opcao = int(input("Sua opção: "))
        if opcao == 1:
            f = criar_funcionario()
            funcionarios.append(f)

        elif opcao == 2:
            salvar_dados(funcionarios)

        elif opcao == 3:
            remover_funcionarios(funcionarios)

        elif opcao == 4:
            atualizar_cadastro(funcionarios)

        elif opcao == 5:
            menor_salario(funcionarios)

        elif opcao == 6:
            maior_salario(funcionarios)

        elif opcao == 7:
            salario_mediano(funcionarios)

        elif opcao == 8:
            quick_sort(funcionarios)


if __name__ == '__main__':
    main()
