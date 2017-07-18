import json
import pickle

with open('data.json') as data_file:
    dataa = json.load(data_file)[0]


d = dataa['data']

c=0
finaldata={}


for k in d:
    r=k['paragraphs']
    for i in r:
        f=i['qas']
        for j in f:
            ans=j["answers"][0]["text"]
            ques=j["question"]
            temp = {}
            temp['sent'] = ans
            temp['isques'] = '0'
            finaldata[c]=temp
            c+=1
            temp = {}
            temp['sent'] = ques
            temp['isques'] = '1'
            finaldata[c] = temp
            c += 1

output=open('data_pickle.pkl','wb')
pickle.dump(finaldata,output)
output.close()