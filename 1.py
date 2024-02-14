import csv

salary_list = dict()

with open('vacancy_new.csv','w') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(['Company','Role','Salary'])

with open('vacancy.csv','r', encoding='UTF-8') as file:
    reader = csv.reader(file, quotechar='"',delimiter=";")
    for salary,work_type,company_size,role,company in reader:
        if company not in salary_list.keys():
            salary_list[company] = [salary, role]
        else:
            if role == salary_list[company][1] and int(salary) > int(salary_list[company[0]]):
                salary_list[company] = [salary,role]
            else:
                salary_list[company] += [salary, role]

    for key,val in salary_list.items():

        with open('vacancy_new.csv','a', encoding='windows-1251') as f:
            if key != 'Company':
                writer = csv.writer(f,delimiter=";")
                writer.writerow([key, val[1],int(val[0])])
answ = dict()
with open('vacancy_new.csv','r',encoding='windows-1251') as f:
    reader = csv.reader(f)
    for i in reader:
        try:
            company, role, salary = ''.join(i).split(';')
        except ValueError:
            pass
        answ[salary] = [company, role]
answ.pop('Salary')
answ_keys = sorted(answ,reverse=1)

c = 0
for key in answ_keys:
    val = answ[key]
    c += 1
    if c <= 3:
        print(f'{val[0]} - {val[1]} - {key}')
    else:
        break
