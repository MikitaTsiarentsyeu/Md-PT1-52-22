test_val = 101
x = "the very important value"

def test_scope(x):
    # print(f"test_scope 1 - {test_val}")
    print(x)
    test_val = 202
    print(f"test_scope 2 - {test_val}")

def test_scope_2(x):
    print(x)

def test_global():
    global test_val
    print(f"test_global 1 - {test_val}")
    test_val = 303
    print(f"test_global 2 - {test_val}")


def outer_func():
    x = "outer value"
    def inner_func():
        nonlocal x
        x = "inner value"
        print(x)
        def more_inner_func():
            nonlocal x
            x = "more inner value"
            print(x)
        more_inner_func()
    inner_func()
    print(x)

# test_scope("x value")
# test_scope_2("another value")
# print(f"after test_scope - {test_val}")
# test_global()
# print(f"after test_global - {test_val}")

outer_func()