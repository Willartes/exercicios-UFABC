while True:
    try:
        palavra = input()

        if palavra == palavra[::-1]:
            print("sim")
        else:
            print("nao")
    
    except EOFError:
        break
    