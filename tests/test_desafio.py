import unittest
from unittest.mock import patch

import desafio


class TestLerValor(unittest.TestCase):
    def test_aceita_ponto_decimal(self):
        with patch("builtins.input", return_value="125.50"):
            self.assertEqual(desafio.ler_valor("Valor: "), 125.5)

    def test_aceita_virgula_decimal(self):
        with patch("builtins.input", return_value="125,50"):
            self.assertEqual(desafio.ler_valor("Valor: "), 125.5)

    def test_rejeita_entrada_invalida_e_tenta_novamente(self):
        with patch("builtins.input", side_effect=["abc", "10"]):
            with patch("builtins.print") as print_mock:
                self.assertEqual(desafio.ler_valor("Valor: "), 10.0)
        print_mock.assert_called_once()
        self.assertIn("Entrada inválida", print_mock.call_args.args[0])

    def test_rejeita_infinito_e_tenta_novamente(self):
        with patch("builtins.input", side_effect=["inf", "10"]):
            with patch("builtins.print") as print_mock:
                self.assertEqual(desafio.ler_valor("Valor: "), 10.0)
        print_mock.assert_called_once()
        self.assertIn("finito", print_mock.call_args.args[0])


if __name__ == "__main__":
    unittest.main()
