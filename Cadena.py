cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc placerat egestas egestas.
Morbi malesuada eros sed odio mattis luctus ut quis libero. Nunc tincidunt sapien at congue sodales.
Praesent a maximus libero. Proin sed placerat elit, 
condimentum vulputate nunc. Quisque et sodales nisi. 
Nulla elementum ex in odio ultrices malesuada. Praesent dictum ante sit amet enim semper scelerisque.
Pellentesque eros massa, dapibus at mi eget, ullamcorper aliquet leo.
Nulla id lacus id dui convallis dapibus. 
Aliquam vitae mattis leo. Vivamus elementum, metus elementum eleifend vehicula, 
magna enim consequat ante, imperdiet blandit elit diam sed urna. 
Vivamus finibus maximus elit ut laoreet. Aliquam fringilla rhoncus dapibus. 
Donec in consequat lorem. Sed vestibulum facilisis egestas.

Proin in convallis augue. Vestibulum elementum nibh et urna pellentesque, 
quis blandit tortor tempor. Vivamus tristique condimentum rutrum. 
Aliquam at odio facilisis, convallis lorem sit amet, posuere odio. 
Integer aliquet in felis tristique scelerisque. Duis finibus at velit in eleifend. 
Integer sed ligula consectetur, sollicitudin nisl at, tempor purus. 
Curabitur consequat ante nec lorem interdum feugiat. Etiam sagittis ornare ex, 
vitae tempus purus commodo eget. Curabitur tempor dui nunc, at ultrices ligula condimentum eget. 
Mauris ac ante viverra, sodales arcu eget, mattis mi. Pellentesque condimentum hendrerit sem. 
Sed tincidunt bibendum augue a dapibus. Nam quis eleifend magna.
"""



caracteres = ['a', 'e','i', 'o','u', ' ', ',']

def contar_caracteres(cadena, caracter):
    return cadena.count(caracter)

total_caracteres = len(cadenaLarga)
total_letras = sum(contar_caracteres(cadenaLarga, letra) for letra in 'abcdefghijklmnopqrstuvwxyz')
total_vocales = sum(contar_caracteres(cadenaLarga, vocal) for vocal in 'aeiou')
total_vocales_a = contar_caracteres(cadenaLarga, 'a')
total_vocales_e = contar_caracteres(cadenaLarga, 'e')
total_vocales_i = contar_caracteres(cadenaLarga, 'i')
total_vocales_o = contar_caracteres(cadenaLarga, 'o')
total_vocales_u = contar_caracteres(cadenaLarga, 'u')
total_espacios = contar_caracteres(cadenaLarga, ' ')
total_comas = contar_caracteres(cadenaLarga, ',')

palabras = cadenaLarga.split()
total_palabras = len(palabras)

print("Total de caracteres:", total_caracteres)
print("Total de letras (incluyendo vocales):", total_letras)
print("Total de vocales:", total_vocales)
print("Total de vocales a:", total_vocales_a)
print("Total de vocales e:", total_vocales_e)
print("Total de vocales i:", total_vocales_i)
print("Total de vocales o:", total_vocales_o)
print("Total de vocales u:", total_vocales_u)
print("Total de espacios:", total_espacios)
print("Total de comas:", total_comas)
print("Total de palabras:", total_palabras)
