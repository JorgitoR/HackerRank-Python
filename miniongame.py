def miniongame(string):
    Vocal = ['A', 'E', 'I', 'O', 'U']

    vocales = 0
    consonantes = 0

    for i in range(len(string)):
        
        if string[i] in Vocal:
            vocales += len(string) - i 
        else:
            consonantes += len(string) - i

    if vocales > consonantes:
        print("Kevin" + " " + "%d" %vocales)
    
    elif consonantes > vocales:
        print("Stuart" + " " + "%d" %consonantes)

    else:
        print("Draw")



if __name__ == '__main__':
    cadena = input()
    miniongame(cadena)