
##next steps : 
# store data in a csv file for retrieval 
# clean up cmd input flow 



def elo_ranking(A,B,Sa,Sb):

    k = 32 # K factor

    Ea = 1/(1 + 10**((B - A )/400)) #expected score for A 
    Eb = 1/(1 + 10**((A - B)/400)) #expected score for B

    #recalculate new score for players 
    A = A + (k * (Sa - Ea))
    B = B + (k * (Sb - Eb))

    return A,B



if __name__ == '__main__':
    print("Starting..")
    
    players = []

    A = 900
    B = 1100

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

        result_str = input("Enter results: ")
        outcome = result_str.split(",")

        A,B = elo_ranking(A,B,int(outcome[0]),int(outcome[1]))
        print(A,B)

