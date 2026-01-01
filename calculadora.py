from numbers import Real

def soma(*numeros: Real) -> Real:
    """
    Soma qualquer quantidade de números Reais.

    Aceita qualquer quantidade de argumentos numéricos (int ou float) e retorna a soma total. Caso não haja números, retorna 0.

    Parâmetros
    --------------
    *numeros: Real
        Um ou mais números a serem somados.

    Retorno
    --------------
    Real
        A soma de todos os valores informados. Retorna 0 caso não haja um 

    Exceções
    --------------
    TypeError
        Lançada caso um dos argumentos não seja um número Real.
    """
    if not numeros:
        return 0
    for n in numeros:
        if not isinstance(n, Real):
            raise TypeError(f'Valor inválido: {n} não é um número')
    return sum(numeros)

def subtrair(*numeros: Real) -> Real:
    """
    Realiza a subtração sequencial de uma quantidade variável de números reais.

    Caso nenhum valor seja informado, a função retorna 0.

    Parameters
    ----------
    *numeros : Real
        Um ou mais números reais (int ou float) a serem subtraídos.

    Returns
    -------
    Real
        Resultado da subtração sequencial dos valores informados.
        Retorna 0 se nenhum valor for fornecido.

    Raises
    ------
    TypeError
        Se algum dos argumentos fornecidos não for um número real.
    """
    if not numeros:
        return 0
    for n in numeros:
        if not isinstance(n, Real):
            raise TypeError(f'Valor inválido: {n} não é um número')

    resultado = numeros[0]
    for n in numeros[1:]:
        resultado -= n

    return resultado

def multiplicar(*numeros: Real) -> Real:
    """
    Realiza a multiplicação de uma quantidade variável de números reais.

    Caso nenhum valor seja informado, a função retorna 0.

    Parameters
    ----------
    *numeros : Real
        Números reais (int ou float) a serem multiplicados.

    Returns
    -------
    Real
        Resultado da multiplicação dos valores informados.

    Raises
    ------
    TypeError
        Se algum dos argumentos não for um número real.
    """
    if not numeros:
        return 0
    for n in numeros:
        if not isinstance(n, Real):
            raise TypeError(f'Valor inválido: {n} não é um número')

    resultado = 1
    for n in numeros:
        resultado *= n

    return resultado

def dividir(a, b):
    """
    Realiza a divisão entre dois números reais.

    A função divide o primeiro valor pelo segundo (a / b).

    Parameters
    ----------
    a : Real
        Dividendo da operação.
    b : Real
        Divisor da operação.

    Returns
    -------
    Real
        Resultado da divisão entre os valores informados.

    Raises
    ------
    TypeError
        Se algum dos argumentos não for um número real.
    ZeroDivisionError
        Se o divisor for zero.
    """
    if not isinstance(a, Real):
        raise TypeError(f'Valor inválido: {a} não é um número')

    if not isinstance(b, Real):
        raise TypeError(f'Valor inválido: {b} não é um número')

    if b == 0:
        raise ZeroDivisionError('Divisão por zero não é permitida')

    return a / b

def is_Par(numero):
    """
    Verifica se um número real é par.

    A função valida se o valor fornecido é um número real (int ou float).
    Caso não seja, lança uma exceção do tipo TypeError.

    Parâmetros:
        numero (Real): Número a ser verificado.

    Retorna:
        bool: True se o número for par, False caso contrário.

    Exceções:
        TypeError: Se o valor fornecido não for um número real.
    """
    if not isinstance(numero, Real):
        raise TypeError(f'Valor inválido: {numero} não é um número')
    return numero % 2 == 0

def validar_numero_positivo(numero: Real) -> bool:
    """
    Verifica se um número é positivo.

    Parâmetros:
        numero (Real): Número a ser validado.

    Retorna:
        bool: True se o número for positivo.

    Exceções:
        TypeError: Se o valor informado não for numérico.
        ValueError: Se o número for zero.
    """
    if not isinstance(numero, Real):
        raise TypeError("O valor informado não é um número")

    if numero == 0:
        raise ValueError("O número não pode ser zero")

    return numero > 0
