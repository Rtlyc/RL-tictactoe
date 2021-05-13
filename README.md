# RL-tictactoe

I have implemented two algorithms for the tic-tac-toe games: TD(0) & Q-Learning
For the final question, we only need TD(0) to do model-free prediction. Due to the lateness of the message in the slack, I have already done the self-play implementation so that I get ultimate value for each state. 

## Usage
See all the usage in help function in details
```
python3 main.py -h
```

play games with the trained agent
```
python3 main.py -p
```

show first three state values(this is used for the final question)
```
python3 main.py -o
```