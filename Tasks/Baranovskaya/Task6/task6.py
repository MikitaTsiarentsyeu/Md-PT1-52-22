# My solution:
for i in range(1, 101):
    s = ""
    if i % 3 == 0:
        s += "Fizz"
    if i % 5 == 0:
        s += "Buzz"
    if s == "":
        s += str(i)
    print(s)

# Solution I found on the internet: 
modulo_list = [
  (3,"Fizz"),
  (5,"Buzz")
]
 
for i in range(1, 101):
    print_string = ""
    for mod in modulo_list:
        if i % mod[0] == 0:
            print_string += mod[1]
     
    if print_string == "":
        print(i)
    else:
        print(print_string)