# Get all the anagarams from an array of words (i.e. a sentence)
def get_anagrams(words):
    words = list(set(words)) #remove duplicates from words
    groups = {} #array (map) to store strings based on their signature 
    for i in range(len(words)):
        signature = ''.join(sorted(words[i])) #get signature of a word (i.e all its characters sorted in alphabetical order)
        if signature in groups:
            groups[signature].append(i)
        else:
            groups[signature] = [i]
    anagrams = []
    for signature in groups:
        if len(groups[signature]) > 1:
            anagrams.append([words[i] for i in groups[signature]])
    return anagrams

def main():
    print("String based algorithms")

if __name__== "__main__":
  main()
