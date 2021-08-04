with open('lyrics.txt', encoding="utf8") as f:
    lyrics = f.read()

lyrics_list = []
banned = [' ', '.' , ',' , '!']
lyrics_word = ''

for w in lyrics:
    w = w.lower()
    if w == '\n':
        if lyrics_word:
            lyrics_list.append(lyrics_word)
            lyrics_word = ''
    elif w not in banned:
        lyrics_word += w
    else:
        if lyrics_word:
            lyrics_list.append(lyrics_word)
        lyrics_word = ''
if lyrics_word:
    lyrics_list.append(lyrics_word)
    lyrics_word = ''

check_dupes = {}

for w in lyrics_list:
    w = w.lower()
    if w not in check_dupes:
        check_dupes[w] = 1
    else:
        check_dupes[w] += 1

most_freq_word = max(check_dupes.values())

for k in check_dupes.keys():
    if check_dupes[k] == most_freq_word:
        most_freq_word = k , check_dupes[k]

def most_common_words(most_freq_word):
    values = most_freq_word.values()
    best = max(values)
    words = []
    for k in most_freq_word:
        if most_freq_word[k] == best:
            words.append(k)
    return words , best 


def words_often(check_dupes , times):
    words = []
    word1 = []
    for i in check_dupes:
        if check_dupes[i] >= times:
            word1 = i , check_dupes[i]
            words.append(word1)
    return words 

resalt = words_often(check_dupes , 7 ) 
print(resalt)