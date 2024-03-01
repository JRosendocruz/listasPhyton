



lista = ["pantalla", "teclado", "bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcam"]
equipo = ['mouse', 'cd', 'microfono', 'cargador']

# 1
lista_1 = [lista[i] for i in range(3, 8)]
print("1. ", lista_1)

# 2
lista_2 = lista[3:]
print("2. ", lista_2)

# 3
lista_3 = lista[:8]
print("3. ", lista_3)

# 4
lista_4 = [lista[i] for i in [0, 2, 4, 6, 8]]
print("4. ", lista_4)

# 5
for elemento in equipo:
    if elemento in lista:
        indice = lista.index(elemento)
        print(f"Indice {indice}: {elemento}")
    else:
        print(f"{elemento.capitalize()} NO encontrado en lista2")
