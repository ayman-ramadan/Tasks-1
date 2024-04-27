#Question_1
Friends = ['Ayman','Mahomud','Ali','Medo','Yoeel']
print(Friends[0]) #method_1
print(Friends[-len(Friends)]) #method_2

print(Friends[-1]) #method_1
print(Friends[len(Friends)-1]) #method_2
'''
Ayman
Ayman
Yoeel
Yoeel
'''
#Question_2
odd_names = ", ".join(Friends[::2])
print(odd_names)
even_names = ", ".join(Friends[1::2])
print(even_names)
'''
Ayman, Ali, Yoeel
Mahomud, Medo
'''
#Question_3
# Print names 2, 3, 4
names= ", ".join(Friends[1:4]) + ","
print(names)

# Print last and second names
names2 = Friends[-2] + ", " + Friends[-1]
print(names2)
'''
Mahomud, Ali, Medo,
Medo, Yoeel
'''
#Question_4
Friends[-2:] = ["Elzero", "Elzero"]
print(Friends)
'''
['Ayman', 'Mahomud', 'Ali', 'Elzero', 'Elzero']
'''
#Question_5
Friends.insert(0,'Alaa')
print(Friends)
Friends.append("Bebo")
print(Friends)
'''
['Alaa', 'Ayman', 'Mahomud', 'Ali', 'Elzero', 'Elzero']
['Alaa', 'Ayman', 'Mahomud', 'Ali', 'Elzero', 'Elzero', 'Bebo']
'''
#Question_6
del Friends[:2]
print(Friends)
del Friends[-1]
print(Friends)
'''
['Mahomud', 'Ali', 'Elzero', 'Elzero', 'Bebo']
['Mahomud', 'Ali', 'Elzero', 'Elzero']
'''
#Question_7
Employees = ['Mahrous','Donatello']
School = ['Naroto','Magdy']
Friends.extend(Employees)
Friends.extend(School)
print(Friends)
'''
['Mahomud', 'Ali', 'Elzero', 'Elzero', 'Mahrous', 'Donatello', 'Naroto', 'Magdy']
'''
#Question_8
Sorted_List = sorted(Friends)
print(Sorted_List)
Reversed_List = sorted(Friends, reverse=True)
print(Reversed_List)
'''
['Ali', 'Donatello', 'Elzero', 'Elzero', 'Magdy', 'Mahomud', 'Mahrous', 'Naroto']
['Naroto', 'Mahrous', 'Mahomud', 'Magdy', 'Elzero', 'Elzero', 'Donatello', 'Ali']
'''
#Question_9
print(len(Friends)) # 8

#Question_10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0]) #Django
print(technologies[-1][-1]) #Web
#----------------------------------------------------------------------------------------------------------------------------------------
#Question_1
name = 'Ayman',
print(name[0])
print(type(name))
'''
Ayman
<class 'tuple'>
'''
#Question_2
friends = ('Osama','Ali','Mahmoud')
updated_friends = list(friends)
updated_friends[0] = "Elzero"
friends = tuple(updated_friends)
print(friends)
print(type(friends))
print(len(friends), "Elements")
'''
('Elzero', 'Ali', 'Mahmoud')
<class 'tuple'>
3 Elements
'''
#Question_3
nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(len(nums_and_letters_one), "Elements")
'''
(1, 2, 3, 'A', 'B', 'C')
6 Elements
'''
#Question_4
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(a)
print(b)
print(c)
'''
1
2
4
'''
#------------------------------------------------------------------------------------------------------------------------------------------
#Question_1
my_list2 = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list2))
print(unique_list)
print(type(unique_list))
print(*unique_list[:-1],sep=',')
'''
[1, 2, 3, 4, 5]
<class 'list'>
1,2,3,4
'''
#Question_2
nums2 = {1, 2, 3}
letters2 = {"A", "B", "C"}
merged_set_1 = nums2.union(letters2)
print(merged_set_1)
merged_set_2 = nums2 | letters2
print(merged_set_2)
merged_set_4 = nums2.copy()
merged_set_4.update(letters2)
print(merged_set_4)
'''
{1, 2, 3, 'C', 'B', 'A'}
{1, 2, 3, 'C', 'B', 'A'}
{1, 2, 3, 'C', 'B', 'A'}
'''
#Question_3
my_set3 = {1, 2, 3}
print(my_set3)
my_set3.clear()
print(my_set3)
my_set3.add("B")
my_set3.add("A")
print(my_set3)
my_set3.discard("C")
'''
{1, 2, 3}
set()
{'A', 'B'}
'''
#Question_4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
result = set_one.issubset(set_two)
print(result) #True

#Question_5
Programming = {
    "HTML": 90,
    "CSS": 80,
    "Python": 30
}

print(f'HTML Progress Is {Programming["HTML"]}%')
print(f'CSS Progress Is {Programming["CSS"]}%')
print(f'Python Progress Is {Programming["Python"]}%')
Programming["AI"] = 20
print(f'AI Progress Is {Programming["AI"]}%')
'''
HTML Progress Is 90%
CSS Progress Is 80%
Python Progress Is 30%
AI Progress Is 20%
'''
