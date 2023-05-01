text = input ("Digite o seu texto: ")

for i, c in enumerate(text):
    if c == "a" or c == "e":
        print (f"Vogal encontrada: {c}, Na posição: {i}")
    else:
        continue

    