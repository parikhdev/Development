'''Task 4: List comprehensions and dict comprehensions — write 5 of each
Your task:
Write 5 list comprehensions and 5 dict comprehensions. Make them varied — use at least 2 with a condition (if). They can be simple, just make them different from each other.'''

# # List Conversion
# List1 = [1,2,3,4,5,['Python', 'tuple', True],7, {1: 'Python', 2: 'Neural Networks'}]
# List2 = [0,'Postgres', 9.8, -0.6, True, {"Gradient", "descent"}]
# tuple = (1,3,5,6.9, False, ("Python", "Java"), {"ML", "DL"})
# List3 = list(tuple)
# set = {"Embedding", False, 6, 9.8, (True, False)}
# List4 = list(set)
# List5 = ["List"] * len(List2)
# print(List1, List2, List3, List4, List5, sep = "\n")

# # Dictionary Conversion
# L1 = [["python",100], ["Rag", 99], ("Semantic Search", 98)]
# dict1 = dict(L1)
# T1 = (["Pandas", 80], ("JavaScript", 50))
# dict2 = dict(T1)
# S1 = {("Regression", "Linear"), ("SVM", "Vector")}
# dict3 = dict(S1)
# L2 = [["DL", {"Backpropogation", "FeedForward", "ActivationFunction"}], ["ML", "ReinforcementLearning"]]
# dict4 = dict(L2)
# dict5 = {"AI": {"DL":{"Backpropogation", "FeedForward"}},
#          "ML": {"Supervised", "Unsupervised"}}
# print(dict1, dict2, dict3, dict4, dict5, sep = "\n")

#List Comprehension
a =[i for i in range(5) if i%2 == 0]
print(a)

nums = [2,4,6,8]
b = [i//2 for i in nums]
print(b)

c = [i**2 for i in nums]
print(c)

d = [(i+1,x) for i, x in enumerate(nums)]
print(d)

e = [[x,x**2] for x in range(5)]
print(e)

#Dict Comprehension 
D1 = {x:i for i, x in enumerate(nums)}
print(D1)

country = ["India", "USA", "Russia", "Ukraine"]
capital = ["Delhi", "NewYork", "Moscow", "Kyiv"]
D2 = {count:cap for count,cap in zip(country,capital)}
print(D2)

D3 = {x:x**2 for x in nums}
print(D3)

D4 = {x+1:x+101 for x in range(5)}
print(D4)

D5 = {x: {i:x} for i, x in enumerate(nums)}
print(D5)