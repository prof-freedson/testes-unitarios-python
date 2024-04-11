# 1) Importar o pacote de
# testes unitários
import unittest

# 2) Impotando a classe 'Calculadora'
from calculadora import Calculadora

# 3) Criando a classe de testes unitários
class CalculadoraTest(unittest.TestCase):
    
    # 4) Criando o metódo de teste
    # do método "soma"
    def teste_soma_dois_numeros(self):
        # 5) Criando o objeto que herdará
        # a classe 'Calculadora'
        calc = Calculadora
        
        # 6) Testar resultados
        # esperados e obtidos
        self.assertEqual(calc.soma(8,4), 12)
    
    def teste_subtrai_dois_numeros(self):
        calc = Calculadora
        self.assertEqual(calc.sub(8,4), 4)
        
    def teste_multiplica_dois_numeros(self):
        calc = Calculadora
        self.assertEqual(calc.mult(8,4), 32)
        
    def teste_divide_dois_numeros(self):
        calc = Calculadora
        self.assertEqual(calc.div(8,4), 2)        
    
    # Extra: tratando uma divisão por zero
    def teste_divisao_por_zero(self):
        calc = Calculadora
        self.assertEqual(calc.div(8,0), ZeroDivisionError)

# Executando os testes unitários
if __name__ == '__main__':
    unittest.main()