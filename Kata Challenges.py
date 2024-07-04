
'''Write a function, first_and_last_equal, that takes a string as input and prints "Yes" if the first and last characters of the string are the same, or "No" otherwise. For instance, first_and_last_equal("everyone") should print “Yes!

def firstandlastlastequal(text):
    if text[0]==text[len(text)-1]: 
        print("Yes")
    else: 
        print("No")
    
enter_text= input("Enter your text:")

firstandlastlastequal(enter_text) 


#code challenge  -Domain extractor

Code Challenge · Domain extractor
Write a function named extract_domain that takes a single argument: a string representing a dot-com URL like "https://www.example.com".
The function should return only the domain name, in this case, "example".
Assume the provided URL will always start with "https://www." and will always contain a domain name followed by ".com".
You don't need to handle input or call the function at all.

def extract_domain(url): 
    return url[4:-4] 
   
modified_url =input("Enter the URL:")
result=extract_domain(modified_url)
print(result)



#code challenge - Conditional slicing

Code Challenge · Conditional Slicing
Due to a mistake at the local school, some student names begin with an underscore (“_”).
Create a function named clean_name that takes one argument: the student's name (str).
If the name starts with an underscore, the function should return the name without it. 
Otherwise, it should return the name unchanged.

You don't need to handle input or call the function at all.
def new_name(text): 
    text = text.replace("_", " ")
    print(f"new sentence {text}")

sentence=input("Enter a sentence: ")

new_name(sentence)


def new_list(text): 
    name_list=text.split(",")
    print(name_list)

    modified_text=[]
    for names in name_list: 
        new_text=names.replace("_","")
        modified_text.append(new_text)
    print(modified_text)
    print(type(modified_text))

    result=", ".join(modified_text)
    print(result)
    print(type(result))

input_text= input("Enter the name: ")

new_list(input_text)

    




Code Challenge · Dollar to Yuan
Define a function called convert_to_yuan that accepts one argument: a string representing a money amount in dollars, formatted like "1542$".
The function should return the corresponding amount in Yuan as an int.
For this exercise, use a conversion rate of 1 Dollar = 7.15 Yuan.
There's no need to handle user input or invoke the function.
Hint: To be able to perform arithmetic operations, you need to use the int function on the string that holds the amount of money.



Task

Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.



def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0
    
    max_result=max(arr)
    min_result=min(arr)

    arr.remove(max_result)
    arr.remove(min_result)

    return sum(arr)

print(sum_array([6, 2, 1, -3, 10]))




Grade book

Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

def get_grade(s1, s2, s3):
    # Code here
    score = (s1 + s2 + s3)/3
    
    if score >=90:
        return'A'
        
    elif score >=80 and score < 90:
        return 'B'
    
    elif score >=70 and score < 80:
        return 'C'
   
    elif score >=60 and score < 70:
        return 'D'
    
    elif score >=0 and score < 60:
        return 'F'
    
    #lesson learned - in case of 90+30+100, the first conditiion resulted in "none".
    # Action - i removed >=100

    # other ways to do it:

def get_grade(s1, s2, s3):
    score =(s1+s2+s3)/3
    return 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F' 



------------------------------------
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 


def find_needle(haystack):
    if "needle" in haystack: 
        needle_position=haystack.index("needle")
        return f"found the needle at position {needle_position}"  




-------------------------------------
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


def count_positives_sum_negatives(arr):
    list=[]
    list2=[]
    
    if not arr: 
        return []
    for i in arr: 
        if i <0:
            list.append(i)
        elif i > 0: 
            list2.append(i)
            
        

    return [len(list2), sum(list)]

count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])

another way of doing it
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

#lesson learned - look for input validation line number 179
'''

