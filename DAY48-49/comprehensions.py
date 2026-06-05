# #list

result = [x**2 for x in range(10)]
print(result)

# #set
result_two = {x for x in range(10)}
print(result_two)

#dict
result_three = {k: v for k, v in [(1,"Gerkaa")]}
print(result_three)

class A:
    def B(self):
        return 4 + 5

    def C(self, B):
        return B + 5

    def G(self, C):
        return C * 2

aa = A()
b = aa.B()
c = aa.C(b)
g = aa.G(c)
print(g)

# zip
keys = [1,2,3,4]
values = ['gerka', 'andrew', 'leonid', 'edgar']
keys_and_values = zip(keys, values)
print(dict(keys_and_values))
new = {k: v for k, v in zip(keys, values)}
print(new)

# enumerate
lst = ['g','g','g']
for i in enumerate(lst):
    print(i)

# map
nums = ["1", "2", "3"]

result = list(map(float, nums))
print(result)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_nums = [x*3 for x in nums if x % 2 == 0]
print(new_nums)

# Dict comprehension
words = ["hi", "cat", "python", "go", "django", "ai"]
new_dict = {k: v for k, v in zip(words, [len(x) for x in words]) if len(k) > 3}
print(new_dict)

names  = ["Alice", "Bob", "German", "Andrew"]
grades = [5, 2, 4, 3]

new_dict = {k: v for k, v in zip(names, grades) if v > 3}
print(new_dict)

#lambda
add = lambda x: [i for i in range(x)]
print(add(10))

#yield
def func_yield():
    yield from range(10)
gen = func_yield()
print(next(gen))
