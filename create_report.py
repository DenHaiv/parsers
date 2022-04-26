with open('old.txt') as old:
    old_list = old.readlines()
    name_old_list = [i.split('\t')[0] for i in old_list]
with open('new.txt') as new:
    new_list = new.readlines()
    name_new_list = [i.split('\t')[0] for i in new_list]

with open('report.txt', 'w') as report:
    for key, val in enumerate(name_new_list):
        if val in name_old_list:
            get_index = name_old_list.index(val)
            report.write(new_list[key].strip('\n') + '\t' + '\t'.join(old_list[get_index].split('\t')[1:]))
        else:
            report.write(new_list[key])




