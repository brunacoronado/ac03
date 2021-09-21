import abc
from unittest import TestCase,main


class Calculadora(object):
    def calcular(self,valor1,valor2,operador):
        operacao = OperacaoFabrica().criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(valor1,valor2)
            return resultado

class OperacaoFabrica(object):
    def criar(self, operador):
        if (operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self,valor1,valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado
class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado
class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado
class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado    


class Testes(TestCase):
    def test_soma(self):
        calculo_soma = Calculadora()
        result = calculo_soma.calcular(2,3,'soma')
        self.assertEqual(result,5)
        
    def test_multiplicacao(self):
        calculo_multiplicacao = Calculadora()
        result = calculo_multiplicacao.calcular(2,5,'multiplicacao')
        self.assertEqual(result,10)

    def test_divisao(self):
        calculo_divisao = Calculadora()
        result = calculo_divisao.calcular(2,4,'divisao')
        self.assertEqual(result,0.5)

    def test_subtracao(self):
        calculo_subtracao = Calculadora()
        result = calculo_subtracao.calcular(10,50,'subtracao')
        self.assertEqual(result, -40)

front = """"CALCULADORA
Operações:\n
    Soma            +
    Subtracao       -
    Multiplicacao   x
    Divisao         /\n"""


def codigo():
    operacoes=['soma','subtracao','multiplicacao','divisao']
    operacao=input("Informe a operacao:\n").lower()
    if operacao not in operacoes:
        print("Operação não reconhecida")
        codigo()
    valor1=float(input("Digite o valor 1:\n"))
    valor2=float(input("Digite o valor 2:\n"))
    resultado = Calculadora().calcular(valor1,valor2,operacao)
    print ("Resultado = {0:g}".format(float(resultado)))


print(front)
codigo()
main()