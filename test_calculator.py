import unittest

from calculator import dividir, multiplicar, somar, subtrair


class TestSomar(unittest.TestCase):
    def test_soma_dois_numeros_inteiros(self):
        soma = somar(2, 3)
        self.assertEqual(soma, 5)

    def test_soma_numero_com_zero(self):
        self.assertEqual(somar(2, 0), 2)


class TestSubtrair(unittest.TestCase):
    def test_subtrair_dois_numeros_inteiros(self):
        subtracao = subtrair(5, 4)
        self.assertEqual(subtracao, 1)

    def test_subtrai_numero_com_zero(self):
        self.assertEqual(subtrair(2, 0), 2)


class TestMultiplicar(unittest.TestCase):
    def test_multiplicar_dois_numeros_inteiros(self):
        multiplicacao = multiplicar(3, 6)
        self.assertEqual(multiplicacao, 18)

    def test_multiplicar_numero_por_zero(self):
        self.assertEqual(multiplicar(3, 0), 0)


class TestDividir(unittest.TestCase):
    def test_dividir_dois_numeros_inteiros(self):
        divisao = dividir(8, 2)
        self.assertEqual(divisao, 4)

    def test_dividir_numero_por_zero(self):
        self.assertEqual(dividir(8, 0), "Infinito.")


unittest.main()
