while True:
    try:
        palavra = input()

        if not palavra:
            break
        
        print(len(palavra))
        
    except EOFError:
        break


