import sys
import collections
import glob
import os
import re
from random import shuffle
import time

start=time.time()

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
                  'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
                  'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',
                  'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
                  'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as',
                  'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through',
                  'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off',
                  'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how',
                  'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
                  'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should',
                  'now','chicago','affinia','allegro','amalfi','ambassador','conrad','fairmont','hardrock','hilton',
                  'hard','rock','homewood','hyatt','intercontinental','james','knickerbocker','monaco','omni','palmer',
                  'sheraton','sofitel','swissotel','talbott']

ctotal=0

#ND data
data_negative_deceptive=""
nd_words=[]
nd_reviews=[]
cnd=0
for j in range(2,5):
    a='D:/Darshan/USC MS CS/NLP/New folder/op_spam_training_data/negative_polarity/deceptive_from_MTurk/fold'+str(j)
    file_list = glob.glob(os.path.join(os.getcwd(),a, "*.txt"))
    for file_path in file_list:
        cnd=cnd+1
        ctotal=ctotal+1
        #print(file_path, cnd, ctotal)
        with open(file_path) as f_input:
            input=(f_input.read().lower())
            data_negative_deceptive=data_negative_deceptive+input
            nd_reviews.append(input)
data_negative_deceptive = re.sub(r"[,.;:'{}*()-@%#?!&$]+\ *", " ", data_negative_deceptive)
#print(len(nd_reviews))
words_negative_deceptive=data_negative_deceptive.split()
for blah in words_negative_deceptive:
    if blah not in stop_words:
        nd_words.append(blah)
#count_negative_deceptive=collections.Counter(nd_words)
#print(len(count_negative_deceptive))

#NT data
data_negative_true=""
nt_words=[]
nt_reviews=[]
cnt=0
for j in range(2,5):
    a='D:/Darshan/USC MS CS/NLP/New folder/op_spam_training_data/negative_polarity/truthful_from_Web/fold'+str(j)
    file_list = glob.glob(os.path.join(os.getcwd(),a, "*.txt"))
    for file_path in file_list:
        cnt=cnt+1
        ctotal=ctotal+1
        #print(file_path, cnt, ctotal)
        with open(file_path) as f_input:
            input=(f_input.read().lower())
            data_negative_true=data_negative_true+input
            nt_reviews.append(input)
data_negative_true = re.sub(r"[,.;:'{}*()-@#?%!&$]+\ *", " ", data_negative_true)
#print(len(nt_reviews))
words_negative_true=data_negative_true.split()
for blah in words_negative_true:
    if blah not in stop_words:
        nt_words.append(blah)
#count_negative_true=collections.Counter(nt_words)
#print(len(count_negative_true))

#PD data
data_positive_deceptive=""
pd_words=[]
pd_reviews=[]
cpd=0
for j in range(2,5):
    a='D:\\Darshan\\USC MS CS\\NLP\\HW2\\op_spam_training_data\\positive_polarity\\deceptive_from_MTurk\\fold'+str(j)
    file_list = glob.glob(os.path.join(os.getcwd(),a, "*.txt"))
    for file_path in file_list:
        cpd=cpd+1
        ctotal=ctotal+1
        #print(file_path, cpd, ctotal)
        with open(file_path) as f_input:
            input=(f_input.read().lower())
            data_positive_deceptive=data_positive_deceptive+input
            pd_reviews.append(input)
data_positive_deceptive = re.sub(r"[,.;:'{}*()-@%#?!&$]+\ *", " ", data_positive_deceptive)
#print(len(pd_reviews))
words_positive_deceptive=data_positive_deceptive.split()
for blah in words_positive_deceptive:
    if blah not in stop_words:
        pd_words.append(blah)
#count_positive_deceptive=collections.Counter(pd_words)
#print(len(count_positive_deceptive))

#PT data
data_positive_true=""
pt_words=[]
pt_reviews=[]
cpt=0
for j in range(2,5):
    a='D:\\Darshan\\USC MS CS\\NLP\\HW2\\op_spam_training_data\\positive_polarity\\truthful_from_TripAdvisor\\fold'+str(j)
    file_list = glob.glob(os.path.join(os.getcwd(),a, "*.txt"))
    for file_path in file_list:
        cpt=cpt+1
        ctotal=ctotal+1
        #print(file_path, cpt, ctotal)
        with open(file_path) as f_input:
            input=(f_input.read().lower())
            data_positive_true=data_positive_true+input
            pt_reviews.append(input)
data_positive_true = re.sub(r"[,.;:'{}*()-@%#?!&$]+\ *", " ", data_positive_true)
#print(len(pt_reviews))
words_positive_true=data_positive_true.split()
for blah in words_positive_true:
    if blah not in stop_words:
        pt_words.append(blah)
#count_positive_true=collections.Counter(pt_words)
#print(len(count_positive_true))

#find all words in respective class
positive_words=pd_words+pt_words
negative_words=nd_words+nt_words
deceptive_words=pd_words+nd_words
true_words=pt_words+nt_words

#count occurence of each word in respective class
positive_count=collections.Counter(positive_words)
negative_count=collections.Counter(negative_words)
deceptive_count=collections.Counter(deceptive_words)
true_count=collections.Counter(true_words)

#to find all reviews in respective class
p_reviews=pt_reviews+pd_reviews
n_reviews=nt_reviews+nd_reviews
d_reviews=pd_reviews+nd_reviews
t_reviews=pt_reviews+nt_reviews

positive_reviews=[]
for review in p_reviews:
    review = re.sub(r"[,.;:'{}*()-@%#?!&$]+\ *", " ", review)
    positive_reviews.append(review)
negative_reviews=[]
for review in n_reviews:
    review = re.sub(r"[,.;:'{}*()-@%#?!&$]+\ *", " ", review)
    negative_reviews.append(review)
deceptive_reviews=[]
for review in d_reviews:
    review = re.sub(r"[,.;:'{}*()-@%#?!&$]+\ *", " ", review)
    deceptive_reviews.append(review)
true_reviews=[]
for review in t_reviews:
    review = re.sub(r"[,.;:'{}*()-@%#?!&$]+\ *", " ", review)
    true_reviews.append(review)

all_reviews=positive_reviews+negative_reviews
#print(all_reviews)


#finding features to differentiate pos and neg
features_pn=[]
for word in positive_count:
    if word not in features_pn and 10<positive_count[word]<200:
        features_pn.append(word)
for word in negative_count:
    if word not in features_pn and 10<negative_count[word]<200:
        features_pn.append(word)
#print(len(features_pn))

#finding features to differentiate dec and true
features_dt=[]
for word in deceptive_count:
    if word not in features_dt and 5<deceptive_count[word]<200:
        features_dt.append(word)
for word in true_count:
    if word not in features_dt and 5<true_count[word]<200:
        features_dt.append(word)
#print(len(features_dt))

#list of dictionaries
count_of_words_of_each_review=[]
for review in all_reviews:
    dict = {}
    if review in positive_reviews:
        dict['clas']=1
    else:
        dict['clas']=-1
    c=collections.Counter(review.split())
    for key in c:
        dict[key]=c[key]
    count_of_words_of_each_review.append(dict)
#print(len(count_of_words_of_each_review))

#calculating weights and bias for pn
weights_pn={}
u_pn={}
for word in features_pn:
    weights_pn[word]=0
    u_pn[word]=0
bias_pn=0
beta_pn=0
cpn=1
for i in range(0,100):
    shuffle(count_of_words_of_each_review)
    for dict in count_of_words_of_each_review:
        activation=0
        clas=dict['clas']
        for word in dict:
            if word in features_pn:
                activation=activation+weights_pn[word]*dict[word]
        activation=activation+bias_pn
        if activation*clas <= 0:
            for word in dict:
                if word in weights_pn:
                    weights_pn[word]=weights_pn[word]+dict[word]*clas
                    u_pn[word]=u_pn[word]+clas*cpn*dict[word]
            bias_pn = bias_pn + clas
            beta_pn=beta_pn+clas*cpn
        cpn=cpn+1
beta_pn=bias_pn-beta_pn/cpn
for word in u_pn:
    u_pn[word]=weights_pn[word]-u_pn[word]/cpn

#print(weights_pn)
#print(bias_pn)

#list of dictionaries
count_of_words_of_each_review_dt=[]
for review in all_reviews:
    dict = {}
    if review in deceptive_reviews:
        dict['clas']=-1
    else:
        dict['clas']=1
    c=collections.Counter(review.split())
    for key in c:
        dict[key]=c[key]
    count_of_words_of_each_review_dt.append(dict)
#print(len(count_of_words_of_each_review))

#calculating weights and bias for dt
weights_dt={}
u_dt={}
for word in features_dt:
    weights_dt[word]=0
    u_dt[word]=0
beta_dt=0
bias_dt=0
cdt=1
for i in range(0,50):
    shuffle(count_of_words_of_each_review_dt)
    for dict in count_of_words_of_each_review_dt:
        activation=0
        clas=dict['clas']
        for word in dict:
            if word in features_dt:
                activation=activation+weights_dt[word]*dict[word]
        activation=activation+bias_dt
        if activation*clas <= 0:
            for word in dict:
                if word in weights_dt:
                    weights_dt[word]=weights_dt[word]+dict[word]*clas
                    u_dt[word]=u_dt[word]+clas*cdt*dict[word]
            beta_dt=beta_dt+clas*cdt
            bias_dt = bias_dt + clas
        cdt=cdt+1
beta_dt=bias_dt-beta_dt/cdt
for word in u_dt:
    u_dt[word]=weights_dt[word]-u_dt[word]/cdt
#print(weights_dt)
#print(bias_dt)

'''print('w',weights_pn)
print('u',u_pn)
print('w',weights_dt)
print('u',u_dt)
print(bias_pn)
print(beta_pn)
print(bias_dt)
print(beta_dt)'''
f=open("D:\\Darshan\\USC MS CS\\NLP\\HW2\\vanilla_weights_bias.txt",'w')
f.write('pos_neg_weights \n'+str(weights_pn))
f.write('\n')
f.write('pos_neg_bias \n'+str(bias_pn))
f.write('\n')
f.write('dec_tru_weights \n'+str(weights_dt))
f.write('\n')
f.write('dec_tru_bias \n'+str(bias_dt))
f.write('\n')
f.write('features_pn \n'+str(features_pn))
f.write('\n')
f.write('features_dt \n'+str(features_dt))
f.close()
f=open("D:\\Darshan\\USC MS CS\\NLP\\HW2\\average_weights_bias.txt",'w')
f.write('pos_neg_u \n'+str(u_pn))
f.write('\n')
f.write('pos_neg_beta \n'+str(beta_pn))
f.write('\n')
f.write('dec_tru_u \n'+str(u_dt))
f.write('\n')
f.write('dec_tru_beta \n'+str(beta_dt))
f.write('\n')
f.close()


print(time.time()-start)