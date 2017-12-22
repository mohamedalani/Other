import sys
#Recursive function that returns a generator with all combinations
def get_all_splits(array):
    if len(array) > 1:
        for sub in get_all_splits(array[1:]):
            yield [' '.join([array[0],sub[0]])] + sub[1:]
            yield [array[0]] + sub
    else:
        yield array
        
        

def get_max_font(wide, height, words):    
    max_found = 1
    for words in get_all_splits(words):
        j=1
        length_words = [len(word) for word in words]
        #Let's find the max font size
        while max(length_words)*j <= wide and (len(words)*j) <= height:
            if j > max_found:
                max_found = j
            j+=1
    return max_found



def process_file(filename):
    file = open("output.txt","w") 
    with open(filename, "r") as input:
        lines = input.read().split("\n")
        for i, line in enumerate(lines[1:]):
            size = [int(item) for item in line.split()[:2]]
            sentence = " ".join(line.split()[2:])
            print("Case #{}: {}".format(i, get_max_font(size[0], size[1], sentence.split())))
            file.write("Case #{}: {}".format(i, get_max_font(size[0], size[1], sentence.split()))+"\n")
    file.close()
        
        
process_file(sys.argv[1])