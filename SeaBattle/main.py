from impl import *

N = 10  # размер стороны игрового поля
fields = init_fields(2, N)

# fields[0][0][0] = 1 # Проверка на соприкосновение кораблей
draw_fields(fields)

# Добавляем корабль
is_success = add_ship(fields[0], 2, ('А', 2), False)
if is_success:
    print('Корабль добавлен')

draw_fields(fields)
