import turtle

draw = turtle.Turtle()
screen = turtle.Screen()
screen.title("Graph Line")

def request():
    try:
        while True:
            storeList = screen.textinput("Equation", "Enter equation in slope-intercept form: ")
            if storeList == None or storeList == "":
                return
            storeList = storeList.split(" ")
            storeList = storeList[2:]

            collect = ""
            for i in storeList[0]:
                if i == 'x':
                    continue
                else:
                    collect += i
            if '/' in collect:
                collect = collect.split('/')
            else:
                collect = collect.split(" ")
                collect += '1'

            if len(storeList) > 1:
                draw_line(float(collect[0]) *20, float(collect[1]) *20, float(storeList[-1]) *20)
            else:
                draw_line(float(collect[0]) *20, float(collect[1]) *20)
    except IndexError:
        draw.write("Enter a vaild formula!", align='center', font=('Arial', 20, 'bold'))

def draw_graph(size):
    draw.hideturtle()
    draw.speed(0)
    draw.goto(0, 0)
    draw.forward(size)
    draw.backward(size * 2)
    draw.goto(0, 0)
    draw.left(90)
    draw.forward(size)
    draw.backward(size * 2)
    draw.goto(0, 0)

def draw_line(rise, run, intercept = 0):
    draw.penup()
    x, y = 0, intercept
    draw.goto(x, y)
    draw.pendown()
    draw.dot()
    while x <= 400 and x >= -400 and y <= 400 and y >= -400:
        x += run
        y += rise
        draw.pendown()
        draw.goto(x, y)
        draw.dot()
    x, y = 0, intercept
    draw.penup()
    draw.goto(x, y)
    draw.pendown()
    while x <= 400 and x >= -400 and y <= 400 and y >= -400:
        x -= run
        y -= rise
        draw.goto(x, y)
        draw.pendown()
        draw.dot()

draw_graph(400)

request()

turtle.done()