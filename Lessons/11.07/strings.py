'my "test" string'
"my 'test' string"

'''my 
"test" 
string'''

x = """my
'test'
string"""

y = 'my\n"test"\nstring'

print(x)
print(y)
print(x == y)
print("'" == '"')

s = "my very long string"
print(len(s))

print(len('\n'))

print(s[0], s[1], s[2], s[3], s[4])
print(s[len(s)-1])
print(s[-1], s[-2], s[-3], s[-4])
print(s[-len(s)])

# s[len(s)] error

print(s[0:7])
print(s[0:2])
print(s[3:-3])

print(s[:7])
print(s[3:])

print(s[3:-3:2])
print(s[::400])
print(s[::-1])


print('s' in s)
print('long' in s)
print('test' in s)

print(s.find('s'))
print(s[s.find('s')])

print(s.find('y'))
print(s[s.find('y')])

print(s.find('very'))
print(s[s.find('very')])

print(s.find('very!!!'))

x = s.replace(" ", "-").replace("m", "M").replace("very", "not so")
print(x)
print(s)

print(s.split())
print(x.split('-'))
print(x.split('not so'))
print(x.split('s'))

# print(set(s))

values = x.split('-')
print("_".join(values))
print(set(s))
print("".join(set(s)))

print("!!!test!!!".strip("!"))
print("   test      ".strip(" "))

print("TeSt StRiNg".upper())
print("TeSt StRiNg".lower())

print("test" == "tesr")

print("test number 1, " + "test number 2")
print("test str\n" * 8)

c, d, p = "cat", "dog", "parrot"
s = "a " + c + ", a " + d + ", and a " + p #very bad approach, is not recommended to be uset
"a cat"
"a cat, a"
"a cat, a dog"
"a cat, a dog, and a "
"a cat, a dog, and a parrot"
print(s)

s = "a {}, a {}, and a {}".format(c, d, p)
print(s)

s = "a {}, a {}, and a {}".format("dog", "parrot", "cat")
print(s)
s = "a {2}, a {0}, and a {1}".format("dog", "parrot", "cat")
print(s)
s = "a {c}, a {d}, and a {p}".format(d="dog", p="parrot", c="cat")
print(s)

print(f"a {c}, a {d}, and a {p}")
print(f"the result is {25/12.5}")