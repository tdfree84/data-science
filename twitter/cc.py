import re
def char_split(row):
    chars = re.split("\w+",row)
    chars = [w.rstrip() for w in chars if w.rstrip()!=""]
    return chars

def char_count(thetext):
    return thetext.flatMap(char_split).map(lambda x: (x,1)).reduceByKey(lambda x,y: (x+y)).sortBy(lambda x:-x[1])
