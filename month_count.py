def month_count():
    month_dict = {1: 'Січень',
                  2: 'Лютий',
                  3: 'Березень',
                  4: 'Квітень',
                  5: 'Травень',
                  6: 'Червень',
                  7: 'Липень',
                  8: 'Серпень',
                  9: 'Вересень',
                  10: 'Жовтень',
                  11: 'Листопад',
                  12: 'Грудень',
                  }
    try:
        enter_num_of_month = int(input('Введіть номер місяця від 0 до 12: '))
    except ValueError:
        return 'Ви вказали не цифри, спробуйте ще раз'

    try:
        return month_dict[enter_num_of_month]
    except KeyError:
        return 'Будь ласко введіть цифри в зазначеному діапазоні'


print(month_count())
