from oo.carro.direcao import Direcao


def test_valor_inicial_de_direcao_eh_norte():
    # Dado uma direção recém instanciada
    direcao = Direcao()

    # Seu valor inicial deve ser 'Norte'
    assert direcao.valor == 'Norte'
