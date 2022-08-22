global_var = [5]

def print_global_var():
    print(f"the value of the global_var from module2 is {global_var}")

def write_to_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)



if __name__ == "__main__":
    print("hello from module2")
    write_to_file("test.txt", "some very important things\n")
    print(__name__)
