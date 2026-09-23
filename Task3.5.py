language_names = ["Esperanto", "Spanish", "Portuguese", "Italian", "French", "English", "German", "Dutch",
                  "Swedish", "Polish", "Turkish"]
Esperanto = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'p', 'g', 'k', 'v', 'f', 'j']
Spanish = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'c', 'p', 'g', 'b']
Portuguese = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'c', 'p', 'h', 'g', 'v', 'b', 'f', 'q']
Italian = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'c', 'p', 'h', 'g', 'v']
French = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'c', 'p', 'v', 'f', 'q', 'é']
English = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'c', 'p', 'h', 'g', 'b', 'f', 'y', 'w']
German = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'c', 'h', 'g', 'k', 'b', 'f', 'z', 'w']
Dutch = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'c', 'p', 'h', 'g', 'k', 'v', 'b', 'z', 'w', 'j']
Swedish = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'c', 'p', 'h', 'g', 'k', 'v', 'b', 'f', 'ä', 'å', 'ö']
Polish = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'c', 'p', 'h', 'g', 'k', 'b', 'z', 'y', 'w', 'j']
Turkish = ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'l', 'd', 'u', 'm', 'h', 'g', 'k', 'b', 'z', 'y', 'ç', 'ğ', 'ı', 'ş', 'ü']
Esperanto_count = [0] * 26
Spanish_count = [0] * 26
Portuguese_count = [0] * 26
Italian_count = [0] * 26
French_count = [0] * 26
English_count = [0] * 26
German_count = [0] * 26
Dutch_count = [0] * 26
Swedish_count = [0] * 26
Polish_count = [0] * 26
Turkish_count = [0] * 26
languages_count = [Esperanto_count, Spanish_count, Portuguese_count, Italian_count, French_count, English_count,
 German_count, Dutch_count, Swedish_count, Polish_count, Turkish_count]
languages=[Esperanto,Spanish,Portuguese,Italian,French,English,German,Dutch,Swedish,Polish,Turkish]
Esperanto_percent = [9, 12, 10, 8, 9, 6, 6, 5, 6, 3, 3, 3, 3, 1, 4, 2, 1, 4]
Spanish_percent = [14, 13, 6, 7, 9, 7, 8, 5, 5, 6, 4, 3, 5, 3, 1, 1]
Portuguese_percent = [13, 15, 6, 5, 11, 7, 8, 5, 3, 5, 5, 5, 4, 3, 1, 1, 2, 1, 1, 1]
Italian_percent = [12, 12, 11, 7, 10, 6, 5, 6, 7, 4, 3, 3, 5, 3, 2, 2, 2]
French_percent = [15, 8, 8, 7, 5, 7, 8, 7, 5, 4, 6, 3, 3, 3, 2, 1, 1, 2]
English_percent = [13, 8, 7, 7, 8, 6, 6, 9, 4, 4, 3, 2, 3, 2, 6, 2, 1, 2, 2]
German_percent = [17, 7, 8, 10, 3, 7, 7, 6, 3, 5, 4, 3, 3, 1, 5, 3, 2, 1, 2, 1, 0]
Dutch_percent = [19, 7, 7, 10, 6, 6, 4, 7, 4, 6, 2, 2, 1, 2, 2, 3, 2, 3, 2, 1, 0, 2, 1]
Swedish_percent = [10, 9, 5, 9, 4, 8, 6, 9, 5, 5, 2, 4, 1, 2, 2, 2, 2, 1, 2, 2, 2]
Polish_percent = [7, 8, 7, 5, 7, 4, 4, 2, 3, 3, 2, 2, 4, 2, 1, 1, 3, 3, 5, 4, 1, 2, 1]
Turkish_percent = [9, 12, 8, 7, 2, 7, 3, 3, 6, 5, 3, 4, 1, 1, 5, 1, 2, 3, 1, 1, 5, 2, 2]
languages_percent = [Esperanto_percent, Spanish_percent, Portuguese_percent, Italian_percent,
                    French_percent, English_percent, German_percent, Dutch_percent, Swedish_percent, Polish_percent,
                    Turkish_percent]
Esperanto_diff = [0] * len(Esperanto_percent)
Spanish_diff = [0] * len(Spanish_percent)
Portuguese_diff = [0] * len(Portuguese_percent)
Italian_diff = [0] * len(Italian_percent)
French_diff = [0] * len(French_percent)
English_diff = [0] * len(English_percent)
German_diff = [0] * len(German_percent)
Dutch_diff = [0] * len(Dutch_percent)
Swedish_diff = [0] * len(Swedish_percent)
Polish_diff = [0] * len(Polish_percent)
Turkish_diff = [0] * len(Turkish_percent)
languages_diff = [Esperanto_diff, Spanish_diff,
                  Portuguese_diff, Italian_diff, French_diff, English_diff, German_diff, Dutch_diff,
                  Swedish_diff, Polish_diff, Turkish_diff]
total = [0] * len(languages_diff)
text=input("Enter String: ")
text=text.lower()
text=text.strip()
text=text.replace(" ","")
for i in range((len(languages))):
            for j in range(len(languages[i])):
               for k in range(len(text)):
                       if(languages[i][j]==text[k]):
                               languages_count[i][j]+=1

for i in range(len(languages_count)):
        for j in range(len(languages_count[i])):
                languages_count[i][j]=languages_count[i][j]/len(text)*100

for i in range(len(languages_diff)):
        for j in range(len(languages_diff[i])):
                languages_diff[i][j] = abs(languages_count[i][j] - languages_percent[i][j])

for i in range(len(languages_diff)):
    total[i] = sum(languages_diff[i])
min:int=0
minimum = total[0]
index = 0
for i in range(len(total)):
    if minimum > total[i]:
        minimum = total[i]
        index = i
print("THE LANGUAGE U ENTERED IS: ",language_names[index])


# LANGUAGES = {
#     "Esperanto": {'e':9,'a':12,'i':10,'n':8,'o':9,'r':6,'s':6,'t':5,'l':6,
#                   'd':3,'u':3,'m':3,'p':3,'g':1,'k':4,'v':2,'f':1,'j':4},
#     "Spanish": {'e':14,'a':13,'i':6,'n':7,'o':9,'r':7,'s':8,'t':5,'l':5,
#                 'd':6,'u':4,'m':3,'c':5,'p':3,'g':1,'b':1},
#     "Portuguese": {'e':13,'a':15,'i':6,'n':5,'o':11,'r':7,'s':8,'t':5,'l':3,
#                    'd':5,'u':5,'m':5,'c':4,'p':3,'h':1,'g':1,'v':2,'b':1,'f':1,'q':1},
#     "Italian": {'e':12,'a':12,'i':11,'n':7,'o':10,'r':6,'s':5,'t':6,'l':7,
#                 'd':4,'u':3,'m':3,'c':5,'p':3,'h':2,'g':2,'v':2},
#     "French": {'e':15,'a':8,'i':8,'n':7,'o':5,'r':7,'s':8,'t':7,'l':5,
#                'd':4,'u':6,'m':3,'c':3,'p':3,'v':2,'f':1,'q':1,'é':2},
#     "English": {'e':13,'a':8,'i':7,'n':7,'o':8,'r':6,'s':6,'t':9,'l':4,
#                 'd':4,'u':3,'m':2,'c':3,'p':2,'h':6,'g':2,'b':1,'f':2,'y':2,'w':2},
#     "German": {'e':17,'a':7,'i':8,'n':10,'o':3,'r':7,'s':7,'t':6,'l':3,
#                'd':5,'u':4,'m':3,'c':3,'h':1,'g':5,'k':3,'b':2,'f':1,'z':2,'w':1},
#     "Dutch": {'e':19,'a':7,'i':7,'n':10,'o':6,'r':6,'s':4,'t':7,'l':4,
#               'd':6,'u':2,'m':2,'c':1,'p':2,'h':2,'g':3,'k':2,'v':3,'b':2,'z':1,'w':2,'j':1},
#     "Swedish": {'e':10,'a':9,'i':5,'n':9,'o':4,'r':8,'s':6,'t':9,'l':5,
#                 'd':5,'u':2,'m':4,'c':1,'p':2,'h':2,'g':2,'k':2,'v':1,'b':2,'f':2,'ä':2,'å':2,'ö':2},
#     "Polish": {'e':7,'a':8,'i':7,'n':5,'o':7,'r':4,'s':4,'t':2,'l':3,
#                'd':3,'u':2,'m':2,'c':4,'p':2,'h':1,'g':1,'k':3,'b':3,'z':5,'y':4,'w':1,'j':2},
#     "Turkish": {'e':9,'a':12,'i':8,'n':7,'o':2,'r':7,'s':3,'t':3,'l':6,
#                 'd':5,'u':3,'m':4,'h':1,'g':1,'k':5,'b':1,'z':2,'y':3,'ç':1,'ğ':1,'ı':5,'ş':2,'ü':2},
# }
# def count_letters(text):
#     counts = {}
#     for ch in text:
#         counts[ch] = counts.get(ch, 0) + 1
#     return counts

# def lang_check(text):
#     text=text.lower().replace(" ","")
#     counts=count_letters(text)
#     actual = {}
#     keys=list(counts.keys())
#     for i in range(len(keys)):
#         j=keys[i]
#         actual[j]=counts[j]/len(text)*100

#     lang_names = list(LANGUAGES.keys())
#     best_lang=None
#     best_score=-1
#     for i in range(len(lang_names)):
#         lang=lang_names[i]
#         expected=LANGUAGES[lang]
#         exp_keys=list(expected.keys())
#         diff=0
#         for j in range(len(exp_keys)):
#             ch=exp_keys[j]
#             pct=expected[ch]
#             if ch in actual:
#                 a=actual[ch]
#             else:
#                 a=0
#             diff=diff+abs(a-pct)
#         if best_score == -1 or diff < best_score:
#             best_score = diff
#             best_lang = lang
#     return best_lang
            

# text=input("ENTER YOUR TEXT: ")
# print(lang_check(text))




                               