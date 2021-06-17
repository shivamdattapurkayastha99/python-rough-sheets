import collections 


t=int(input("Enter the no of testcases"))
for i in range(t):
    text = input("Enter the text") 
    word = input("Enter the word") 
    s1 = collections.Counter(word) 
    anagram_count = 0 
    for i in range(len(text) - len(word) +1): 
        text_word = text[i:i+len(word)] 
        if s1 == collections.Counter(text_word): 
            print (f"Anagram found: {i},{text_word}") 
            anagram_count += 1 
         
    print(f"Number of anagrams found:{anagram_count}") 