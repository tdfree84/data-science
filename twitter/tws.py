import re

def two_words_split(row):
    words = re.split("\W+",row)
    return_list = []
    # Create list of ['wordone wordtwo','etcone etctwo'...]
    two = []
    for i in range(len(words)):
        try:
            two.append(words[i].strip()+' '+words[i+1].strip())
        except:
            pass
    two.remove(two[-1])
    
    english_common = []
    with open('50-english.txt','r') as f:
        for line in f:
            english_common.append(line.lower().strip())
            
    dictionary = []
    with open('dictionary.txt','r') as f:
        for line in f:
            dictionary.append(line.lower().strip())

    # Get rid of unneeded phrases
    for i in range(len(two)):
            try:
                thesplit = two[i].split(' ')

                one = thesplit[0].strip().lower()
                _two = thesplit[1].strip().lower()

                if one not in "bcedfghjklmnpoqrstvwxz" \
                    and _two not in "bcedfghjklmnpoqrstvwxz" \
                    and one not in english_common and _two not in english_common \
                    and one in dictionary and _two in dictionary \
                    and one != "https" and _two != "https" \
                    and one != "rt" and _two != "rt":
                    return_list.append(two[i])
            except:
                pass
    
    return return_list

def two_words_count(thetext):
    return thetext.flatMap(two_words_split).map(lambda x: (x,1)).reduceByKey(lambda x,y: (x+y)).sortBy(lambda x:-x[1])

#print(two_words("This is a happy sentence about christmas. Have a merry christmas!"))