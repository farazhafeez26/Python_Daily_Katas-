'''Write a function, first_and_last_equal, that takes a string as input and prints "Yes" if the first and last characters of the string are the same, or "No" otherwise. For instance, first_and_last_equal("everyone") should print “Yes!'''

def first_and_last_last_equal(text):
    if text[0]==text[len(text)-1]: 
        print("Yes")
    else: 
        print("No")
    
enter_text= input("Enter your text:")

first_and_last_last_equal(enter_text)