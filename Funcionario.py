class Funcionario:

    __slots__ = ["__nome", "__email", "__salario", "__cargo"]
    __quantidade = 0
    def __init__(self, nome, email, salario, cargo):
        self.__nome = nome
        self.__email = email
        self.__salario = salario
        self.__cargo = cargo
        
        

  
    def getNome(self):
        return self.__nome


    def setNome(self, nome):
        self.__nome = nome

    def getEmail(self):
        return self.__email


    def setEmail(self, email):
        self.__email = email
          
    def getSalario(self):
        return self.__salario


    def setSalario(self, salario):
        self.__salario = salario

    def getCargo(self):
        return self.__cargo


    def setCargo(self, cargo):
        self.__cargo = cargo


    def __str__(self):
        return  "Nome: " + str(self.__nome) + " E-mail: " + str(self.__email) + " Salário: " + str(self.__salario)

