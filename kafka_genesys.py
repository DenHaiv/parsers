import openpyxl
import uuid
import datetime
import random
import string
import time
import os
st = time.time()

"""Создание Excel-file со столбцами A - AU"""
wb = openpyxl.Workbook()
list_ex = wb.active

list_ex['A1'] = 'interaction_resource_id'
list_ex['B1'] = 'employee_id'
list_ex['C1'] = 'interaction_id'
list_ex['D1'] = 'queue_duration_seconds'
list_ex['E1'] = 'mediation_duration_seconds'
list_ex['F1'] = 'media_name'
list_ex['G1'] = 'ring_duration_seconds'
list_ex['H1'] = 'after_call_work_duration_seconds'
list_ex['I1'] = 'talk_time_seconds'
list_ex['J1'] = 'start_ts'
list_ex['K1'] = 'end_ts'
list_ex['L1'] = 'hold_duration_seconds'
list_ex['M1'] = 'technical_result'
list_ex['N1'] = 'resource_type'
list_ex['O1'] = 'employee_name'
list_ex['P1'] = 'interaction_type'

def generate_random_string(length):
    """Функция для случайной строки"""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(length))
    return rand_string

number_of_agents = 500

"""Формирование списка agents с 10000 UUID"""
agents_lst = [f'PERFORMANCE_1_{uuid.uuid4().hex + generate_random_string(10)}' for _ in range(2, number_of_agents + 2)]


"""Заполнение ячеек статическими значениями"""
queue_duration_seconds = 1
mediation_duration_seconds = 2
media_name = 'Voice'
ring_duration_seconds = 7
after_call_work_duration_seconds = 4
talk_time_seconds = 1840
start_ts = '02/01/2019 13:40:00'
end_ts = '02/01/2019 14:11:00'
hold_duration_seconds = 9
technical_result = 'Completed'
resource_type = 'Agent'
employee_name = 'Perf_Employee_Name'
interaction_type = 'INBOUND'

path = 'E://Python/Study/Tutor/days'
os.mkdir(path)

end_day = 1
num_of_files = 17
num_rows = 20000 + 2
"""Заполение N-строк в Excel-file"""
for d in range(1, end_day + 1):
    path_for_day = f'{path}/day{d}'
    os.mkdir(path_for_day)
    for i in range(num_of_files):
        os.chdir(path_for_day)
        for j in range(2, num_rows):

            list_ex[f'A{j}'] = f'PERFORMANCE_1_{uuid.uuid4().hex + generate_random_string(10)}'
            list_ex[f'B{j}'] = agents_lst[j % 500]
            list_ex[f'C{j}'] = f'PERFORMANCE_1_{uuid.uuid4().hex + generate_random_string(10)}'
            list_ex[f'D{j}'] = queue_duration_seconds
            list_ex[f'E{j}'] = mediation_duration_seconds
            list_ex[f'F{j}'] = media_name
            list_ex[f'G{j}'] = ring_duration_seconds
            list_ex[f'H{j}'] = after_call_work_duration_seconds
            list_ex[f'I{j}'] = talk_time_seconds
            list_ex[f'J{j}'] = start_ts
            list_ex[f'K{j}'] = end_ts
            list_ex[f'L{j}'] = hold_duration_seconds
            list_ex[f'M{j}'] = technical_result
            list_ex[f'N{j}'] = resource_type
            list_ex[f'O{j}'] = employee_name
            list_ex[f'P{j}'] = interaction_type

        wb.save(f'PERFORMANCE_TestGenesysAccount_31_{i}_genesys_20190102-20190102.xlsx')

end = time.time()
print(end - st)
