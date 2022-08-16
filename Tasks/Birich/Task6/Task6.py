import itertools as its

gen_fizz = its.cycle([""] * 2 + ["Fizz"])
gen_buzz = its.cycle([""] * 4 + ["Buzz"])

fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(gen_fizz, gen_buzz))
result = (word or num for word, num in zip(fizzes_buzzes, its.count(start=1)))

for elem in its.islice(result, 100):
    print(elem)
