# Write your code here :-)
WIDTH = 800
HEIGHT = 500

animal1 = Actor('giraffe')
animal1.pos = 200, 200
animate(animal1, tween="linear", duration=5, on_finished=None, animal1.pos)

def draw():
    screen.clear()
    animal1.draw()

def on_mouse_down(pos):
    if animal1.collidepoint(pos):
        if animal1.image == "giraffe":
            animal1.image = "dog"
        elif animal1.image == "dog":
            animal1.image = "giraffe"
