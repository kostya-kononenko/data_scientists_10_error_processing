def uniq_number():
    number_list = []

    try:
        num_of_num = int(input('Введіть будь ласко яку кількість цифр ви будете вводити: '))
    except ValueError:
        return 'Ви вказали не цифри, спробуйте ще раз'

    for i in range(num_of_num):
        try:
            my_num = int(input('Введіть будь ласко цифру: '))
        except ValueError:
            return 'Ви вказали не цифри, спробуйте ще раз'
        number_list.append(my_num)

    number_set = set(number_list)
    if len(number_list) == len(number_set):
        return "Всі введені елементи унікальні"
    else:
        return 'Є однакові елементи'
    return number_list


print(uniq_number())
