def inverter_string(string):
    # Inicializamos uma string vazia para armazenar a string invertida
    string_invertida = ""
    # Iteramos de trás para frente na string original
    for i in range(len(string) - 1, -1, -1):
        # Concatenamos cada caractere na posição atual à string invertida
        string_invertida += string[i]
    # Retornamos a string invertida
    return string_invertida

# Exemplo de uso: inverter uma string fornecida pelo usuário
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
