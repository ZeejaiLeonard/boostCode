# Write your code here :-)
animal = Actor('giraffe')
animal.pos = 200, 200

WIDTH = 800
HEIGHT = 500

def draw():
    screen.clear()
    animal.draw()

def on_mouse_down(pos):
    if animal.collidepoint(pos):
        if animal.image == "giraffe":
            animal.image = "dog"
        elif animal.image == "dog":
            animal.image = "giraffe"



