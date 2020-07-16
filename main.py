


def elo_ranking(A,B):

    k = 32 # K factor

    #hardcode outcome for now, A wins against B 
    Sa = 1
    Sb = 0

    Ea = 1/(1 + 10**((B - A )/400)) #expected score for A 
    Eb = 1/(1 + 10**((A - B)/400)) #expected score for B

    #recalculate new score for players 
    A = A + (k * (Sa - Ea))
    B = B + (k * (Sb - Eb))

    return A,B



if __name__ == '__main__':
    print("Starting..")
    
    players = []

    for i in range(5):
        
        player1 = input("Player1: ")
        player2 = input("Player2: ")

        if player1 in players:
            print("welcome back ",player1)
        else: 
            players.append(player1)
            print("added ",player1," to the known players list")
        if player2 in players: 
            print("welcome back ",player2)
        else: 
            players.append(player2)
            print("added ",player2," to the known players list")

        


        # a = 900
        # b = 1100

        # for i in range(10):
        #     a,b = elo_ranking(a,b)
        #     print(i,a,b)