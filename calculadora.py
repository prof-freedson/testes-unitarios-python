# 1) Criar a classe 'Calculadora'
class Calculadora:
    
    # 2) Criando o método 'soma'
    def soma(a, b):
        return a + b
    
    # 3) Criando o método 'sub'
    def sub(a, b):
        return a - b
    
    # 4) Criando o método 'mult'
    def mult(a, b):
        return a * b
    
    # 4) Criando o método 'div'
    def div(a, b):
        if b == 0:
            return ZeroDivisionError
        else:
            return a / b