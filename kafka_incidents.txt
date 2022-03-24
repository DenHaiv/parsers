import openpyxl
import uuid
import datetime
import random
import string
import time
st = time.time()

def generate_random_string(length):
    """Функция для случайной строки"""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def generate_random_number():
    """Функция для случайной числа"""
    rand_number = random.randint(100, 9999)
    return rand_number

def rand_prior():
    """Случайное значение для столбца AT"""
    return random.randint(1, 6)

def rand_list_element():
    """Случайное значение для выбора одного UUID из списка lst"""
    return random.randint(0, num_rand)

"""Создание Excel-file со столбцами A - AU"""
wb = openpyxl.Workbook()
list_ex = wb.active

list_ex['A1'] = 'Number'
list_ex['B1'] = 'Assignment group'
list_ex['C1'] = 'Resolver Group'
list_ex['D1'] = 'Open Group'
list_ex['E1'] = 'Assigned to'
list_ex['F1'] = 'Created by'
list_ex['G1'] = 'Opened by'
list_ex['H1'] = 'Last reopened by'
list_ex['I1'] = 'Resolved by'
list_ex['J1'] = 'Updated by'
list_ex['K1'] = 'Company'
list_ex['L1'] = 'Opened'
list_ex['M1'] = 'Incident State'
list_ex['N1'] = 'Business service'
list_ex['O1'] = 'Category'
list_ex['P1'] = 'Subcategory'
list_ex['Q1'] = 'Template ID'
list_ex['R1'] = 'Category.1'
list_ex['S1'] = 'Reported on'
list_ex['T1'] = 'Owner Group'
list_ex['U1'] = 'Child Incidents'
list_ex['V1'] = 'Reassignment count'
list_ex['W1'] = 'Reopen count'
list_ex['X1'] = 'Summary'
list_ex['Y1'] = 'Updated'
list_ex['Z1'] = 'Ticket Follow-Up'
list_ex['AA1'] = 'Task type'
list_ex['AB1'] = 'Hot Ticket'
list_ex['AC1'] = 'Environment'
list_ex['AD1'] = 'Location'
list_ex['AE1'] = 'Parent Location'
list_ex['AF1'] = 'Impact'
list_ex['AG1'] = 'Urgency'
list_ex['AH1'] = 'Severity'
list_ex['AI1'] = 'Contact type'
list_ex['AJ1'] = 'Created'
list_ex['AK1'] = 'User Type'
list_ex['AL1'] = 'Work notes'
list_ex['AM1'] = 'First Call Resolution'
list_ex['AN1'] = 'Business resolve time'
list_ex['AO1'] = 'Incident alerts'
list_ex['AP1'] = 'Resolved'
list_ex['AQ1'] = 'Last reopened at'
list_ex['AR1'] = 'Updates'
list_ex['AS1'] = 'Active'
list_ex['AT1'] = 'Priority'
list_ex['AU1'] = 'Short description'

"""Заполнение ячеек статическими значениями"""
incidentState = 'Closed'
businessService = 'My Service Desk'
templateID = 'ATS WP FLASH CALL'
category1 = ''
reportedOn = ''
ownerGroup = ''
childIncidents = 0
reassignmentCount = 0
reopenCount = 0
summary = ''
updated = ''
ticketFollowUp = 0
taskType = 'Incident'
hotTicket = 'FALSE'
environment = 'Production'
location = '123, avenue of hart Levue'
parentLocation = 'Frank_[Country]'
impact = '4 - Low'
urgency = '4 - Low'
severity = '3 - Low'
contactType = 'Chat'
created = ''
userType = 'RESPONSABLE CLIENTELE'
workNotes = ''
firstCallResolution = ''
businessResolveTime  = 0
incidentAlerts = 0
resolved = ''
lastReopenedAt = ''
updates = ''
firstCallResolution = 'TRUE'
active = 'FALSE'
priority = ''
shortDescription = ''

num_lst = 100000
num_rand = 99999
num_row = 500 + 2
num_workNotes = 1

"""Формирование списка с 10000 UUID"""
lst_uuid = [f'PERFORMANCE_1_{uuid.uuid4().hex}' for __ in range(num_lst)]
#lst_uuid = [f'PERFORMANCE_1_Generated_Value_{i}' for i in range(num_lst)]

"""Заполение N-строк в Excel-file"""
for i in range(1):

    for j in range(2, num_row):
        def date_and_time():
            """Функция для генерирования случайного времени. Значение времени одинакого в одной строке"""
            return datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        def date_and_time_WN():
            """Функция для генерирования случайного времени для Work Notes"""
            res = []
            for i in range(num_workNotes):
                res.append(datetime.datetime.today().strftime(f"%d/%m/%Y %H:{str(i).zfill(2)}:%S"))
            return res



        """Значеие UUID для агента и группы. Будет использоваться одинаковое значение в строке, чтобы сохранить пропорция 1:30 для incident и incident_activity"""
        agent_and_group_uuid = lst_uuid[rand_list_element()]

        """Формирование значения workNotes; это значение эквивалентно incident activity. Отношение incident к incident_activity 1:30"""
        workNotes = ''.join([f'{date_and_time_WN()[i]} - {lst_uuid[rand_list_element()]}.one.section@test.com (Additional comments)\nsomething{rand_list_element()}\n\n' for i in range(num_workNotes)])
        #full_workNotes = '"' + workNotes + '"'

        list_ex[f'A{j}'] = agent_and_group_uuid
        list_ex[f'B{j}'] = agent_and_group_uuid
        list_ex[f'C{j}'] = agent_and_group_uuid
        list_ex[f'D{j}'] = agent_and_group_uuid
        list_ex[f'E{j}'] = agent_and_group_uuid
        list_ex[f'F{j}'] = agent_and_group_uuid
        list_ex[f'G{j}'] = agent_and_group_uuid
        list_ex[f'H{j}'] = agent_and_group_uuid
        list_ex[f'I{j}'] = agent_and_group_uuid
        list_ex[f'J{j}'] = agent_and_group_uuid
        list_ex[f'K{j}'] = agent_and_group_uuid
        list_ex[f'L{j}'] = date_and_time()
        list_ex[f'M{j}'] = incidentState
        list_ex[f'N{j}'] = businessService
        list_ex[f'O{j}'] = generate_random_string(8)
        list_ex[f'P{j}'] = generate_random_string(8)
        list_ex[f'Q{j}'] = templateID
        list_ex[f'R{j}'] = generate_random_string(8)
        list_ex[f'S{j}'] = date_and_time()
        list_ex[f'T{j}'] = lst_uuid[rand_list_element()]
        list_ex[f'U{j}'] = childIncidents
        list_ex[f'V{j}'] = reassignmentCount
        list_ex[f'W{j}'] = reopenCount
        list_ex[f'X{j}'] = generate_random_number()
        list_ex[f'Y{j}'] = date_and_time()
        list_ex[f'Z{j}'] = ticketFollowUp
        list_ex[f'AA{j}'] = taskType
        list_ex[f'AB{j}'] = hotTicket
        list_ex[f'AC{j}'] = environment
        list_ex[f'AD{j}'] = location
        list_ex[f'AE{j}'] = parentLocation
        list_ex[f'AF{j}'] = impact
        list_ex[f'AG{j}'] = urgency
        list_ex[f'AH{j}'] = severity
        list_ex[f'AI{j}'] = contactType
        list_ex[f'AJ{j}'] = date_and_time()
        list_ex[f'AK{j}'] = userType
        list_ex[f'AL{j}'] = workNotes
        list_ex[f'AM{j}'] = firstCallResolution
        list_ex[f'AN{j}'] = businessResolveTime
        list_ex[f'AO{j}'] = incidentAlerts
        list_ex[f'AP{j}'] = date_and_time()
        list_ex[f'AQ{j}'] = date_and_time()
        list_ex[f'AR{j}'] = businessResolveTime
        list_ex[f'AS{j}'] = active
        list_ex[f'AT{j}'] = rand_prior()
        list_ex[f'AU{j}'] = generate_random_string (8)

    wb.save(f'PERFORMANCE_TestSilvaAccount_{i}_silva-incident_20200202-20200202.xlsx')

end = time.time()
print(end - st)
