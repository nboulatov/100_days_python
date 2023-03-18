import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("black_states_img.gif")
screen.setup(height=491,width=725)
turtle.shape("black_states_img.gif")

data = pandas.read_csv("50_states.csv")
state_column = data.state.to_list()
correct_guesses = []

while len(correct_guesses)<50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        states_to_learn = [state for state in state_column if state not in correct_guesses]
        data = pandas.DataFrame(states_to_learn)
        data.to_csv("States to learn")
        break
    if answer_state in state_column:
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.color("black")
        t.penup()
        state_row = data[data.state == answer_state]
        t.goto(int(state_row.x),int(state_row.y))
        t.write(answer_state)

