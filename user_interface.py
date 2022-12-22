import input_output as io

def start():
    operation = int(input('Введите действие: \n \
        1: внести данные в телефоную книгу \n \
        2: получить данные из телефонной книги \n \
        3: Выйти \n'))

    match operation:
        case 1:
            var = int(input('Каким образом хотите ввести данные: \n \
                1: Одной строкой (ФИО, телефон, комментарий. ) \n \
                2: Построчно \n '))

            match var:
                case 1:
                    io.input_data(input('Введите данные, в качестве разделителя используйте пробел, запятую или точку с запятой \n'))
                case 2:
                    n1 = input('Фамилия: ')
                    n2 = input('Имя: ')
                    n3 = input('Отчество: ')
                    p = input('Телефон: ')
                    c = input('Комментарий: ')
                    data = ' '.join([n1,n2,n3,p,c])
                    io.input_data(data)
                case _: exit()

        case 2:
            find_data = input('Введите критерий поиска: ')
            key = int(input('\
                            1: выгрузить в out_file.txt(построчное отображение) \n \
                            2: Выгрузить в out_file.csv(отображение данных в одну строку) \n '))
            match key:
                case 1|2:
                    io.output_data(key, find_data)
                case _: exit()

        case 3: exit()
        case _: exit()
