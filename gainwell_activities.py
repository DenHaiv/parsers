import string
import random
import os
import datetime
from gainwell_insidents import SAK_ATN_CONST

number_of_lines = 5
number_of_files = 1
path = 'D://Work//CKM//files//activities'
os.chdir(path)


def set_APP_file_name(n):
    file_name = f'PERFORMANCE_TestPenrollIcPrActivity_{n}_WI_A_T_PR_APPLN_RTP_20210101-20210515.psv'
    return file_name


def set_ANALYST_file_name(n):
    file_name = f'PERFORMANCE_TestPenrollIcPrActivity_{n}_WI_T_ANALYST_20210101-20210515.psv'
    return file_name


def generate_random_string(length):
    """Функция для случайной строки"""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def get_ID_CLERK(file_name):
    with open(f'D://Work//CKM//files//activities//{file_name}') as f:
        for i in f.readlines()[1:]:
            yield i.split('|')[0]


for file in range(number_of_files):
    with open(set_APP_file_name(file), 'w') as f:
        f.write('NAM_USER|DSC_RTP_REAS|SAK_ATN|DTE_SYSDATE')

        DSC_RTP_REAS = 'Date of Birth Proof'

        for line in range(number_of_lines):
            NAM_USER = 'PERFORMANCE_' + generate_random_string(41)
            DTE_SYSDATE = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
            s_out = '\n' + NAM_USER + '|' + DSC_RTP_REAS + '|' + SAK_ATN_CONST + '|' + DTE_SYSDATE
            f.write(s_out)

    with open(set_ANALYST_file_name(file), 'w') as f:
        f.write('ID_CLERK|NAM_FIRST|NAM_LAST|NAME_USER')

        ID_CLERK = get_ID_CLERK(set_APP_file_name(file))

        for line in range(number_of_lines):
            NAM_FIRST = generate_random_string(7)
            NAM_LAST = generate_random_string(7)
            NAME_USER = generate_random_string(3)

            s_out = '\n' + next(ID_CLERK) + '|' + NAM_FIRST + '|' + NAM_LAST + '|' + NAME_USER

            f.write(s_out)
