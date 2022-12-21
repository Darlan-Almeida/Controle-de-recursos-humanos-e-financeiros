from Funcionario import Funcionario

class Gerente(Funcionario):
  def __init__(self, nome, email , salario, cargo, nome_gerencia):
    super().__init__(nome , email , salario, cargo)
    self.__nome_gerencia = nome_gerencia


  def getNome_gerencia(self):
        return self.__nome_gerencia


  def setNome_gerencia(self , nome_gerencia):
        self.__nome_gerencia = nome_gerencia

  def getSalario(self):
        return super().getSalario() * 1.1 + 1000

  
  def __str__(self):
    return f"{super().__str__()}; Quant. Func. : {self.__qntd_funcionarios}"
    
    
  
