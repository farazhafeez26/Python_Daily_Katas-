
#-----------------------------------------------


# 23rd Sept - Warm up 

languages= ["python","Ruby", "java", "perl" ]
languages.append("c++")
languages.remove("java")

languages.sort()

print(languages)


movies = {
    "Inception": {"year": 2010, "director": "Christopher Nolan", "genre": "Sci-Fi"},
    "The Matrix": {"year": 1999, "director": "Lana Wachowski, Lilly Wachowski", "genre": "Sci-Fi"}
}

movies["Jurassic Park"]={"year": 2010, "director": "Steven Spielberg", "genre": "Sci-Fi"}

#print(movies)

def movie_info(title):
    if title in movies:
        details=movies[title]
        print(f"{title}:")

        for  x, y in details.items():
            print(f"{x}:{y}")
    else:
        print("not found")

def find_movie_year(title):
    if title in movies: 
        return movies[title]["year"]
    else: 
        print("not found")


title=input("Enter the movie title:")

movie_info(title)



#-----------------------------------------------
'''Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.

In Roman numerals:

1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.
   1 -->       "I"
1000 -->       "M"
1666 --> "MDCLXVI"

'''

'''

def solution(n):
    if 1 <= n <= 3999:
        roman_map = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
            90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        roman = ''
        for value, symbol in roman_map.items():
            print(value, symbol)
            while n >= value:
                roman += symbol
                n -= value
        return roman
    else:
        return 'Please enter a number between 1 and 3999'


alternative: 

def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string=''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >=key:
            roman_string+=roman_numerals[key]
            n-=key
    return roman_string

'''    

#-----------------------------------------------


'''

#23rd July Check three and two 7kyu 

def check_three_and_two(array):
    if len(array) != 5:
        return False
    
    a_count = array.count("a")
    b_count = array.count("b")
    c_count = array.count("c")

    counts= [a_count,b_count,c_count]

    return sorted(counts)==[0,2,3]
'''
#-----------------------------------------------




'''

#22nd July Spanish Conjugator
def conjugate(verb):
    word_er = {
      "yo": "o",
      "tú": "es",
      "él/ella/Ud.": "e",
      "nosotros/nosotras": "emos",
      "vosotros/vosotras": "\u00E9" + "is",  # Unicode for é
      "ellos/ellas/Uds.": "en"
  }

    word_ar = {
      "yo": "o",
      "tú": "as",
      "él/ella/Ud.": "a",
      "nosotros/nosotras": "amos",
      "vosotros/vosotras": "\u00E1" + "is",  # Unicode for á
      "ellos/ellas/Uds.": "an"
  }

    word_ir = {
      "yo": "o",
      "tú": "es",
      "él/ella/Ud.": "e",
      "nosotros/nosotras": "imos",
      "vosotros/vosotras":  "\u00ED" + "s",  # Corrected to Unicode for í
      "ellos/ellas/Uds.": "en"
  }

    if verb[-2:] == "ar":
        stem = verb[:-2]
        endings = word_ar
    elif verb[-2:] == "er":
        stem = verb[:-2]
        endings = word_er
    elif verb[-2:] == "ir":
        stem = verb[:-2]
        endings = word_ir
    else: 
        return "enter a valid verb"

    conjugations = [stem + v for v in endings.values()]

    return {verb: conjugations}

'''


# Examples

# Duplicate encode

'''
print(duplicate_encode("din"))      # => "((("
print(duplicate_encode("recede"))   # => "()()()"
print(duplicate_encode("Success"))  # => ")())())"
print(duplicate_encode("(( @"))     # => "))((" 

def duplicate_encode(word):
  char_count = {}
  word_lower=word.lower()

  for char in word: 
    if char in char_count:
      char_count[char]+=1
    else:
      char_count[char]=1
  print(f"character {char}:{char_count}")      
  encoded_string = ""
  for char in word: 
    if char_count[char]==1:
      encoded_string+="("
    else:
      encoded_string+=")"
      
  print(encoded_string)
      
duplicate_encode("success")  

'''




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

'''Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him.

Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message:

If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
If he doesn't get 10 hoops, return the string "Keep at it until you get it".'''
'''
def hoop_count(n):
    # Good Luck!
   
    if n >=10: 
        return "Great, now move on to tricks"
    else: 
        return "Keep at it until you get it"
    '''


'''def even_or_odd(number):
  if number%2==0: 
      return "Even"
  else:
      return "Odd"

even_or_odd(-419)
'''
'''
To convert international clothing sizes (such as "xs", "s", "xxl") to European number sizes, we need to handle arbitrary amounts of the "x" modifier. The base size for medium (m) is 38, and each "x" modifies the size by adding or subtracting 2.
def size_to_number(size):
    base_medium = 38
    size = size.lower()
    
    # Count the number of 'x' characters
    count_x = size.count("x")
    
    if size.count('s') + size.count('m') + size.count('l') != 1:
        return None

    # Check for 'm' with modifiers
    if 'm' in size and 'x' in size:
        return None
    # Determine the size based on the presence of 's', 'm', or 'l'
    if "s" in size:
        return 36 - (count_x * 2)
    elif "m" in size:
        return base_medium
    elif "l" in size:
        return 40 + (count_x * 2)
    else:
        return None  # Return None if the size is not recognized
    
'''



'''
def make_negative(number):
    if number>0:
        return -number
    else: 
        return number
    
    def make_negative(number):
    if number>0:
        return -number
    else: 
        return number
        '''
'''
def duplicate_encode(word):
    # Convert the word to lowercase to ignore capitalization
    lower_word = word.lower()
    
    # Count occurrences of each character
    char_count = {}
    for char in lower_word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Build the new string based on the counts
    encoded_string = ""
    for char in lower_word:
        if char_count[char] == 1:
            encoded_string += "("
        else:
            encoded_string += ")"
    
    return encoded_string


'''

