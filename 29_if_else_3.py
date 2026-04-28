'''write a program to find out whether person is eligible to apply for Govt. of Gujarat clerk post or not based upon below criteria.
if candidate has general cast and age below 25 and Graduate he is eligible 
if candidate has OBC cast and age below 27 and Graduate he is eligible 
if candidate has sc cast and age below 28 and Graduate he is eligible 
if candidate has st cast and age below 30 and Graduate he is eligible 
decide what is input 
    input: caste, age, education 
check is there any common criteria
Yes candidate must be graduate
'''
caste = input("Enter your caste")
age = int(input("Enter your age"))
education = input("Enter your last qualification")
is_eligible = False

if education == 'graduate' and caste == 'general' and age<25:
    print("candidate is eligible to apply for job.")
    is_eligible = True 

if education == 'graduate' and caste == 'OBC' and age<27:
    print("candidate is eligible to apply for job.")
    is_eligible = True 

if education == 'graduate' and caste == 'sc' and age<28:
    print("candidate is eligible to apply for job.")
    is_eligible = True 

if education == 'graduate' and caste == 'st' and age<30:
    print("candidate is eligible to apply for job.")
    is_eligible = True 

if is_eligible == False:
    print("candidate is not eligible to apply for the job. sorry")