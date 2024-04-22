#prompt the user to enter a sentence or paragraph

text=input("Enter a sentence or paragraph")

#split the text in to words using white space as the delimeter

words=text.split()

#declare a function

def count_words(text):
    #check if input is empty
    if not text:
        return 0
    #return the count of words
    return len(words)

#call the count_words function

count=count_words(text)

#print the result that is the count of words

print("The number of words in the input is",count) 

