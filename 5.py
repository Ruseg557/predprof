import csv

salary_list = dict()

with open('vacancy.csv','r', encoding='UTF-8') as file:
    reader = csv.reader(file, quotechar='"',delimiter=";")
    for salary,work_type,company_size,role,company in reader:
        if company not in salary_list.keys():
            salary_list[company] = [f'{salary}, {role}, {work_type}']
        else:
            if company not in salary_list.keys():
                salary_list[company] = [f'{salary}, {role}, {work_type}']
            else:
                salary_list[company] += [f'{salary}, {role}, {work_type}']


key = sorted(salary_list.values(),key=len,reverse=1)

for company in salary_list.keys():
    data = salary_list[company]
    if data == key[0]: biggest = company

comp_input = input('Введите название компании: ')
while comp_input.lower() != 'стоп!' and comp_input.lower() != 'стоп':
    if comp_input in salary_list:
        print(f'\nВ компании {comp_input} найдены следующие ваканскии: \n')
        for i in salary_list[comp_input]:
            data = i.split(', ')
            print(f'{data[1]} - {data[0]} - {data[2]}')
    else:
        print('О вакансиях в такой компании нет сведений\n')
    comp_input = input('\nВведите название компании или "СТОП" для остановки: ')
print(f'\nБольше всего вакансий в компании {biggest} - {len(salary_list[biggest])}')