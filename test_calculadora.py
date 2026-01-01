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

    def test_soma_com_valor_invalido(self):
        with raises(TypeError):
            soma(1, "2", 3)

    def test_soma_com_none(self):
        with raises(TypeError):
            soma(1, None)

    def test_soma_sem_argumentos(self):
        assert soma() == 0
class TestSubtracao:
    def test_subtracao_dois_numeros(self):
        assert subtrair(10, 4) == 6


    def test_subtracao_resultado_negativo(self):
        assert subtrair(3, 5) == -2


    def test_subtracao_valores_iguais(self):
        assert subtrair(7, 7) == 0

    def test_subtracao_com_valor_invalido(self):
        with raises(TypeError):
            subtrair(10, "5")

    def test_subtracao_com_none(self):
        with raises(TypeError):
            subtrair(None, 5)

    def test_subtracao_sem_argumentos(self):
        assert subtrair() == 0

class TestMultiplicacao:
    def test_multiplicacao_dois_positivos(self):
        assert multiplicar(3, 4) == 12


    def test_multiplicacao_por_zero(self):
        assert multiplicar(5, 0) == 0


    def test_multiplicacao_com_negativos(self):
        assert multiplicar(-2, 4) == -8

    def test_multiplicacao_com_valor_invalido(self):
        with raises(TypeError):
            multiplicar(2, "3")

    def test_multiplicacao_com_none(self):
        with raises(TypeError):
            multiplicar(2, None)

    def test_multiplicacao_sem_argumentos(self):
        assert multiplicar() == 0

class TestDivisao:
    def test_divisao_correta(self):
        assert dividir(10, 2) == 5


    def test_divisao_por_zero(self):
        with raises(ZeroDivisionError):
            dividir(10, 0)

    def test_divisao_com_decimais(self):
        assert dividir(5, 2) == 2.5

    def test_divisao_dividendo_invalido(self):
        with raises(TypeError):
            dividir("10", 2)

    def test_divisao_divisor_invalido(self):
        with raises(TypeError):
            dividir(10, "2")

    def test_divisao_ambos_invalidos(self):
        with raises(TypeError):
            dividir("10", "2")

class TestIsPar:
    def test_numero_par(self):
        assert is_Par(4) is True

    def test_numero_impar(self):
        assert is_Par(5) is False

    def test_zero_e_par(self):
        assert is_Par(0) is True

    def test_is_par_float_impar(self):
        assert is_Par(2.5) is False

    def test_is_par_com_string(self):
        with raises(TypeError):
            is_Par("4")

    def test_is_par_com_none(self):
        with raises(TypeError):
            is_Par(None)

class TestIsPositive:
    def test_numero_positivo(self):
        assert validar_numero_positivo(5) is True


    def test_numero_negativo(self):
        assert validar_numero_positivo(-3) is False


    def test_zero_lanca_excecao(self):
        with raises(ValueError):
            validar_numero_positivo(0)

    def test_valor_invalido_string(self):
        with raises(TypeError):
            validar_numero_positivo("5")

    def test_valor_none(self):
        with raises(TypeError):
            validar_numero_positivo(None)

    def test_float_positivo(self):
        assert validar_numero_positivo(3.5) is True

    def test_float_negativo(self):
        assert validar_numero_positivo(-1.2) is False