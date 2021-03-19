# начало программы

import play

frames = 48

# задание спрайта
player = play.new_circle(color='green', x=0, y=-270, radius=20, border_color='light green')
q1 = play.new_text(words='YOU WIN!', x=0, y=0, font=None, font_size=100, color='yellow')
# задание препятствий
wall1 = play.new_box(color='black', x=0, y=0, width=100, height=10)
wall2 = play.new_box(color='black', x=-50, y=10, width=10, height=100)
wall3 = play.new_box(color='black', x=50, y=-10, width=10, height=100)
wall4 = play.new_box(color='black', x=100, y=-110, width=10, height=100)
wall5 = play.new_box(color='black', x=145, y=-160, width=100, height=10)
wall6 = play.new_box(color='black', x=-145, y=-150, width=100, height=10)
wall7 = play.new_box(color='black', x=-175, y=-200, width=300, height=10)
wall8 = play.new_box(color='black', x=-195, y=-50, width=10, height=300)
wall9 = play.new_box(color='black', x=-300, y=10, width=200, height=10)
wall10 = play.new_box(color='black', x=-300, y=-40, width=10, height=100)
wall11 = play.new_box(color='black', x=-290, y=100, width=200, height=10)
wall12 = play.new_box(color='black', x=290, y=100, width=200, height=10)
wall13 = play.new_box(color='black', x=100, y=50, width=10, height=300)
wall14 = play.new_box(color='black', x=0, y=100, width=150, height=10)
wall15 = play.new_box(color='black', x=-130, y=100, width=10, height=300)

# точка финиша
finish = play.new_text(words='finish', x=0, y=270, font=None, font_size=50)


@play.when_program_starts
def start():
    player.start_physics(bounciness=0.2)
    wall1.start_physics(can_move=False)
    wall2.start_physics(can_move=False)
    wall3.start_physics(can_move=False)
    wall4.start_physics(can_move=False)
    wall5.start_physics(can_move=False)
    wall6.start_physics(can_move=False)
    wall7.start_physics(can_move=False)
    wall8.start_physics(can_move=False)
    wall9.start_physics(can_move=False)
    wall10.start_physics(can_move=False)
    wall11.start_physics(can_move=False)
    wall12.start_physics(can_move=False)
    wall13.start_physics(can_move=False)
    wall14.start_physics(can_move=False)
    wall15.start_physics(can_move=False)
    q1.hide()

# задание движения спрайта
@play.repeat_forever
async def game():
    player.physics.x_speed = 0
    player.physics.y_speed = 0

    if play.key_is_pressed('w', 'up'):
        player.y = player.y + 5
    if play.key_is_pressed('s', 'down'):
        player.y = player.y - 5
    if play.key_is_pressed('a', 'left'):
        player.x = player.x - 5
    if play.key_is_pressed('d', 'right'):
        player.x = player.x + 5

    if player.is_touching(finish):
        wall1.hide()
        wall2.hide()
        wall3.hide()
        wall4.hide()
        wall5.hide()
        wall6.hide()
        wall7.hide()
        wall8.hide()
        wall9.hide()
        wall10.hide()
        wall11.hide()
        wall12.hide()
        wall13.hide()
        wall14.hide()
        wall15.hide()
        finish.hide()
        q1.show()

    await play.timer(seconds=1/frames)

@play.when_key_pressed("1", "2", "3")
def do1(key):
    if key == "1":
        player.color = "black"
    elif key == "2":
        player.color = "blue"
    elif key == '3':
        player.color = "red"


@play.mouse.when_clicked
def do2():
    player.go_to(play.mouse)


# конец (начало) программы
play.start_program()