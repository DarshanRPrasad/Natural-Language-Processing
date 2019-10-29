import ast
import math
f=open('D:\\Darshan\\USC MS CS\\NLP\\hmm assignment\\hmmlearn.txt','r',encoding="UTF-8")
data=f.read()
f.close()
lines=data.split('\n\n')

start_tag_probs=lines[0]
a=start_tag_probs.find('{')
b=start_tag_probs.rfind(')')
sub=start_tag_probs[a:b]
start_tag_probs=ast.literal_eval(sub)


all_transitions=lines[1]
a=all_transitions.find('{')
b=all_transitions.rfind(')')
sub=all_transitions[a:b]
all_transitions=ast.literal_eval(sub)

word_with_tag_probs=lines[2]
word_with_tag_probs=ast.literal_eval(word_with_tag_probs)

f=open('D:\\Darshan\\USC MS CS\\NLP\\hmm assignment\\it_isdt_dev_raw.txt','r',encoding="UTF-8")
data=f.read()
f.close()
lines=data.split('\n')
words_in_each_line=[]
for line in lines:
    a=line.split()
    words_in_each_line.append(a)

all_tags=[]
for key in all_transitions['SP']:
    all_tags.append(key)



#print(len(words_in_each_line))
for line in words_in_each_line:
    if len(line)>0:
        print(line)
        prob={}
        for tag in all_tags:
            prob[tag]=[]
            if tag in start_tag_probs and line[0] in word_with_tag_probs and tag in word_with_tag_probs[line[0]]:
                prob[tag].append(math.log(start_tag_probs[tag])+math.log(word_with_tag_probs[line[0]][tag]))
            else:
                #prob[tag].append(math.log(start_tag_probs[tag]))
                prob[tag].append('-')
        #print(prob)

        for i in range(1,len(line)):
            for tag in all_tags:
                if line[i] in word_with_tag_probs and tag in word_with_tag_probs[line[i]]:
                    max=-9999
                    a=0
                    for parent_tag in prob:
                        if prob[parent_tag][i-1]!='-':
                            a=prob[parent_tag][i-1]+math.log(all_transitions[parent_tag][tag])+math.log(word_with_tag_probs[line[i]][tag])
                            if a>max:
                                max=a
                    prob[tag].append(a)
                else:
                    prob[tag].append('-')
        print(prob)
        most_prob=-9999
        tags_for_line=[]
        tag_seq=[]
        for tag in prob:
            if prob[tag][len(line)-1]!='-' and prob[tag][len(line)-1]>most_prob:
                most_prob=prob[tag][len(line)-1]
                end_tag=tag
        tag_seq.insert(0,end_tag)
        print(tag_seq, ' this is the end tag',most_prob)


        for i in range(len(line)-2,-1,-1):
            for tag in prob:
                if prob[tag][i]!='-' and line[i+1] in word_with_tag_probs and tag_seq[0] in word_with_tag_probs[line[i+1]] :
                    next=tag_seq[0]
                    a=prob[tag][i]+math.log(all_transitions[tag][next])+math.log(word_with_tag_probs[line[i+1]][next])
                    #print('hyyyeee',a,most_prob)
                    if a == most_prob:
                            #print('here')
                            most_prob=prob[tag][i]
                            tag_seq.insert(0,tag)
                            break

        print(tag_seq)






