from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import OrderedDict
import glob
import os
import string
import re,math
from collections import Counter
WORD=re.compile(r'\w+')
def text_to_vector(text):
    u='u'
    words = WORD.findall(text)
    wor=[]
    for i in words:
        if i is u:
            continue
        else:
            wor.append(i)
    return Counter(wor)
def clear_punctuation(s):
    clear_string = ""
    for symbol in s:
        if symbol not in string.punctuation:
            clear_string += symbol
    return clear_string
def check(result,dicc,x ):
    dect={}
    dect=result[0]
    #print dect
    #print dect['joke']
    dect1={}
    dect2={}
    dect3={}
    dect1=result[1]
    dect2=result[2]
    dect3=result[3]
    #result1=kmean(dect1)
    #print result[0],'\n\n\n\n\n\n'
    #print result[1]
    flag=0
    for k in dicc:
        if ((dect[k] ==  dect2[k]) & (dect1[k] == dect3[k])):
            flag=flag+1
            #continue
        #else:
           # kmean(result[0],result[1],x)
    #else:
      #  kmean(result[0],result[1],x)
    mm=len(dicc)
    if flag is mm:
        result=kmean(result[0],result[1],x)
        check(result,dicc)
    else:
        print 'first cluster is:\t',result[4],'\n','second cluster is:\t',result[5]
def ecludin(vec1,vec2):
    vec=set(vec1.keys()) | set(vec2.keys())
    b=0
    for i in vec:
        if i in vec1.keys():
            s=int(vec1[i])
        else:
            s=0
        if i in vec2.keys():
            r=int(vec2[i])
        else:
            r=0
        a=pow((float(s)-r),2)
        b=b+a
    c=math.sqrt(b)
    return c
path='J:\mtech\others\data\*'
files=glob.glob(path)
stop_word=set(stopwords.words("english"))
dic=OrderedDict()
stemmer=PorterStemmer()
#print len(files)
dic={}
j=0
for name in files:
    #print 'hhhh'
    fil=[]
    stem=[]
    f=open(name,"rb")
    ## print 'hh'
    for i in f:
        #print 'h'
        punc=clear_punctuation(i)
        words=word_tokenize(punc)
        for w in words:
            if w not in stop_word:
                fil.append(stemmer.stem(w))
               # print 'hello'
               
    dic[j]=[fil]
    j=j+1
    f.close() 
#print dic
#print len(dic)

x=len(dic)
vector={}
u ='u'
for i in range(x):
    ls=dic[i]
    k=''
    for m in ls:
        if m is u:
            continue
        else:
            k=k+str(m)
    #string=''.join(str(x) for y in ls)
    #print string
    vector[i]=text_to_vector(k)
#for i in range(x):
    #print i,'th doc is  ',vector[i],'\n\n'
#print vector[1].keys()
#print vector[1]
dicc=[]
for i in range(x):
    #ls=dic.keys[i]
    dicc=set(dicc)|set(vector[i].keys())    
for i in range(x):
    for j in dicc:
        if j in vector[i].keys():
            continue
        else:
            vector[i][j]='0'

def kmean(c1,c2,x):
    result={}
    for i in range(x):
        a=ecludin(c1,vector[i])
        b=ecludin(c2,vector[i])
        if(a<=b):
            result[i]=1
        else:
            result[i]=2
    #print result
    one=[]
    two=[]
    a=1
    for i in range(x):
        if result[i] is a:
            one.append(i)
        else:
            two.append(i)
    #print one
    #print two
    centroid1={}
    centroid2={}
    z=0
    #x=0
    #count=0
    #coun=0
    #l=0
    h=0
    for j in dicc:
        count=0
        x=0
        for i in one:
            x=x+int(vector[i][j])
            count=count+1
        if count is 0:
            b=0
        else:
            b=float(x)/count 
        centroid1[j]=b
        z=z+1
        coun=0
        l=0
        for k in two:
            l=l+int(vector[k][j])
            coun=coun+1
        if coun is 0:
            c=0
        else:
            c=float(l)/coun
        centroid2[j]=c
        h=h+1
    #print centroid1,'\n\n\n\n\n'
    #print centroid2
    return centroid1,centroid2,c1,c2,one,two

#c1=vector[0]
#c2=vector[2]

result=kmean(vector[0],vector[3],x)
check(result,dicc,x)
#print result[0],'\n\n'
#print result[1],'\n\n'
#print result[2],'\n\n'
#print result[3],'\n\n'
#print result[4],'\n\n'
#print result[5]

    
    
#if flag is len(dicc):
#    print 'first cluster is:\t',result[4],'\n','second cluster is:\t',result[5]
#else:
#    kmean(result[0],result[1],x)

    
