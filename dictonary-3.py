# 1.invert a dictionary with list values (group keys by their values)
d={'a':1,'b':2,'c':1,'d':3}
res={}
for key,value in d.items():
    res.setdefault(value,[]).append(key)
    print(res)

#     output:
# {1: ['a']}
# {1: ['a'], 2: ['b']}
# {1: ['a', 'c'], 2: ['b']}
# {1: ['a', 'c'], 2: ['b'], 3: ['d']}

# 2.find max and min value in dictionary
d={'a':10,'b':5,'c':15}
print("Max Value-->", max(d.values()))
print("Min Value-->",min(d.values()))

# output:
# Max Value--> 15
# Min Value--> 5

# 3.Create a dictionary comprehension for the given list of number,where
# each number is a key
# the value is "prime" if the number is prime.
# the value is "notprime"if the number is not prime.

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
nums=[2,3,4,5,6]
result={n:'prime' if is_prime(n)else"not prime" for n in nums}  
print(result)  

# output:
# {2: 'prime', 3: 'prime', 4: 'not prime', 5: 'prime', 6: 'not prime'}

# 4.Create a dictionary from a list of words,keys as words,values as word length,but only for words longer than 3 characters
list=["hi","hello","world","is","great"]
res={x:len(x) for x in list if len(x)>3}
print(res)

# output:
# {'hello': 5, 'world': 5, 'great': 5}

# 5.Create a dictionary with uppercase letters as keys and their ASCII values as values use dict comprehension.
# {'A':65,'B':66,'c':67}
letters=['A','B','c']
res={chr(ord(i)-32):ord(i)-32 for i in letters}
print(res)

# output:
# {'A': 65, 'B': 66, 'C': 67}

# 6. Explain about setdefault function in dictionary data type ?

 Purpose:
1. setdefault() tries to get the value for a given key.
2. If the key exists, it simply returns its current value.
3.If the key does not exist, it inserts the key with a specified default value, then returns that default.

# # 7. Difference between d[key] and d.get(key)?

i.d[key]
1. Accesses the value directly for the key key.
2. If the key exists, returns its value.
3. If the key does not exist, raises a KeyError exception.
eg:
d={'a':10}
print(d['b'])
# output:
# error:keyerror

ii.d.get(key)
d={'a':10}
print(d.get('b'))

# output:
# none


# # 8. What is the difference between Shallow Copy and Deep Copy in Python? Explain with examples.

i.Shallow Copy

A shallow copy creates a new object, but doesn’t recursively copy nested objects — instead, 
it copies references to them. So, changes to nested mutable objects in the copy affect the original.

ii.Deep Copy

A deep copy creates a new object and recursively copies all nested objects, building a completely independent duplicate. 
Changes to nested objects in the copy do not affect the original.

