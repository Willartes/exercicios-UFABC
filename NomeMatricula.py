while True:
    try:
        nomicula = input()

        nome = ""
        matricula = ""

        for char in nomicula:
            if char.isalpha():
                nome += char
            elif char.isdigit():
                matricula += char

        print(f"{nome} {matricula}")

    except EOFError:
        break
