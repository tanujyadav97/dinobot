from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import pickle
import string

stored_ans = pickle.load(open("ans.pkl", "r"))
stored_ans_data = pickle.load(open("ans_data.pkl","r"))

fperson=["i","my","me","our","ours","you","yours","we","us","mine","am","are"]
sperson=["you","your","you","your","yours","i","mine","you","you","yours","are","am"]

sw=stopwords.words("english")
stemmer=SnowballStemmer("english")

def ques_responce(strr):
    strr=strr.translate(string.maketrans("", ""), string.punctuation)
    temp=strr.split(' ')
    arr=[]
    stemmed=[]
    for i in temp:
        a=stemmer.stem(i)
        stemmed.append(a)
        if a not in sw:
            arr.append(i)


    if stemmed.__contains__(stemmer.stem("you")) and len(arr)<=2:
        if stemmed.__contains__(stemmer.stem("build")) or stemmed.__contains__(stemmer.stem("developed")) or stemmed.__contains__(stemmer.stem("designed")) or stemmed.__contains__(stemmer.stem("created"))or stemmed.__contains__(stemmer.stem("made")):
            return "Tanuj Yadav, a student of NIT Delhi created me. He is Awesome."
        else:
            return "I am DinoBot, the ChatBot, your intelligent friend"

    keys=stored_ans_data.keys()
    max=0
    maxi=[]
    for i in keys:
        key_words=stored_ans_data[i]
        stemmed_keywords=(stemmer.stem(x) for x in key_words)
        c=0
        for j in arr:
            j=stemmer.stem(j)
            if j in stemmed_keywords:
                c+=1
        if c>max:
            max=c
            maxi=[]
            maxi.append(i)
        else:
            if c==max and c>0:
                maxi.append(i)

    responce=""
    size_responce=len(maxi)
    if(size_responce>1):
        responce=str(size_responce)+" results found."

    if size_responce==0:
        return "Sorry! I don't remember."

    for i in maxi:
        maxarr=stored_ans[i].translate(string.maketrans("", ""), string.punctuation)
        maxarr=maxarr.split(' ')
        cnt=0
        temp=''
        for j in maxarr:
            j=j.lower()
            if j=='are':
                if cnt>0 and temp=='you':
                    temp=j
                    try:
                        ind = fperson.index(j)
                        maxarr[cnt] = sperson[ind]
                    except ValueError:
                        j = j
            else:
                temp=j
                try:
                    ind=fperson.index(j)
                    maxarr[cnt]=sperson[ind]
                except ValueError:
                    j=j
            cnt+=1


        responce=responce+'\n'+' '.join(maxarr)

    return responce

def ans_responce(str):
    temp = str.split(' ')
    if temp[0].lower()=='forget':
        return process_forget(str)
    else:

        arr = []
        for i in temp:
            a = stemmer.stem(i)
            if a not in sw:
                arr.append(i)

        index = len(stored_ans.keys()) + 1
        stored_ans[index] = str
        stored_ans_data[index] = arr
        output = open('ans.pkl', 'wb')
        pickle.dump(stored_ans, output)
        output.close()

        output = open('ans_data.pkl', 'wb')
        pickle.dump(stored_ans_data, output)
        output.close()


        return "Got it!"

def process_forget(strr):
    strr = strr.translate(string.maketrans("", ""), string.punctuation)
    temp = strr.split(' ')
    del temp[0:1]
    arr = []
    stemmed = []
    for i in temp:
        a = stemmer.stem(i)
        stemmed.append(a)
        if a not in sw:
            arr.append(i)

    keys = stored_ans_data.keys()
    max = 0
    maxi = []
    for i in keys:
        key_words = stored_ans_data[i]
        stemmed_keywords = (stemmer.stem(x) for x in key_words)
        c = 0
        for j in arr:
            j = stemmer.stem(j)
            if j in stemmed_keywords:
                c += 1
        if c > max:
            max = c
            maxi = []
            maxi.append(i)
        else:
            if c == max and c > 0:
                maxi.append(i)

    responce = ""
    size_responce = len(maxi)
    if (size_responce ==1):
        responce = str(size_responce) + " memory deleted."
    if (size_responce > 1):
        responce = str(size_responce) + " memories deleted."

    if size_responce == 0:
        return "Sorry! I don't remember this, so can't forget."

    for i in maxi:
        responce=responce+'\n("'+stored_ans[i]+'")'
        stored_ans[i]=""
        stored_ans_data[i]=""
        output = open('ans.pkl', 'wb')
        pickle.dump(stored_ans, output)
        output.close()

        output = open('ans_data.pkl', 'wb')
        pickle.dump(stored_ans_data, output)
        output.close()

    return responce