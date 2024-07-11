import turtle
from turtle import Turtle, Screen
import pandas


screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=700, height=500)
screen.tracer(0)
turtle.shape(image)

# 1. Convert all states into a list then check if user typed correct Country
# 2. Convert guess title to count correct answer.
# 3. Create a function that makes a turtle and locate it on the map using coordinates from csv file.
data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
country_count = len(data["state"].tolist())
x_coordinate = data["x"].tolist()
y_coordinate = data["y"].tolist()


def create_turtle(answer, x_coord, y_coord):
    timy = Turtle()
    timy.penup()
    timy.goto(x=x_coord, y=y_coord)
    timy.write(f"{answer}")


points = 0
game_on = True
correct_guessed = []

while game_on:
    screen.update()
    user_guess = screen.textinput(title=f"{points}/{country_count} States Correct",
                                  prompt="Guess or type (of) to exit the game:").title()
    print(user_guess)
    if user_guess == "Of":
        game_on = False
    else:
        if user_guess in correct_guessed:
            print("Guessed already, try again")
        elif user_guess in all_states:
            country_index = all_states.index(user_guess)
            x_coord = x_coordinate[country_index]
            y_coord = y_coordinate[country_index]
            create_turtle(user_guess, x_coord, y_coord)
            points += 1
            correct_guessed.append(user_guess)
        else:
            print("Wrong!")

# Create a csv file that contains all states that user missed.
states_to_learn_dict = [state for state in all_states if state not in correct_guessed]

# states_to_learn_dict = []
#
# for states in all_states:
#     if states not in correct_guessed:
#         states_to_learn_dict.append(states)


new_file = pandas.DataFrame(states_to_learn_dict)
new_file.to_csv("states_to_learn.csv")
