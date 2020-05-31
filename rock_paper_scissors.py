'''Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner,
and ask if the players want to start a new game)

https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Usage:
    python rock_paper_scissors.py
'''

import sys

def get_play():
    '''Get player selection of rock/paper/scissors
        Args:
            None

        Returns:
            player selection as string (rock/paper/scissors)

    '''
    while True:
        play = input('Available options:\n'
                     '1 - rock\n'
                     '2 - paper\n'
                     '3 - scissors\n'
                     'Enter your selection: ')
        # print('\n==> DEBUG: selection is ', play, "returns a variable of type", type(play))
        if play == '1' or play.lower() == 'rock':
            return 'rock'
        if play == '2' or play.lower() == 'paper':
            return 'paper'
        if play == '3' or play.lower() == 'scissors':
            return 'scissors'
        print(f'{play} is not a valid selection - TRY AGAIN')


def get_winner(player1,player2):
    '''Get winner of a rock, paper, scissors game
        Args:
            player1 & player2 selections (already verified)

        Returns:
            winner player or TIE
    '''
    if player1 == player2:
        return 'TIE'
    if player1 == 'rock' and player2 == 'scissors':
        return 'PLAYER 1'
    if player1 == 'scissors' and player2 == 'paper':
        return 'PLAYER 1'
    if player1 == 'paper' and player2 == 'rock':
        return 'PLAYER 1'
    return 'PLAYER 2'


if __name__ == '__main__':
    while True:
        control = input('\nDo you want to play rock/paper/scissors (YES/NO)? ')
        if control.lower() == 'yes' or control.lower() == 'y':
            # game logic
            print("\nPlayer 1 get ready!")
            player1 = get_play()
            # print('\n==> DEBUG: player 1 selection is: ', player1)
            print("\nPlayer 2 get ready!")
            player2 = get_play()
            # print('\n==> DEBUG: player 2 selection is: ', player2)
            if get_winner(player1,player2) == 'TIE':
                print("\nNo winners - it is a TIE")
            else:
                print('\n *** The winner is ', get_winner(player1,player2), '***')
        else:
            break

    print('\nTHANKS FOR PLAYING!')