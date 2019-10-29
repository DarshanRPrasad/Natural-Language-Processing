# use this file to learn naive-bayes classifier
# Expected: generate nbmodel.txt

import sys
import collections
import glob
import os
import re

if __name__ == "__main__":
    model_file = "nbmodel.txt"
    input_path = 'D:/Darshan/USC MS CS/NLP/New folder/op_spam_training_data'
    cnd = 0
    cnt = 0
    cpd = 0
    cpt = 0
    ctotal = 0
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
                  'now']
    # print(len(stop_words))
    # reading negative deceptive
    data_negative_deceptive = ""
    nd_words = []
    a = input_path + '/negative_polarity/deceptive_from_MTurk/'
    file_list = glob.glob(os.path.join(os.getcwd(), a, "*/*.txt"))
    for file_path in file_list:
        cnd = cnd + 1
        ctotal = ctotal + 1
        with open(file_path) as f_input:
            data_negative_deceptive = data_negative_deceptive + (f_input.read().lower())
            data_negative_deceptive = re.sub(r"[,.;:'{}*()-@#?!&$]+\ *", " ", data_negative_deceptive)
    words_negative_deceptive = data_negative_deceptive.split()

    for blah in words_negative_deceptive:
        if blah not in stop_words:
            nd_words.append(blah)
    count_negative_deceptive = collections.Counter(nd_words)

    '''wanted=[]
    for lsd in nd_words:
        if count_negative_deceptive[lsd]>2:
            wanted.append(lsd)

    nd_words=wanted
    count_negative_deceptive=collections.Counter(nd_words)'''

    # reading  negative true
    data_negative_true = ""
    nt_words = []
    a = input_path + '/negative_polarity/truthful_from_Web/'
    file_list = glob.glob(os.path.join(os.getcwd(), a, "*/*.txt"))

    for file_path in file_list:
        cnt = cnt + 1
        ctotal = ctotal + 1
        with open(file_path) as f_input:
            data_negative_true = data_negative_true + (f_input.read().lower())
            data_negative_true = re.sub(r"[,.;:'@#?(*)!&{}$-]+\ *", " ", data_negative_true)
    words_negative_true = data_negative_true.split()
    for blah in words_negative_true:
        if blah not in stop_words:
            nt_words.append(blah)
    count_negative_true = collections.Counter(nt_words)

    '''wanted=[]
    for lsd in nt_words:
        if count_negative_deceptive[lsd]>2:
            wanted.append(lsd)

    nt_words=wanted
    count_negative_true=collections.Counter(nt_words)'''

    # print(count_negative_true)

    # reading  positive deceptive
    data_positive_deceptive = ""
    pd_words = []
    a = input_path + '/positive_polarity/deceptive_from_MTurk/'
    file_list = glob.glob(os.path.join(os.getcwd(), a, "*/*.txt"))

    for file_path in file_list:
        cpd = cpd + 1
        ctotal = ctotal + 1
        with open(file_path) as f_input:
            data_positive_deceptive = data_positive_deceptive + (f_input.read().lower())
            data_positive_deceptive = re.sub(r"[,()*.:;@'#-?!{}&$]+\ *", " ", data_positive_deceptive)
    words_positive_deceptive = data_positive_deceptive.split()
    for blah in words_positive_deceptive:
        if blah not in stop_words:
            pd_words.append(blah)
    count_positive_deceptive = collections.Counter(pd_words)
    # print(count_positive_deceptive)

    # reading  positive true
    data_positive_true = ""
    pt_words = []
    a = input_path + '/positive_polarity/truthful_from_TripAdvisor/'
    file_list = glob.glob(os.path.join(os.getcwd(),a, "*/*.txt"))
    #file_list = glob.iglob(a, recursive=True)
    for file_path in file_list:
        print(file_path)
        cpt = cpt + 1
        ctotal = ctotal + 1
        with open(file_path) as f_input:
            data_positive_true = data_positive_true + (f_input.read().lower())
            data_positive_true = re.sub(r"[,.{}*:'();@#-?!&$]+\ *", " ", data_positive_true)
    words_positive_true = data_positive_true.split()
    for blah in words_positive_true:
        if blah not in stop_words:
            pt_words.append(blah)
    count_positive_true = collections.Counter(pt_words)
    # print(count_positive_true)

    # check

    # total distict words
    distinct = []
    for a in nd_words:
        if a not in distinct:
            distinct.append(a)
    for a in nt_words:
        if a not in distinct:
            distinct.append(a)
    for a in pd_words:
        if a not in distinct:
            distinct.append(a)
    for a in pt_words:
        if a not in distinct:
            distinct.append(a)
    print ('distinct', distinct)
    print (len(distinct))

    # smoothing
    for word in distinct:
        pt_words.append(word)
        pd_words.append(word)
        nd_words.append(word)
        nt_words.append(word)

    # after smoothing
    # print('after smoothing:')
    count_negative_deceptive = collections.Counter(nd_words)
    # print(count_negative_deceptive)
    count_negative_true = collections.Counter(nt_words)
    # print(count_negative_true)
    count_positive_deceptive = collections.Counter(pd_words)
    # print(count_positive_deceptive)
    count_positive_true = collections.Counter(pt_words)
    # print(count_positive_true)

    # total count of each class
    l1 = 0
    for w in count_negative_deceptive:
        l1 = l1 + count_negative_deceptive[w]
    # print(l1)
    l2 = 0
    for w in count_negative_true:
        l2 = l2 + count_negative_true[w]
    # print(l2)
    l3 = 0
    for w in count_positive_true:
        l3 = l3 + count_positive_true[w]
    # print(l3)
    l4 = 0
    for w in count_positive_deceptive:
        l4 = l4 + count_positive_deceptive[w]
    # print(l4)

    # calculating probabilities

    nd = {}
    nt = {}
    pd = {}
    pt = {}
    for a in distinct:
        nd[a] = count_negative_deceptive[a] / l1
        nt[a] = count_negative_true[a] / l2
        pt[a] = count_positive_true[a] / l3
        pd[a] = count_positive_deceptive[a] / l4

    # write to a file the parameters
    f = open('D:/Darshan/USC MS CS/NLP/New folder/'+model_file, "w")
    print('priors\nneg_dec ' + str(cnd / ctotal) + '\nneg_true ' + str(cnt / ctotal) + '\npos_true ' + str(
        cpt / ctotal) + '\npos_dec ' + str(cpd / ctotal))
    f.write('negative deceptive probabilities \n' + str(nd) + '\n\n')
    f.write('negative true probabilities \n' + str(nt) + '\n\n')
    f.write('positive true probabilities \n' + str(pt) + '\n\n')
    f.write('positive deceptive probabilities \n' + str(pd) + '\n\n')
    f.write('distinct words \n' + str(distinct) + '\n\n')
    f.write('priors\nneg_dec ' + str(cnd / ctotal) + '\nneg_true ' + str(cnt / ctotal) + '\npos_true ' + str(
        cpt / ctotal) + '\npos_dec ' + str(cpd / ctotal))
    f.close()