while True:
    try:
        primaira_palavra, segunda_palavra = map(str, input().split())

        if not (primaira_palavra and segunda_palavra):
            break
        
        print(f"{primaira_palavra}{segunda_palavra}")
        
    except EOFError:
        break


