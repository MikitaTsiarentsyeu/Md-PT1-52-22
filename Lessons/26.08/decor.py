def do_twice(func):
    def wrapper(number):
        print("the first call:")
        func(number)
        print("the second call:")
        func(number)
    return wrapper

def comment_process(func):
    def wrapper(number):
        print("the process started")
        func(number)
        print("the process finished")
    return wrapper

def print_number_support(number):
    print(f"{number} - this is number")

@do_twice
def print_number_twice(number):
    print_number_support(number)

@comment_process
def print_number_comment(number):
    print_number_support(number)

# print_number(4444)
# print_number_four = do_twice(print_number_four)
# print_number_four = comment_process(print_number_four)
# print_number_four()