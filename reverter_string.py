def reverter_string(s):
    resultado = ""
    for i in range(len(s)-1, -1, -1):
        resultado += s[i]
    return resultado

entrada = input("Digite uma string: ")

string_invertida = reverter_string(entrada)
print("String invertida:", string_invertida)
