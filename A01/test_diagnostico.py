"""A01: testes da função itens_disponiveis. Escreva os casos que faltam."""
import unittest

from diagnostico import itens_disponiveis

DADOS = [
    {"nome": "Notebook", "quantidade": 3},
    {"nome": "Projetor", "quantidade": 0},
    {"nome": "Cabo", "quantidade": 5},
]


class ItensDisponiveis(unittest.TestCase):
    def test_limite_um_devolve_os_que_tem_estoque(self):
        self.assertEqual(itens_disponiveis(DADOS, 1), ["Notebook", "Cabo"])

    # TODO: lista vazia.
    # TODO: quantidade exatamente igual ao limite (fronteira).
    # TODO: a função não pode alterar a lista recebida.


if __name__ == "__main__":
    unittest.main()
