#AABCAAADA
def merge_the_tools(string, k):

    #iteraremos: 0, 3, 6
    
    # i = 0
    #[0:3]
    #------
    #i = 3
    #[3:6]
    #------
    #i = 6
    #[6:9]

    for i in range(0, len(string), k):
        unir = ""
        for c in string[i:k+i]:
            if c not in unir:
                unir += c 
        print(unir)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)