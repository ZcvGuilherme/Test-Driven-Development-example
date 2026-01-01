from calculadora import *
from pytest import raises
class TestSoma:
    def test_soma_positivos(self):
        assert soma(3, 4) == 7

    def test_soma_com_zero(self):
        assert soma(0,0) == 0

    def test_soma_negativos(self):
        assert soma(-3, -5) == -8

    def test_soma_positivo_negativo(self):
        assert soma(3,-5) == -2

class TestSubtracao:
    def test_subtracao_dois_numeros():
        assert subtrair(10, 4) == 6


    def test_subtracao_resultado_negativo():
        assert subtrair(3, 5) == -2


    def test_subtracao_valores_iguais():
        assert subtrair(7, 7) == 0

class TestMultiplicacao:
    def test_multiplicacao_dois_positivos():
        assert multiplicar(3, 4) == 12


    def test_multiplicacao_por_zero():
        assert multiplicar(5, 0) == 0


    def test_multiplicacao_com_negativos():
        assert multiplicar(-2, 4) == -8

class TestDivisao:
    def test_divisao_correta():
        assert dividir(10, 2) == 5


    def test_divisao_por_zero():
        with raises(ZeroDivisionError):
            dividir(10, 0)


    def test_divisao_com_decimais():
        assert dividir(5, 2) == 2.5

class TestIsPar:
    def test_numero_par():
        assert isPar(4) is True


    def test_numero_impar():
        assert isPar(5) is False


    def test_zero_e_par():
        assert isPar(0) is True

class TestIsPositive:
    def test_numero_positivo():
        assert validarNumeroPositivo(5) is True


    def test_numero_negativo():
        assert validarNumeroPositivo(-3) is False


    def test_zero_lanca_excecao():
        with raises(ValueError):
            validarNumeroPositivo(0)
