import re

def word_split(row):
    words = re.split("\W+",row)
    words = [w.strip().lower() for w in words if w!=""]
    return words

def word_count(thetext):
    return thetext.flatMap(word_split).map(lambda x: (x,1)).reduceByKey(lambda x,y: (x+y)).sortBy(lambda x:-x[1])
