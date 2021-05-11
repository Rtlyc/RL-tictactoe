from QAgent import QAgent
from tictactoe import TicTacToe

episode = 200
start = 0 #my netid is yl5680
wins = 0 
alpha = 0.1
gamma = 1 
epsilon= 0.1

board = TicTacToe()
agent = QAgent(alpha=alpha,gamma=gamma,epsilon=epsilon)

for i in range(episode):
    board.reset()
    # board.state[start] = 1
    # board.opponent()
    

    while True:
        cur_state = board.state[:]
        agent.update_actions(board.blank())
        action = agent.ai(cur_state)
        next_state,reward,gameover = board.step(action)

        agent.learn(cur_state,action,reward,next_state)

        if gameover:
            if reward == 1: wins += 1
            # board.render()
            # print()
            break 

# play with the model
'''
while True:
    board.reset()
    board.state[start] = 1
    board.render()
    p = int(input("Place ur step:(0-9)"))
    board.state[p] = 0
    while True:
        agent.update_actions(board.blank())
        action = agent.ai(board.state)
        next_state,reward,gameover = board.step(action,True)
        board.render()
        if gameover:
            break 
        p = int(input("Place ur step:(0-9)"))
        board.state[p] = 0 
        board.render()
        gameover,reward = board.gamecheck()
        if gameover:
            break
'''

board.reset()
ls = [agent.Q[(tuple(board.state),action)] for action in range(9)]
print(ls)