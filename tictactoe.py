import random

class TicTacToe:
    def __init__(self):
        """
        param: 
            state(list(int)): configuration of the board 
        """
        self.state = [-1]*9


    def blank(self)->list:
        """
        return empty slots
        ret: 
           potentials(list(int)) 
        """
        potentials = []
        for i in range(len(self.state)):
            if self.state[i] == -1:
                potentials.append(i)
        return potentials

    def opponent(self):
        """
        opponent make a move randomly
        """
        move = random.choice(self.blank())
        self.state[move] = 0

    def reset(self):
        """
        reset a game
        """
        self.state = [-1]*9


    def step(self, action, player):
        """
        update available actions
        param: 
            actions(list(int)): lisf of actions
            ##player(int): 1->X, 0->O
        """
        self.state[action] = 1
        gameover, reward = self.gamecheck()
        if gameover: return self.state, reward, gameover
        # next_state = self.state[:]
        # move = random.choice(self.blank())
        # next_state[move] = 0

        # if gameover: return self.state, reward, gameover
        # if not player:
        #     self.opponent()
        #     gameover, reward = self.gamecheck()
        #     return self.state,reward,gameover
        if player != -1: # real person
            self.opponent()
            gameover, reward = self.gamecheck()
        return self.state, reward, gameover

    def pstep(self, action):
        self.state[action] = 1
        gameover, reward = self.gamecheck()
        if gameover: return self.state, reward, gameover

    def mirror(self):
        """
        change the state to be opposite so that two players can learn
        """
        newstate = []
        for val in self.state:
            if val < 0:
                newstate.append(val)
            else:
                newstate.append(1-val)
        self.state = newstate


    def render(self):
        """
        draw board
        """
        for i in range(len(self.state)):
            val = ' '
            if self.state[i] == 1: val = 'X'
            elif self.state[i] == 0: val = 'O' 
            print(val,end="")
            if i%3 != 2: print('|',end="")
            else: print()
        print()
    
    def gamecheck(self)->(bool,float):
        """
        check whether game is over 
        ret:
            gameover(bool)
            reward(float)
        """
        gamepoints = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        gameover = False
        reward = 0
        for a,b,c in gamepoints:
            if self.state[a] == self.state[b] and self.state[a] == self.state[c] and self.state[a] != -1:
                if self.state[a] == 1: reward = 1 
                else: reward = -1  
                gameover = True  
                break
        else:
            if -1 not in self.state: gameover = True 
        return gameover,reward  


    


                