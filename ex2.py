def fibonacciSequence(givenNumber: int) -> str:

    # Valor anterior ao atual
    previousNumber = 0
    # Valor atual
    result = 0
    # Variável contadora
    i = 1

    while result < givenNumber:
        # Caso a condição não passe pelo while então o resultado é zero, se passar uma vez
        # então o resultado é um. Para os demais casos o resultado incrementa em seu valor o valor
        # anterior e o valor anterior recebe a subtração entre o novo resultado e o valor anterior.

        if i == 1:
            result = 1
            i += 1
        else:
            result += previousNumber
            previousNumber = result - previousNumber

    # Valores de retorno
    # Caso o resultado da sequência seja igual ao valor dado no input então o valor pertence a sequência,
    # caso contrario o valor não pertence a sequência fibonacci.
    if result == givenNumber:
        return f'O número {givenNumber} pertence à sequência.'

    return f'O número {givenNumber} não pertence à sequência.'


print(fibonacciSequence(21))