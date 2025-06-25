# from random import randint

# real_number = randint(0, 101)  # Исправлен диапазон
# try_again = 'Попробуйте снова.'
# while True:
#     try:
#         user_number = int(input('Введите число от 1 до 100 включительно: '))
#         if user_number == real_number:
#             print(f'Вы угадали. Задуманное число действительно {real_number}.')
#             break
#         elif user_number > real_number:
#             print(f'Ваше число больше того, что задано. {try_again}')
#         elif user_number < real_number:
#             print(f'Ваше число меньше того, что задано. {try_again}')
#     except ValueError:
#         print('Введено не корректное значение, попробуйте снова.')

import sys
print(sys.version)
print(sys.version_info)
print('for githab test again')