numbers =  {"one" : 1, "two" : 2, "three" : 3,
            "four" : 4, "five" : 5, "six" : 6,
            "seven" : 7, "eight" : 8, "nine" : 9,
            "ten" : 10, "eleven" : 11, "twelve" : 12,
            "thirteen" : 13, "fourteen" : 14, "fifteen" : 15,
            "sixteen" : 16, "seventeen" : 17, "eighteen" : 8,
            "nineteen" : 19, "twenty" : 20}

numbers.update({"input_numbers" : "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split(" ")})

#switch to integers
numbers["input_numbers"] = [int(numbers.get(x)) for x in numbers["input_numbers"]]
print(numbers["input_numbers"])
print("________________________________________")

#without duplicates
numbers["input_numbers"] = set(numbers["input_numbers"])
print(numbers["input_numbers"])
print("________________________________________")

#ascending sorting
numbers["input_numbers"] = list(numbers["input_numbers"])
numbers["input_numbers"].sort()
print(numbers["input_numbers"])
print("________________________________________")

# the product of the first and second, the sum of the third and fourth, etc.
print([numbers["input_numbers"][x-2]+numbers["input_numbers"][x-1] if x%4 == 0 else 
numbers["input_numbers"][x-2]*numbers["input_numbers"][x-1] 
for x in range(2,len(numbers["input_numbers"])+1,2)])
print("________________________________________")

#sum of odd ones
print (sum([numbers["input_numbers"][x]for x in range(len(numbers["input_numbers"]))
if numbers["input_numbers"][x]%2 != 0]))
print("________________________________________")
   