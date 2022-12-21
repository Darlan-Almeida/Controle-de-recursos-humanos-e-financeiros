from Funcionario import Funcionario

class Secretario(Funcionario):
  def __init__(self, nome, email , salario , cargo):
    super().__init__(nome , email , salario , cargo)

  def getSalario(self):
      return super().getSalario() * 1.1

    
