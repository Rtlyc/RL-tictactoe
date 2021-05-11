import random

class QAgent:
    def __init__(self, alpha=0.1, gamma=1, epsilon=0.1):
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

    def update_actions(self,actions):
        """
        update available actions
        param: 
            actions(list(int)): lisf of actions
        """
        self.actions = actions

    def learn(self,state,action,reward,next_state):
        """
        learning process
        Q(St,At) = Q(St,At) + alpha * [Reward + gamma * max(Q(St+1,At+1)) - Q(St,At))]
        param: 
            state(list(int)): configuration of board 
            action(int)
            reward(float)
            next_state(list(int)): configureation of board 
        """
        q_next = self.get_gready_action(next_state)

        q = self.Q.get((tuple(state),action),None)
        if q is None:
            self.Q[(tuple(state),action)] = reward 
        else:
            self.Q[(tuple(state),action)] = q + self.alpha*(reward + self.gamma * q_next - q)


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
        for action in self.actions:
            q = self.Q.get((tuple(state),action),0)
            if q > maxq:
                maxq = q
                potentials = [action] 
            elif q == maxq:
                potentials.append(action)
        return random.choice(potentials)

    def ai(self,state)->int:
        """
        act to the environment.  
        param: 
            state(list(int)): configuration of board 
        ret: 
            action(int)
        """
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        return self.get_gready_action(state)




        