import turtle
import pandas

merki = turtle.Turtle("turtle")
merki.hideturtle()
merki.penup()

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)


data = pandas.read_csv("50_states.csv")

states = data["state"]
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What´s another state´s name?").title()
    for i in range(0, len(states)):
        if answer_state == states[i]:
            x_pos = data["x"][i]
            y_pos = data["y"][i]
            merki.goto(x_pos, y_pos)
            merki.write(states[i])
            guessed_states.append(states[i])


turtle.mainloop()
