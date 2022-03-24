from itertools import cycle
import string
import random
import os

pool = cycle(['I', 'E', 'R', 'C'])
number_of_lines = 20
path = 'D://Work//CKM//files'
os.chdir(path)

def generate_random_string(length):
    """Функция для случайной строки"""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

with open('PERFORMANCE_TestPenrollIcPrIncident_18838_WI_T_PR_APPLN_20210101-20211019.psv', 'w') as f:
    f.write('SAK_ATN|DTE_RECEIVED|DTE_FINALIZED|CDE_PROV_TYPE|CDE_ENROLL_TYPE')

    DTE_RECEIVED = '20210101'
    DTE_FINALIZED = '20210101'
    CDE_PROV_TYPE = (i for i in range(500000))
    CDE_ENROLL_TYPE = (i for i in pool)

    for line in range(number_of_lines):
        SAK_ATN = 'PERFORMANCE_' + generate_random_string(41)
        s_out = '\n' + SAK_ATN + '|' + DTE_RECEIVED + '|' + DTE_FINALIZED + '|' + str(next(CDE_PROV_TYPE)) + '|' + next(CDE_ENROLL_TYPE)
        f.write(s_out)


with open('PERFORMANCE_TestPenrollIcPrIncident_18838_WI_T_PR_TYPE_CDE_20210101-20211019.psv', 'w') as f:
    f.write('CDE_PROV_TYPE|DSC_PROV_TYPE')

    CDE_PROV_TYPE = (i for i in range(500000))

    for line in range(number_of_lines):
        DSC_PROV_TYPE = generate_random_string(15)
        s_out = '\n' + str(next(CDE_PROV_TYPE)) + '|' +  DSC_PROV_TYPE
        f.write(s_out)



