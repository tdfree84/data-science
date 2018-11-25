
import re

positive_words = []
with open('positive-words.txt','r') as f:
    for line in f:
        positive_words.append(line.rstrip())
        
english_common = []
with open('50-english.txt','r') as f:
    for line in f:
        english_common.append(line.rstrip())

def positive_split(row):
    words = re.split("\W+",row)
    words = [w.strip().lower() for w in words if w.strip().lower() in positive_words \
             and w.strip().lower() not in english_common and w.strip().lower() != ""]
    return words

def positive_count(thetext):
    return thetext.flatMap(positive_split).map(lambda x: (x,1)).reduceByKey(lambda x,y: (x+y)).sortBy(lambda x:-x[1])
