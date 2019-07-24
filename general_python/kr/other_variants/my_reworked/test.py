morse_code = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
              '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
              '-.-': 'K', '.-..': 'L', '--': "M", '-.': 'N', '---': 'O',
              '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
              '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
              '--..': 'Z'}


def decode_morse(string_to_decode: str) -> str:
    words = []
    for word in string_to_decode.split('   '):
        words.append(''.join(map(lambda w: morse_code[w], word.split())))
    return ' '.join(words)


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as open_file:
        for line in open_file:
            print(decode_morse(line))
