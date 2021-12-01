board = list(range(1,10))

def display(board):
    print ("-------------")
    for dis in range(3):
        print ("|", 
               board[0+dis*3], "|", 
               board[1+dis*3], "|", 
               board[2+dis*3], "|")
        print ("-------------")

def choice(element):
    a = False
    while not a:
        player_choice = input("Where will we put "+element)
        try:
            player_choice = int(player_choice)
        except:
            print ("Incorrect move")
            continue
        if player_choice >= 1 and player_choice <= 9:
            if (str(board[player_choice-1]) not in "x0"):
                board[player_choice-1] = element
                a = True
            else:
                print ("Again")
        else:
            print ("Incorrect move")

def check_win(board):
    str_win = ((0,1,2),(3,4,5),(2,5,8),(6,7,8),(0,3,6),(2,4,6),(1,4,7),(0,4,8))
    for element_st in str_win:
        if board[element_st[0]] == board[element_st[1]] == board[element_st[2]]:
            return board[element_st[0]]
    a = False # all def have 'a' for check

def main(board):
    counter = 0
    a = False
    while not a:
        display(board)
        if counter % 2 == 0:
            choice("x")
        else:
            choice("0")
        counter += 1
        if counter > 4:
            check = check_win(board)
            if check:
                print (check, "WIN")
                a = True
                break
        if counter == 9:
            print ("1:1 or DRAW")
            break
    display(board)

main(board)
