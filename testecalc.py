import unittest
from calc import calcular

class TestCalculadora(unittest.TestCase):
    # --- testes ---
    def test_soma_inteiros_basica(self):
        self.assertEqual(calcular(5, 3, '+'), 8)

    def test_soma_com_numero_negativo(self):
        self.assertEqual(calcular(-7, 2, '+'), -5)

    def test_soma_com_strings_numericas(self):
        self.assertAlmostEqual(calcular('2.5', '3.5', '+'), 6.0)

    # --- subtração ---
    def test_subtrai_valores_maiores_menos_menores(self):
        self.assertEqual(calcular(20, 5, '-'), 15)

    def test_subtracao_com_resultado_negativo(self):
        self.assertEqual(calcular(2, 9, '-'), -7)

    def test_subtracao_floats(self):
        self.assertAlmostEqual(calcular(5.5, 2.2, '-'), 3.3, places=7)

    # --- multiplicação ---
    def test_multiplica_inteiros(self):
        self.assertEqual(calcular(4, 6, '*'), 24)

    def test_multiplica_por_zero(self):
        self.assertEqual(calcular(12345, 0, '*'), 0)

    def test_multiplicacao_float_e_string(self):
        self.assertAlmostEqual(calcular('1.5', 2, '*'), 3.0)

    # --- divisão ---
    def test_divisao_exata(self):
        self.assertAlmostEqual(calcular(12, 3, '/'), 4.0)

    def test_divisao_gera_decimal(self):
        self.assertAlmostEqual(calcular(7, 2, '/'), 3.5)

    def test_divisao_com_numerador_negativo(self):
        self.assertAlmostEqual(calcular(-9, 3, '/'), -3.0)

    def test_divisao_por_zero_deve_retornar_none(self):
        self.assertIsNone(calcular(10, 0, '/'))

    # --- potenciação ---
    def test_potencia_inteira(self):
        self.assertEqual(calcular(3, 4, '^'), 81)

    def test_potencia_expoente_zero(self):
        self.assertEqual(calcular(42, 0, '^'), 1)

    def test_potencia_base_negativa_expoente_par(self):
        self.assertEqual(calcular(-3, 2, '^'), 9)

    def test_potencia_base_negativa_expoente_impar(self):
        self.assertEqual(calcular(-3, 3, '^'), -27)

    def test_potencia_com_float(self):
        self.assertAlmostEqual(calcular(2.5, 2, '^'), 6.25)

    # --- entradas inválidas / operações desconhecidas ---
    def test_operador_desconhecido_retorna_none(self):
        self.assertIsNone(calcular(10, 5, '%'))

    def test_operandos_nao_numericos_retorna_none_um(self):
        self.assertIsNone(calcular('x', 5, '+'))

    def test_operandos_nao_numericos_retorna_none_outro(self):
        self.assertIsNone(calcular(5, None, '*'))

    def test_ambos_operandos_invalidos(self):
        self.assertIsNone(calcular('a', 'b', '-'))

if __name__ == '__main__':
    unittest.main(verbosity=2)