#начало игры
import play
from random import randint

w = play.screen.width
h = play.screen.height

#создание объектов для внешнего интерфейса
place1 = play.new_box(color = 'light green', x = 0, y = 0, width = 100, height = 200, border_width=5, border_color='green')
place2 = play.new_box(color = 'light green', x = 0, y = 0, width = 100, height = 200, border_width=5, border_color='green')
place3 = play.new_box(color = 'light green', x = 0, y = 0, width = 100, height = 200, border_width=5, border_color='green')
hello = play.new_text(words = 'Привет! Нажми на кнопку, чтобы испытать удачу!', x = 0, y = 0, font = None, font_size=40, color = 'green')
result = play.new_text(words = 'Вы выиграли!', x = 0, y = 0, font = None, font_size=40, color = 'green')
button = play.new_box(color = 'yellow', x = 0, y = 0, width = 150, height = 50)
button_text = play.new_text(words= 'Вперед!', x = 0, y = 0, font = None, font_size = 50)

#создание случайных чисел 
num1_text = play.new_text(words = '', x = -200, y = 0, font = None, font_size = 100)
num2_text = play.new_text(words = '', x = 0, y = 0, font = None, font_size = 100)
num3_text = play.new_text(words = '', x = 200, y = 0, font = None, font_size = 100)

@play.when_program_starts
def start():
    place1.x = -200
    place2.x = 0
    place3.x = 200
    hello.y = 250
    result.y = -250
    button.y = 170
    button_text.y = 170

    num1_text.hide()
    num2_text.hide()
    num3_text.hide()
    result.hide()

@play.repeat_forever
def do():
    pass

@button.when_clicked
async def clicking():
    num1 = randint(0, 9)
    num2 = randint(0, 9)
    num3 = randint(0, 9)

    num1_text.words = str(num1)
    num2_text.words = str(num2)
    num3_text.words = str(num3)

    num1_text.show()
    num2_text.show()
    num3_text.show()
    if num1 == num2 and num2 == num3 and num3 == num1:
        result.words = 'Вы выиграли!'
    else:
        result.words = 'Вы проиграли! Попробуйте снова.'
    result.show()
    await play.timer(seconds=2.0)
    num1_text.hide()
    num2_text.hide()
    num3_text.hide()
    result.hide()

play.start_program()