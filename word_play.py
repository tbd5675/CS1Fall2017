"""
Tate Dyer
HW5
"""

def check_deletions(word, file):
    check=""
    counter=0
    word=word.lower()
    for line in file:
        new_word=line.strip()
        for i in range (0,len(word)):
            for j in range (0, len(word)):
                if word[i]==word[i-1]:
                    break
                elif i!=j:
                    check+=word[j]
            if check!= "" and check==new_word:
                counter+=1
                print(str(counter)+ " "+ check)
            check=""
    return str(counter)

"""
tests:
raccoon-test_words.txt
1 racon - 1 deletion
trouble- test_words.txt
1 rouble- 1 deletion
grape- test_words.txt
1 gape - 1 deletion
coconut- test_words.txt
0 deletions
balloon- test_words.txt
1 ballon - 1 deletion
rattoons - test_words.txt
1 ratoons, 2 rattons, 3 rattoon - 3 deletions
"""
def main():
    word= (input("Enter a word you want to check: "))
    if word== "":
        print("Error input can not be an empty string.")
    else:
        file=(input("Enter the name of the word file to check: "))
        if file=="":
            print("Error input can not be an empty string.")
        else:
            with open(file) as f:
                print("Found " + check_deletions(word,f) + " deletions")

main()