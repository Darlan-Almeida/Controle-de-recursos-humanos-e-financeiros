from Funcionario import Funcionario

class Vendedor(Funcionario):
  def __init__(self, nome, email, salario, cargo , quantidade_vendas):
    super().__init__(nome, email, salario , cargo)
    self.__quantidade_vendas = quantidade_vendas


  def getquantidade_vendas(self):
        return self.__quantidade_vendas


  def setquantidade_vendas(self, quantidade_vendas):
        self.__quantidade_vendas = quantidade_vendas

  def getBonificacao(self):
        return super().getSalario() * 0.1 + (2 * self.__quantidade_vendas)
  
  def getSalario(self):
      return super().getSalario() + self.getBonificacao()

  def __str__(self):
    return f"{super().__str__()}; Quantidade de vendas : {self.__quantidade_vendas}"