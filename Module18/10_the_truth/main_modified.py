def decode_text(txt: str):
    word_decode = ""
    word_shift = -3   # устанавливаем шифт на -3 изначально
    for word in txt.split():   # идём циклом по тексту.split(), т.е. делим текст на слова
        if word.find('/') != -1:   # функция find возвращает -1 если символ, переданный в неё параметром не найден, т.е. если в слове нет /, то:
            print(word_decode(word, word_shift))   #используя данные функции выводим уже расшифрованное слово
            word_shift -= 1
        else:
            print(word_decode(word, word_shift), end=' ') # обратите внимание на end

def shifter(str,shift):
    count = 0
    result = ''
    tmp=str+str
    for i in str:
        result+=tmp[count+shift]
        count+=1
    return result

def caesar_cipher(message,shift):
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGJIGKLMNOPQRSTUVY'
    abc += abc
    count = 1
    ceaser_cipher = ''
    for letter in message:
        if letter == " ":
            new_index = index
            ceaser_cipher += ' '
        else:
            index = abc.index(letter)
            new_index = index + shift
            ceaser_cipher += abc[new_index]
    print('out: ', ceaser_cipher)


text='vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
#прохожу по каждому слову в списке. Если нахожу в слове '/', то ключ смещения увеличиваю на 1.

print(decode_text(text))