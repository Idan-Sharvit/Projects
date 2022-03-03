import pandas as pd
from screen import screen
import turtle


data = pd.read_csv('50_states.csv')
states = data.state.tolist()
good_guess = 0
game_on = True
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while game_on:
    if answer_state == 'Exit':
        missing_states = pd.DataFrame(states)
        missing_states.to_csv('states_to_learn.csv')
        print("Those are the states you have missed:")
        for state in states:
            print(state)
        exit(0)
    if answer_state in states:
        good_guess += 1
        state_x_cor = int(data.x[data.state == answer_state])
        state_y_cor = int(data.y[data.state == answer_state])
        turtle.goto(state_x_cor, state_y_cor)
        turtle.write(arg=answer_state.title(), font=('Arial', 10, 'normal'))
        states.remove(answer_state)
    answer_state = screen.textinput(title=f"{good_guess}/50 States Correct",
                                    prompt="What's another state's name?").title()

turtle.mainloop()
