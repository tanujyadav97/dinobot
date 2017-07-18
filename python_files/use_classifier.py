from sklearn.externals import joblib
clf=joblib.load("classifier.pkl")

qwords=['which','whose','what','who','whom','to','whose','what','which','where','whither','whence','when','how','why','whether','whatsoever']
arr2=['do','does','did',"don't","doesn't","didn't"]
arr3=['has','have','had',"hasn't","haven't","hadn't"]
arr4=['is','are','were']

def isques(s):

    arr = s.split(" ")
    j=arr[0].lower()
    fe1=0
    fe2=0
    fe3=0
    fe4=0
    fe5=0
    if j in qwords:
        fe1=1
    else:
        if j in arr2:
            fe2=1
        else:
            if j in arr3:
                fe3 = 1
            else:
                if j in arr4:
                    fe4=1
                else:
                    if s.endswith('?'):
                        fe5=1


    a=clf.predict([fe1,fe2,fe3,fe4,fe5])
    return a