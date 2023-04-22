def string_inverter(sentence: str) -> str:

    # Lista auxiliar para manipular strings.
    aux_list = list(sentence)

    # Reordenação  .
    for c in range(0, int(len(aux_list) / 2)):
        aux_list[c], aux_list[len(aux_list) - c - 1] = aux_list[len(aux_list) - c - 1], aux_list[c]

    sentence = ""

    # Sentença recebe a frase reordenada.
    for c in aux_list:
        sentence += c

    return sentence


print(string_inverter('Target Sistemas'))