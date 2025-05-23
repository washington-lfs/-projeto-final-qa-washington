# Calculadora Simples
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida!")
    return a / b

# Testes Unitários (usando unittest)
import unittest

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)          # 2 + 3 = 5
        self.assertEqual(soma(-1, 1), 0)         # -1 + 1 = 0

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)     # 5 - 3 = 2
        self.assertEqual(subtracao(10, -2), 12)  # 10 - (-2) = 12

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 4), 12)  # 3 * 4 = 12
        self.assertEqual(multiplicacao(-2, 5), -10) # -2 * 5 = -10

    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5)      # 10 / 2 = 5
        self.assertAlmostEqual(divisao(1, 3), 0.333, places=3)  # Arredondamento
        with self.assertRaises(ValueError):      # Teste de divisão por zero
            divisao(10, 0)

# Executar os testes no Google Colab
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
