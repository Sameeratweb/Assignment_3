
def quincy_strategy(opponent_history):
    if opponent_history[-4]=='R' and opponent_history[-3]=='P' and opponent_history[-2]=='P' and opponent_history[-1]=='S':
        return 'P'
    elif opponent_history[-4]=='P' and opponent_history[-3]=='P' and opponent_history[-2]=='S' and opponent_history[-1]=='R':
        return 'P'
    elif opponent_history[-4]=='P' and opponent_history[-3]=='S' and opponent_history[-2]=='R' and opponent_history[-1]=='R':
        return 'S'
    elif opponent_history[-4]=='S' and opponent_history[-3]=='R' and opponent_history[-2]=='R' and opponent_history[-1]=='P':
        return 'S'
    elif opponent_history[-4]=='R' and opponent_history[-3]=='R' and opponent_history[-2]=='P' and opponent_history[-1]=='P':
        return 'R'


def kris_strategy(opponent_history):

    if len(opponent_history)%3==0:
        return 'P'
    if len(opponent_history)%3==1:
        return 'R'
    if len(opponent_history)%3==2:
        return 'S'


def abbey_strategy(prev_play,opponent_history):
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    if opponent_history[-2]==opponent_history[-1]:
        if prev_play=='P':
            return ideal_response[prev_play]
        elif prev_play=='R':
            return ideal_response[prev_play]
        elif prev_play=='S':
            return ideal_response[prev_play]
    elif opponent_history[-2]!=opponent_history[-1]:
        if opponent_history[-3]!=opponent_history[-2]:
            if prev_play=='P':
                return ideal_response[opponent_history[-4]]
            elif prev_play=='R':
                return ideal_response[opponent_history[-4]]
            else:
                return ideal_response[opponent_history[-4]]
        else:
            return prev_play

def player(prev_play, opponent_history=[]):


    if not prev_play:
        opponent_history.clear()


    if len(opponent_history)<=5:
        guess = 'P'

    elif opponent_history[1]== 'P' and opponent_history[2]=='S' and opponent_history[3]=='S':
        guess = kris_strategy(opponent_history)

    elif opponent_history[1]== 'P' and opponent_history[2]=='P' and opponent_history[3]=='S':
        guess = abbey_strategy(prev_play,opponent_history)

    elif opponent_history[1]== 'R' and opponent_history[2]=='R' and opponent_history[3]=='S':
        guess = abbey_strategy(prev_play,opponent_history)

    elif opponent_history[1]== 'R' and opponent_history[2]=='P' and opponent_history[3]=='P':
        guess = quincy_strategy(opponent_history)

    opponent_history.append(prev_play)
    return guess
