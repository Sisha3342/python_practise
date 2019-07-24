#var 7

coding = open('coding.txt', 'r')
coding_dictionary = dict()
for line in coding:
    line = line.rstrip('\n')
    coding_dictionary[line.split(':')[1]] = line.split(':')[0]
coding.close()


def decode_morse(msg, coding_dictionary):
        msg = msg.strip()
        decode = ''
        i = 0
        while i != len(msg):
            temp = ''
            while i != len(msg) and msg[i] != ' ':
                temp += msg[i]
                maybe_space = False
                i += 1

            if i == len(msg):
                decode += coding_dictionary[temp]
                break

            if msg[i] == ' ' and maybe_space == False:
                    maybe_space = True
                    decode += coding_dictionary[temp]
            elif msg[i] == ' ' and maybe_space == True:
                    decode += ' '
                    maybe_space = False
            i += 1
        return decode


read_file = open('input.txt', 'r')
for line in read_file:
    print(decode_morse(line.rstrip('\n'), coding_dictionary))
read_file.close()
