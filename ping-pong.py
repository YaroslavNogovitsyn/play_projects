import play
from random import randint

frames = 48  # что делает эта переменная

RIGHT = play.screen.width / 2  # что делает эта переменная (как считается и назначение)
LEFT = -1 * RIGHT
TOP = play.screen.height / 2
BOTTOM = -1 * TOP
R_SIZE = 100
B_SIZE = 10

ball = play.new_circle(color='green', x=0, y=0, radius=B_SIZE)
l_racket = play.new_box(color='black', x=LEFT + 10, y=0, width=20, height=R_SIZE)
r_racket = play.new_box(color='red', x=RIGHT - 10, y=0, width=20, height=R_SIZE)


@play.when_program_starts  # "раздел программы"
def start():
    l_racket.start_physics(stable=True, obeys_gravity=False, bounciness=1, mass=1)
    r_racket.start_physics(stable=True, obeys_gravity=False, bounciness=1, mass=1)
    ball.start_physics(stable=False, x_speed=15, y_speed=randint(-10, 10), obeys_gravity=False, bounciness=1, mass=10)


def point_l():  # начать с центра поля и в нужную сторону
    ball.go_to(x=0, y=0)
    ball.physics.x_speed = -1 * abs(
        ball.physics.x_speed) - 2  # минус - летим влево, -2 или +2 ускорение с течением времени


def point_r():
    ball.go_to(x=0, y=0)
    ball.physics.x_speed = abs(ball.physics.x_speed) + 2


@play.repeat_forever
async def do():
    if play.key_is_pressed('w', 'ц'):
        l_racket.y += 15
    if play.key_is_pressed('s', "ы"):
        l_racket.y -= 15
    if play.key_is_pressed('o', "щ"):
        r_racket.y += 15
    if play.key_is_pressed('l', "д"):
        r_racket.y -= 15
    if ball.x > RIGHT - 2 * B_SIZE:  # что происходит здесь?
        point_l()  # и здесь?
    if ball.x < LEFT + 2 * B_SIZE:
        point_r()

    await play.timer(seconds=1 / frames)  # частота смены кадров (пауза раз в несколько кадров)


play.start_program()
