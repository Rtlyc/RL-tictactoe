from QAgent import QAgent
from tictactoe import TicTacToe
from TDAgent import TDAgent

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


##########TD(0) LEARNING############
agent1 = TDAgent(1)
agent0 = TDAgent(0)

board = TicTacToe()
for i in range(episode):
    board.reset()
    while True:
        cur_state = board.state[:]
        action1 = agent1.act(cur_state)
        next_state,reward,gameover = board.TDstep(action1, 1)

        #v(s) = v(s) + alpha(Reward + gamma * v(s') - v(s))
        agent1.learn(cur_state, reward, next_state)
        agent0.learn(cur_state, 0-reward, next_state)
        if gameover: break 

        cur_state = board.state[:]
        action0 = agent0.act(cur_state)
        next_state,reward,gameover = board.TDstep(action0, 0)
        agent0.learn(cur_state, reward, next_state)
        agent1.learn(cur_state, 0-reward, next_state)
        if gameover: break 

board.reset()
def TDcheck_probabilities(board, agent1):
    ls = [-1]*9
    for i in range(9):
        temp = board.state[:]
        if temp[i] != -1: continue
        temp[i] = agent1.player
        ls[i] = agent1.Q.get(tuple(temp),-1)
    return ls

def play(board, agent1):
    while True:
        board.reset()
        while True:
            print(TDcheck_probabilities(board, agent1))
            action1 = agent1.act(board.state)
            next_state,reward,gameover = board.TDstep(action1, 1)
            board.render()
            if gameover: break 
            p = int(input("Place ur step:(0-9)"))
            board.state[p] = 0
            board.render()
            board.gamecheck()
            if gameover: break

# play(board, agent1)



import getopt, sys
 
 
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
 
# Options
options = "hmpo"
 
# Long options
long_options = ["Help", "My_file", "Output", "Play"]
 
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            msg = \
            '''
            optional arguments:
                -h, --Help: show help messages
                -m, --My_file: show the name of the file
                -p, --Play: play with the agent
                -o, --Output: show value for first three states
            '''
            print (msg)
             
        elif currentArgument in ("-m", "--My_file"):
            print ("Displaying file_name:", sys.argv[0])
             
        elif currentArgument in ("-o", "--Output"):
            state1 = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
            state2 = [1,-1,-1,-1,-1,-1,-1,-1,-1]
            state3 = [1,-1,-1,-1,0,-1,-1,-1,-1]

            print(agent1.Q[tuple(state1)])
            print(agent1.Q[tuple(state2)])
            print(agent1.Q[tuple(state3)])

        elif currentArgument in ('-p', "--Play"):
            play(board, agent1)
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))




    



# ###########Q-LEARNING###########
# for i in range(episode):
#     board.reset()
#     # board.state[start] = 1
#     # board.opponent()
    

#     while True:
#         cur_state = board.state[:]
#         Debug(board.render)
#         agent.update_actions(board.blank())
#         action = agent.ai(cur_state) 
#         # agent.update_actions(board.blank())###update_actions
#         next_state,reward,gameover = board.step(action, 1) ####always one

#         agent.learn(cur_state,action,reward,next_state)

#         if gameover:
#             # if agent.player == 0:
#             #     board.mirror()
#             if reward: wins += 1
#             Debug(board.render)
#             break 
            
#         Debug(board.render)
#         # board.mirror()
#         # agent.switch_player()


# def show_probabilities(board,agent):
#     ls = [-1]*9
#     for action in board.blank():
#         ls[action] = agent.Q.get((tuple(board.state),action),-1)
#     print(ls)
    


# # ############play with the model

# while True:
#     board.reset()
#     board.state[start] = 1
#     board.render()
#     print()
#     p = int(input("Place ur step:(0-9)"))
#     board.state[p] = 0
#     board.render()
#     show_probabilities(board,agent)
#     while True:
#         agent.update_actions(board.blank())
#         action = agent.ai(board.state)
#         next_state,reward,gameover = board.step(action,-1)
#         board.render()
#         if gameover:
#             break 
#         p = int(input("Place ur step:(0-9)"))
#         board.state[p] = 0 
#         board.render()
#         show_probabilities(board,agent)
#         gameover,reward = board.gamecheck()
#         if gameover:
#             break


# board.reset()
# ls = [agent.Q[(tuple(board.state),action)] for action in range(9)]
# print(ls)

# print(wins/episode)