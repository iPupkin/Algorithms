# Blake Van Dyken
# 8/30/22
# PS0

def main():
    numWords, numLetters = input().split(" ") # get n, k
    words = []
    
    for word in range(int(numWords)):
        # sort the word alphabetically then add it to the list
        words.append("".join(sorted(input())))
        
    print(findNonAnagrams(words, int(numWords)))
    
# sort 
def findNonAnagrams(words, numWords): 
    not_anagrams = 0
    
    for word in range(numWords): # loop through list
        for otherWord in range(numWords): # compare to rest of list
            if (word != otherWord): # dont compare to itself
                # check if words do not match
                if (words[word] != words[otherWord]):
                    not_anagrams += 1
                
                
    return not_anagrams
    
if __name__ == "__main__":
    main()
    