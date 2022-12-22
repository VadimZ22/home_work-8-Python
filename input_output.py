import logger as lg

def input_data(data):
    div = [' ', ',', ';']
    for i in div:
        if i in data:
            data = data.split(i)

    with open('phonebook.csv', 'a', encoding='utf-8') as file:
        file.write(' '.join(data) + '\n')
    lg.log('input', data)


def output_data(key, data_find):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        data = []
        for i in file:
            if data_find.lower() in i.lower():
                data.append(i)
    match key:
        case 1:
            with open('out_file.txt', 'w', encoding='utf-8') as file:
                for i in data:
                    for j in i.split():
                        file.write(j + '\n')
                    file.write('\n')
            lg.log('output', 'txt', data_find)

        case 2:
            with open('out_file.csv', 'w', encoding='utf-8') as file:
                for i in data:
                    file.write(i)
            lg.log('output', 'csv', data_find)

