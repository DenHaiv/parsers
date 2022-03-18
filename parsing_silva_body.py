def change_line_feed(s: str):
    if '\n' in s:
        return s.replace('\n', '" + "${n}" + "')
    return s


with open('file.txt', 'r') as f:
    list_of_words = f.readline().split(',"')
    with open('file1.txt', 'w') as f1:
        # First string
        two_first_words = list_of_words[0].split(':"')
        out_line = '"{" + \n' + '"\\"' + two_first_words[0].replace('"', '').replace('{', '') + '\\":\\"' + \
                   two_first_words[1].replace('"', '') + '\\"," +'
        f1.write(out_line)

        for i in list_of_words[1:-1]:
            try:
                two_words = i.split(':"')
                if two_words[0].replace('"', '') == 'Work notes':
                    a = two_words[1].replace('\\n\\n', '" + "${n}" + "${n}" + "').replace('\\n',
                                                                                          '" + "${n}" + "').replace(
                        '""', '"')
                    out_line = '\n"\\"' + two_words[0].replace('"', '') + '\\":\\"' + a + '\\"," +'
                else:
                    out_line = '\n"\\"' + two_words[0].replace('"', '') + '\\":\\"' + two_words[1].replace('"',
                                                                                                           '') + '\\"," +'
                f1.write(out_line)
                print(out_line.replace('\n', ''))
            except:
                print(i.replace('\n', ''))

        # Last string
        two_last_words = list_of_words[-1].split(':"')
        out_line = '\n"\\"' + two_last_words[0].replace('"', '') + '\\":\\"' + two_last_words[1].replace('"',
                                                                                                         '').replace(
            '}', '') + '\\"" + ' + '\n"}"'
        f1.write(out_line)
