


def elo_ranking(A,B):

    k = 32 # K factor

    #hardcode outcome for now, A wins against B 
    Sa = 1
    Sb = 0

    Ea = 1/(1 + 10**((B - A )/400)) #expected score for A 
    Eb = 1/(1 + 10**((A - B)/400)) #expected score for B

    A = A + k * (Sa - Ea)
    B = B + k * (Sb - Eb)
    return A,B



if __name__ == '__main__':
    print("Starting..")
    a,b = elo_ranking(90,110)
    print(a,b)