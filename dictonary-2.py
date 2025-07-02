# 1.Delete a list of keys from a dictionary
sample_dict={"name":"kelly","age":25,"salary":800,"city":"new york"}
keys=["name","salary"]
for keys in keys:
    sample_dict.pop(keys)
print(sample_dict)    

# output:
# {'age': 25, 'city': 'new york'}

# 2.Count the frequency of each character in a given string using a dictionary.
h="pallavi"
temp={}
for x in h:
    temp[x]=temp.get(x,0)+1
print(temp)    

# output:
# {'p': 1, 'a': 2, 'l': 2, 'v': 1, 'i': 1}

# 3.Swap keys and values in a dictionary.
k={'a':10,'b':20,'c':30,'d':40}
tem={}
for i,j in k.items():
    temp[j]=i
print(tem)    

# 4.write a program to sum all the values in a dictionary.
g={'english':90,'telugu':95,'social':80,'math':70}
sum=0
for i in g:
    sum+=g[i]
print(sum)    

# output:
# 335

# 5.create a nested dictionary for student details (name, roll, marks).
h={"student-1":{'name':"pallavi",'Roll':101,'marks':95},
    "student-2":{'name':"chinni",'Roll':108,'marks':78}},
print(h)

# output:
# ({'student-1': {'name': 'pallavi', 'Roll': 101, 'marks': 95}, 'student-2': {'name': 'chinni', 'Roll': 108, 'marks': 78}},)

# # 6. Convert a dictionary to a list of tuples.
k={'a':1,'b':2,'c':3,'d':5,'e':6}
for i in k.items():
    print(i)

# output:
# ('a', 1)
# ('b', 2)
# ('c', 3)
# ('d', 5)
# ('e', 6)

# # 7. Write a program to store names as keys and their lengths as values.
k=['programming','java','pythonprogramming','c++']
res={}
for i in k:
    res[i]=len(i)
print(res)   


# output:
# {'programming': 11, 'java': 4, 'pythonprogramming': 17, 'c++': 3}




# # 8. Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and 
# "odd" if the number is odd
# Expected Output:
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
g={}
for i in range(1,6):
    if i%2==0:
        g[i]="even"
    else:
        g[i]="odd"
print(g)

# output:
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

# 9. Create Reverse Word Dictionary
#  Given list of words:words = ["cat", "dog", "bat"]
#  Create a dictionary with words as keys and their reversed strings as values
#  Expected Output:
#  {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}

words = ["cat", "dog", "bat"]
k={}
for i in words:
    res=" "
    for x in i:
        res=x+res
    k[i]=res
print(k)

# output:
# {'cat': 'tac ', 'dog': 'god ', 'bat': 'tab '}