import play

# ЭКРАН
frames = 45  # частота кадров
lose = play.new_text(words='YOU LOSE', font_size=100, color='red')
win = play.new_text(words='YOU WIN', font_size=100, color='yellow')
platform = play.new_box(
    color='brown', y=-250, width=150, height=15
)

ball = play.new_circle(
    color='green', y=-160, radius=15
)
blocks = []


# count = play.new_text(words = '0', x = 200, y = -150, font = None, font_size = 30)
# count_text = play.new_text(words='Количество неудачных попыток: ', x = 0, y = -150, font = None, font_size = 30)

@play.when_program_starts
def start():
    # платформа не поддается гравитации и управляется только с клавиатуры
    platform.start_physics(
        stable=True, obeys_gravity=False, bounciness=1, mass=1
    )
    # шарик не поддается гравитации, случайно перемещается по полю
    ball.start_physics(
        ball.start_physics(stable=False, x_speed=35, y_speed=35, obeys_gravity=False, bounciness=1, mass=10)
    )

    # генерация блоков
    block_x = play.screen.left + 75
    block_y = play.screen.top - 50

    for i in range(3):  # количество рядов
        while block_x <= play.screen.right - 30:
            # for i in range(8):
            block = play.new_box(
                color='grey', x=block_x, y=block_y, width=110, height=30, border_color='dark grey', border_width=1
            )
            blocks.append(block)
            block_x = block_x + block.width
        block_x = play.screen.left + 75
        block_y = block.y - block.height

    # for i in range(len(blocks)):
    # blocks[i].show()

    platform.show()
    lose.hide()
    win.hide()


@play.repeat_forever
async def game():
    # перемещение платформы
    if play.key_is_pressed('a'):
        platform.physics.x_speed = -20
    elif play.key_is_pressed('d'):
        platform.physics.x_speed = 20
    else:
        platform.physics.x_speed = 0

    # удаление блоков
    for b in blocks:
        if b.is_touching(ball):
            # ball.x_speed=-ball.x_speed
            # ball.y_speed=-ball.y_speed
            ball.physics.x_speed = -1 * ball.physics.x_speed
            ball.physics.y_speed = -1 * ball.physics.y_speed
            b.hide()
            blocks.remove(b)

    # проигрыш
    if ball.y <= platform.y:
        for b in blocks:
            blocks.remove(b)
        play.set_backdrop('light blue')
        platform.hide()
        ball.hide()
        lose.show()

    # выигрыш
    if len(blocks) == 0:
        play.set_backdrop('light yellow')
        win.show()

    await play.timer(seconds=1 / frames)  # частота смены кадров (пауза раз в несколько кадров)


@play.when_key_pressed("1", "2", "3", "4")
def do1(key):
    if key == "1":
        platform.color = "blue"
    elif key == "2":
        platform.color = "green"
    elif key == '3':
        platform.color = "red"
    elif key == '4':
        platform.color = "brown"


play.start_program()
