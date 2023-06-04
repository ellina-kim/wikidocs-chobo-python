voca = """
게맛살
구멍
글라이더
기차
대롱
더치페이
롱다리
리본
멍게
박쥐
본네트
빨대
살구
양심
이빨
이자
자율
주기
쥐구멍
차량
차박
트라이앵글
""".split()

init_word = '기차'
print('끝말잇기를 하자. 내가 먼저 말할게.\n' + init_word)
spoken_words = [init_word]


def trans_first(word):
    s1 = "냥녀뇨니라락란래량로뢰료루리"
    s2 = "양여요이나낙난내양노뇌뇨누이"
    tt = str.maketrans(s1, s2)
    return word[0].translate(tt) + word[1:]


while True:
    user_input = input('> ')
    
    if not user_input:
        continue
    elif user_input == "졌다":
        print('야호!')
        break
    elif user_input[0] != spoken_words[-1][-1]:
        print('글자가 안 이어져. 내가 이겼다!')
        break
    elif user_input in spoken_words:
        print('아까 했던 말이야. 내가 이겼어!')
        break
    else:
        spoken_words.append(user_input)
        my_word = None
        for word in list(set(voca) - set(spoken_words)):
            if word.startswith(trans_first(user_input[-1])):
                my_word = word
                break
       
        if not my_word:
            print('모르겠다. 내가 졌어.')
            break
        else:
            print(my_word)
            spoken_words.append(my_word)
            continue
    
