import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
LANGUAGES = {
    "Esperanto": {'e':9,'a':12,'i':10,'n':8,'o':9,'r':6,'s':6,'t':5,'l':6,
                  'd':3,'u':3,'m':3,'p':3,'g':1,'k':4,'v':2,'f':1,'j':4},
    "Spanish": {'e':14,'a':13,'i':6,'n':7,'o':9,'r':7,'s':8,'t':5,'l':5,
                'd':6,'u':4,'m':3,'c':5,'p':3,'g':1,'b':1},
    "Portuguese": {'e':13,'a':15,'i':6,'n':5,'o':11,'r':7,'s':8,'t':5,'l':3,
                   'd':5,'u':5,'m':5,'c':4,'p':3,'h':1,'g':1,'v':2,'b':1,'f':1,'q':1},
    "Italian": {'e':12,'a':12,'i':11,'n':7,'o':10,'r':6,'s':5,'t':6,'l':7,
                'd':4,'u':3,'m':3,'c':5,'p':3,'h':2,'g':2,'v':2},
    "French": {'e':15,'a':8,'i':8,'n':7,'o':5,'r':7,'s':8,'t':7,'l':5,
               'd':4,'u':6,'m':3,'c':3,'p':3,'v':2,'f':1,'q':1,'é':2},
    "English": {'e':13,'a':8,'i':7,'n':7,'o':8,'r':6,'s':6,'t':9,'l':4,
                'd':4,'u':3,'m':2,'c':3,'p':2,'h':6,'g':2,'b':1,'f':2,'y':2,'w':2},
    "German": {'e':17,'a':7,'i':8,'n':10,'o':3,'r':7,'s':7,'t':6,'l':3,
               'd':5,'u':4,'m':3,'c':3,'h':1,'g':5,'k':3,'b':2,'f':1,'z':2,'w':1},
    "Dutch": {'e':19,'a':7,'i':7,'n':10,'o':6,'r':6,'s':4,'t':7,'l':4,
              'd':6,'u':2,'m':2,'c':1,'p':2,'h':2,'g':3,'k':2,'v':3,'b':2,'z':1,'w':2,'j':1},
    "Swedish": {'e':10,'a':9,'i':5,'n':9,'o':4,'r':8,'s':6,'t':9,'l':5,
                'd':5,'u':2,'m':4,'c':1,'p':2,'h':2,'g':2,'k':2,'v':1,'b':2,'f':2,'ä':2,'å':2,'ö':2},
    "Polish": {'e':7,'a':8,'i':7,'n':5,'o':7,'r':4,'s':4,'t':2,'l':3,
               'd':3,'u':2,'m':2,'c':4,'p':2,'h':1,'g':1,'k':3,'b':3,'z':5,'y':4,'w':1,'j':2},
    "Turkish": {'e':9,'a':12,'i':8,'n':7,'o':2,'r':7,'s':3,'t':3,'l':6,
                'd':5,'u':3,'m':4,'h':1,'g':1,'k':5,'b':1,'z':2,'y':3,'ç':1,'ğ':1,'ı':5,'ş':2,'ü':2},
}
def count_letters(text):
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def lang_check(text):
    text=text.lower().replace(" ","")
    counts=count_letters(text)
    actual = {}
    keys=list(counts.keys())
    for i in range(len(keys)):
        j=keys[i]
        actual[j]=counts[j]/len(text)*100

    lang_names = list(LANGUAGES.keys())
    best_lang=None
    best_score=-1
    for i in range(len(lang_names)):
        lang=lang_names[i]
        expected=LANGUAGES[lang]
        exp_keys=list(expected.keys())
        diff=0
        for j in range(len(exp_keys)):
            ch=exp_keys[j]
            pct=expected[ch]
            if ch in actual:
                a=actual[ch]
            else:
                a=0
            diff=diff+abs(a-pct)
        if best_score == -1 or diff < best_score:
            best_score = diff
            best_lang = lang
    return best_lang
            

text=input("ENTER YOUR TEXT: ")
print(lang_check(text))




                               