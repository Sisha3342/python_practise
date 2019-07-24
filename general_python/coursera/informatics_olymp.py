def mean(rating_list):
    sum = 0
    for i in rating_list:
        sum += i
    return sum / len(rating_list)


def take_form(contestant_info):
    return int(contestant_info.split()[2])


def take_rating(contestant_info):
    return int(contestant_info.split()[3])


nine_form_rating = []
ten_form_rating = []
eleven_form_rating = []
info_file = open('input.txt', 'r', encoding='utf8')

for i in info_file:
    form = take_form(i)
    rating = take_rating(i)

    if form == 9:
        nine_form_rating.append(rating)
    elif form == 10:
        ten_form_rating.append(rating)
    else:
        eleven_form_rating.append(rating)

print(mean(nine_form_rating), mean(ten_form_rating), mean(eleven_form_rating))
info_file.close()
