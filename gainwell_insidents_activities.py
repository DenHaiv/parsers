from itertools import cycle
import string
import random
import os
import datetime

pool = cycle(['I', 'E', 'R', 'C'])
number_of_lines = 10
number_of_files = 2
act_to_inc = 5
path_incidents = 'D://Work//CKM//files//incidents'
path_activities = 'D://Work//CKM//files//activities'

DSC_RTP_REAS = 'Date of Birth Proof'

def generate_random_string(length):
    """Функция для случайной строки"""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


# Functions for incidents
def set_APP_file_name(n):
    file_name = f'PERFORMANCE_TestPenrollIcPrIncident_{n}_WI_T_PR_APPLN_20210101-2021100{n + 1}.psv'
    return file_name

def set_TYPE_file_name(n):
    file_name = f'PERFORMANCE_TestPenrollIcPrIncident_{n}_WI_T_PR_TYPE_CDE_20210101-2021100{n + 1}.psv'
    return file_name


# Functions for Acticities
def set_APP_file_AC_name(n):
    file_name = f'PERFORMANCE_TestPenrollIcPrActivity_{n}_WI_A_T_PR_APPLN_RTP_20210101-2021050{n + 1}.psv'
    return file_name


def set_ANALYST_file_name(n):
    file_name = f'PERFORMANCE_TestPenrollIcPrActivity_{n}_WI_T_ANALYST_20210101-2021050{n + 1}.psv'
    return file_name

def main():
    for file in range(number_of_files):

        os.chdir(path_incidents)

        with open(set_APP_file_name(file), 'w') as i1:
            i1.write('SAK_ATN|DTE_RECEIVED|DTE_FINALIZED|CDE_PROV_TYPE|CDE_ENROLL_TYPE')

            os.chdir(path_activities)
            with open(set_APP_file_AC_name(file), 'w') as a1:
                with open(set_ANALYST_file_name(file), 'w') as a2:

                    a1.write('NAM_USER|DSC_RTP_REAS|SAK_ATN|DTE_SYSDATE')
                    a2.write('ID_CLERK|NAM_FIRST|NAM_LAST|NAME_USER')

                    DTE_RECEIVED = '20210101'
                    DTE_FINALIZED = '20210101'
                    CDE_PROV_TYPE = (i for i in range(number_of_lines))
                    CDE_ENROLL_TYPE = (i for i in pool)

                    os.chdir(path_incidents)
                    for line in range(number_of_lines):
                        SAK_ATN = 'PERFORMANCE_' + generate_random_string(41)
                        s_out_i1 = '\n' + SAK_ATN + '|' + DTE_RECEIVED + '|' + DTE_FINALIZED + '|' + str(
                            next(CDE_PROV_TYPE)) + '|' + next(CDE_ENROLL_TYPE)
                        i1.write(s_out_i1)


                        os.chdir(path_activities)
                        NAM_USER_lst = []
                        for line in range(act_to_inc):
                            NAM_USER = 'PERFORMANCE_' + generate_random_string(41)
                            NAM_USER_lst.append(NAM_USER)
                            DTE_SYSDATE = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
                            s_out_a1 = '\n' + NAM_USER + '|' + DSC_RTP_REAS + '|' + SAK_ATN + '|' + DTE_SYSDATE
                            a1.write(s_out_a1)

                        ID_CLERK = iter(NAM_USER_lst)

                        for line in range(act_to_inc):
                            NAM_FIRST = generate_random_string(7)
                            NAM_LAST = generate_random_string(7)
                            NAME_USER = generate_random_string(3)

                            s_out_a2 = '\n' + next(ID_CLERK) + '|' + NAM_FIRST + '|' + NAM_LAST + '|' + NAME_USER

                            a2.write(s_out_a2)

        os.chdir(path_incidents)
        with open(set_TYPE_file_name(file), 'w') as i2:
            i2.write('CDE_PROV_TYPE|DSC_PROV_TYPE')

            CDE_PROV_TYPE = (i for i in range(number_of_lines))

            for line in range(number_of_lines):
                DSC_PROV_TYPE = generate_random_string(15)
                s_out_i2 = '\n' + str(next(CDE_PROV_TYPE)) + '|' + DSC_PROV_TYPE
                i2.write(s_out_i2)


if __name__ == '__main__':
    main()

