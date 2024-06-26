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
You don't need to handle input or call the function at all.'''

def extract_domain(url): 
    return url[4:-4] 
   
modified_url =input("Enter the URL:")
result=extract_domain(modified_url)
print(result)

