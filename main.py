from QAgent import QAgent
from tictactoe import TicTacToe

episode = 100000
start = 0 #my netid is yl5680
wins = 0 
alpha = 0.1
gamma = 1 
epsilon= 0.1

board = TicTacToe()
agent = QAgent(player=1, alpha=alpha,gamma=gamma,epsilon=epsilon)

def Debug(func):
    if __debug__: 
        print(1)
        func()

for i in range(episode):
    board.reset()
    # board.state[start] = 1
    # board.opponent()
    

    while True:
        cur_state = board.state[:]
        Debug(board.render)
        agent.update_actions(board.blank())
        action = agent.ai(cur_state) 
        # agent.update_actions(board.blank())###update_actions
        next_state,reward,gameover = board.step(action, 1) ####always one

        agent.learn(cur_state,action,reward,next_state)

        if gameover:
            # if agent.player == 0:
            #     board.mirror()
            Debug(board.render)
            break 
            
        Debug(board.render)
        # board.mirror()
        # agent.switch_player()


def show_probabilities(board,agent):
    ls = [-1]*9
    for action in board.blank():
        ls[action] = agent.Q.get((tuple(board.state),action),-1)
    print(ls)
    


# play with the model

while True:
    board.reset()
    board.state[start] = 1
    board.render()
    print()
    p = int(input("Place ur step:(0-9)"))
    board.state[p] = 0
    board.render()
    show_probabilities(board,agent)
    while True:
        agent.update_actions(board.blank())
        action = agent.ai(board.state)
        next_state,reward,gameover = board.step(action,-1)
        board.render()
        if gameover:
            break 
        p = int(input("Place ur step:(0-9)"))
        board.state[p] = 0 
        board.render()
        show_probabilities(board,agent)
        gameover,reward = board.gamecheck()
        if gameover:
            break


board.reset()
ls = [agent.Q[(tuple(board.state),action)] for action in range(9)]
print(ls)