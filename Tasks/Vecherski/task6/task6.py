'''
the most beautiful and understandable solution in my opinion from the network, 
improved by me with the help of end in print =) . however, it is not the fastest.
'''
[print((i%3<1)*'Fizz'+(i%5<1)*'Buzz' or i, end=", ") for i in range(1, 101)]