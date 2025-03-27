import random

playerPoints = 0
computerPoints = 0

print("Spiel geht bis Drei Punkte")

while playerPoints < 3 and computerPoints < 3:
        
    spots = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9"
    }

    playerWon = False


    def print_board():
        board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
                f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
                f"|{spots[7]}|{spots[8]}|{spots[9]}|")
        print(board)


    def check_winner():
        global playerWon
        global threePointsReached
        if (spots[1] == spots[2] == spots[3] or
            spots[4] == spots[5] == spots[6] or
                spots[7] == spots[8] == spots[9]):
            playerWon = True
            

        elif (spots[1] == spots[4] == spots[7] or
            spots[2] == spots[5] == spots[8] or
            spots[3] == spots[6] == spots[9]):
            playerWon = True


        elif (spots[1] == spots[5] == spots[9] or
            spots[3] == spots[5] == spots[7]):
            playerWon = True

    def check_tie():
        feldbesetzt = 0
        for spot in spots:
            if spots[spot] == "x" or spots[spot] == "*":
                feldbesetzt += 1 
        if feldbesetzt == 9:
            return True
        return False


    print_board()

    while playerWon == False:

        playerPlayed = False

        while playerPlayed == False:

            playerInput = input("wähle Feld -> ")

            if (playerInput.isdigit() and int(playerInput) <= 9 and int(playerInput) >= 1):
                if (spots[int(playerInput)] == "x" or spots[int(playerInput)] == "*"):
                    print("Feld bereits besetzt")
                    continue
                else:
                    break
            else:
                print("ungültige Eingabe")
                continue

        match playerInput:
            case "1":
                spots[1] = "x"
            case "2":
                spots[2] = "x"
            case "3":
                spots[3] = "x"
            case "4":
                spots[4] = "x"
            case "5":
                spots[5] = "x"
            case "6":
                spots[6] = "x"
            case "7":
                spots[7] = "x"
            case "8":
                spots[8] = "x"
            case "9":
                spots[9] = "x"

        print("Dein Spielzug: ")
        print_board()
        check_winner()
        check_tie()
        if check_tie():
            print("Unentschieden")
            break
        if (playerWon == True):
            playerPoints += 1
            print("Spieler hat gewonnen!")
            print("Spieler hat " + str(playerPoints) + " Punkte")
            break

        botPlayed = False
        while (botPlayed == False):
            randomNum = random.randint(1, 9)

            if (spots[randomNum] == "x" or spots[randomNum] == "*"):
                continue
            else:
                spots[randomNum] = "*"
                botPlayed = True
                print("Computer Spielzug: ")
                break

        print_board()
        check_winner()
        check_tie()
        
        if (playerWon == True):
            computerPoints += 1
            print("Computer hat gewonnen!")
            print("Computer hat " + str(computerPoints) + " Punkte")
            break
        if check_tie():
            print("Unentschieden")
            break
            
