'''Write a function, first_and_last_equal, that takes a string as input and prints "Yes" if the first and last characters of the string are the same, or "No" otherwise. For instance, first_and_last_equal("everyone") should print “Yes!

def firstandlastlastequal(text):
    if text[0]==text[len(text)-1]: 
        print("Yes")
    else: 
        print("No")
    
enter_text= input("Enter your text:")

firstandlastlastequal(enter_text) '''


#code challenge  -Domain extractor

'''Code Challenge · Domain extractor
Write a function named extract_domain that takes a single argument: a string representing a dot-com URL like "https://www.example.com".
The function should return only the domain name, in this case, "example".
Assume the provided URL will always start with "https://www." and will always contain a domain name followed by ".com".
You don't need to handle input or call the function at all.

def extract_domain(url): 
    return url[4:-4] 
   
modified_url =input("Enter the URL:")
result=extract_domain(modified_url)
print(result)

'''

#code challenge - Conditional slicing
'''Code Challenge · Conditional Slicing
Due to a mistake at the local school, some student names begin with an underscore (“_”).
Create a function named clean_name that takes one argument: the student's name (str).
If the name starts with an underscore, the function should return the name without it. 
Otherwise, it should return the name unchanged.
You don't need to handle input or call the function at all.'''

def new_name(text): 
    text = text.replace("_", " ")
    print(f"new sentence {text}")

sentence=input("Enter a sentence: ")

new_name(sentence)





'''Code Challenge · Dollar to Yuan
Define a function called convert_to_yuan that accepts one argument: a string representing a money amount in dollars, formatted like "1542$".
The function should return the corresponding amount in Yuan as an int.
For this exercise, use a conversion rate of 1 Dollar = 7.15 Yuan.
There's no need to handle user input or invoke the function.
Hint: To be able to perform arithmetic operations, you need to use the int function on the string that holds the amount of money.'''