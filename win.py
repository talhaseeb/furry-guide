import itertools


def win(currrent_game):

    def all_same(l):
        if l.count(l[0])== len(l) and l[0]!= 0:
            return True
        else:
            return False

    #horizontal
    for row in game:
        print(row)
        if all_same(row):
                    # print("in if")
            print(f"player {row} is winner horizontally !")
            return True            # print("winner")

    #diagnol
    diag=[]
    for col,row in enumerate(reversed(range(len(game)))):
        diag.append(game[row][col])
    if all_same(diag):
        print(f"player {diag} is winner diaganolly (/) !")
        return True
    diag=[]
    for idx in range(len(game)):
        diag.append(game[idx][idx])
    if all_same(diag) :
        print(f"player {diag} is winner diaganolly (\\) !")
        return True
    #verical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"player {row} is winner vertically " )
            return True

    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("this placed is occupied")
            return game_map , False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)

        return game_map , True
    except IndexError as e:
        print("make sure to enter input row/column 0,1,2 ", e)
        return game_map , False
    except Exception as e:
        print("Something went wrong !!", e)
        return game_map , False

play = True
players = [1,2]
while play:
    game_size = int(input("what size of tic tac toe you want? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won= False
    game , _ = game_board(game,just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player= next(player_choice)
        print(f"Current player : {current_player}")
        played = False
        while not played:
            column_choice = int(input("select column of your choice (0,1,2) :  "))
            row_choice = int(input("select row of your choice (0,1,2) :  "))
            game , played= game_board(game,current_player,row_choice,column_choice)

        if win(game):
            game_won = True
            again = input("do you want to play again (y/n) ?")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Bye")
                play = False
            else:
                print("enter a valid input")
                play = False
