import collections
input_path1='D:\\Darshan\\USC MS CS\\NLP\\hmm assignment\\it_isdt_train_tagged.txt'
f=open(input_path1,'r', encoding="UTF-8")
data=""
data=f.read()
dic={}
all_pairs=[]
pairs_list=[]
lines = data.split('\n')
for line in lines:
    pairs=line.split()
    pairs_list.append(pairs)
    all_pairs.extend(pairs)
updated_pairs=[]
for pair in all_pairs:
    a=pair.find('/')
    b=pair.rfind('/')
    if a< b:
        pair=pair[0:a]+pair[b:]
        updated_pairs.append(pair)
    else:
        updated_pairs.append(pair)

word_tag_frequency=collections.Counter(updated_pairs)
print("IT IS ",updated_pairs)

word_dict={}
tag_dict={}
i=0
j=0

word_tag_count={}
tag_count={}
for pair in word_tag_frequency:

    a={}
    index=pair.rfind('/')
    word=pair[0:index]
    tag=pair[index+1:]

    if word not in word_dict:
        word_dict[word]=i
        i+=1
    if tag not in tag_dict:
        tag_dict[tag] = j
        j += 1

print (tag_dict)
#print(word_tag_count)
#print(len(tag_count))
tags_only=[]
for line in pairs_list:
    extracted_tags=[]
    for pair in line:
        a=pair.rfind('/')
        extracted_tags.append(pair[a+1:])
    tags_only.append(extracted_tags)

tags_vocab=[]

for line in tags_only:
    for tag in line:
        if tag not in tags_vocab:
            tags_vocab.append(tag)
#print(len(tags_vocab))
all_transitions=collections.defaultdict(dict)
check={}
for tag in tags_vocab:
    check[tag]=1

for tag in tags_vocab:
    for element in check:
        all_transitions[tag][element]=check[element]
#print(all_transitions)

for line in tags_only:
    for i in range(0,len(line)-1):
        all_transitions[line[i]][line[i+1]]=all_transitions[line[i]][line[i+1]]+1
#print(all_transitions)

start_tag_count={}
for key in all_transitions:
    sum=0
    for inner_key in all_transitions[key]:
        sum=sum+all_transitions[key][inner_key]
    start_tag_count[key]=sum
#print(start_tag_count)

for key in all_transitions:
    for inner_key in all_transitions[key]:
        all_transitions[key][inner_key]=all_transitions[key][inner_key]/start_tag_count[key]
#print(all_transitions)

start_line_tags=[]
for line in tags_only:
    if(len(line)>0):
        start_line_tags.append(line[0])

'''for key in all_transitions:
    start_line_tags.append(key)'''

start_line_count=collections.Counter(start_line_tags)

#print(start_line_count)
#print(len(start_line_tags))
for key in start_line_count:
    start_line_count[key]=start_line_count[key]/len(start_line_tags)
#print(start_line_count)


for key in word_tag_count:
    for in_key in word_tag_count[key]:
        word_tag_count[key][in_key]=word_tag_count[key][in_key]/tag_count[in_key]


f=open('D:\\Darshan\\USC MS CS\\NLP\\hmm assignment\\hmmlearn.txt','w',encoding="UTF-8")
f.write(str(start_line_count))
f.write('\n\n')
f.write(str(all_transitions))
f.write('\n\n')
f.write(str(word_tag_count))
f.close()


#print(word_tag_count)
#print(all_transitions)
#print(len(start_line_count))
