import random

class TDAgent:
    def __init__(self, player, alpha=0.1, gamma=1, epsilon=0.1):
        """
        Q values will be saved in the dictionary 
        param: 
            alpha: learning_rate
            gamma: discount rate 
            epsilon: probability of chosing random action 
        """
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.Q = {}
        self.player = player


    def learn(self, cur_state, reward, next_state):
        """
        learning process
        #v(s) = v(s) + alpha(Reward + gamma * v(s') - v(s))
        param: 
            cur_state(list(int)): configuration of board 
            reward(float)
            next_state(list(int)): configureation of board 
        """
        vs = self.Q.get(tuple(cur_state),None)
        if vs is None:
            self.Q[tuple(cur_state)] = reward
        else:
            vs_next = self.Q.get(tuple(next_state), 0)
            self.Q[tuple(cur_state)] = vs + self.alpha*(reward + self.gamma * vs_next - vs)


    def get_gready_action(self,state)->int:
        """
        get the action of the maximum q given state   
        param: 
            state(list(int)): configuration of board 
        ret: 
            action(int)
        """
        maxq = -float('inf')
        potentials = []
        for action in range(len(state)):
            if state[action] != -1: continue
            temp = state[:]
            temp[action] = self.player
            q = self.Q.get(tuple(temp),0)
            if q > maxq:
                maxq = q
                potentials = [action] 
            elif q == maxq:
                potentials.append(action)
        if not potentials: return -1
        return random.choice(potentials)

    def act(self,state)->int:
        """
        act to the environment.  
        param: 
            state(list(int)): configuration of board 
        ret: 
            action(int)
        """
        potentials = [i for i in range(len(state)) if state[i]==-1]
        if random.random() < self.epsilon:
            return random.choice(potentials)
        return self.get_gready_action(state)




        