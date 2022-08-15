def prepare():
    print("STARTING A NEW PIZZA")
    print("preparing a base")
    print("choosing a sauce")

def add_ingridient(ingridient):
    print(f"adding {ingridient}")

def grind_cheese():
    print("grinding cheese")

def bake():
    print("baking the pizza")

def done():
    print("slicing")
    print("boxing")
    print("DONE!")

# def make_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake()
#     done()

# def make_double_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake()
#     done()

# def make_4_chheses():
#     prepare()
#     add_ingridient("chedder")
#     add_ingridient("maasdam")
#     add_ingridient("cordon-bleu")
#     add_ingridient("suluguni")
#     grind_cheese()
#     bake()
#     done()

def pizza_factory(ingridients):
    def factory_method():
        prepare()
        for i in ingridients:
            add_ingridient(i)
        grind_cheese()
        bake()
        done()
    return factory_method

make_pepperoni = pizza_factory(["pepperoni"])
make_double_pepperoni = pizza_factory(["pepperoni", "pepperoni"])
make_4_chheses = pizza_factory(["chedder", "maasdam", "cordon-blue", "suluguni"])

make_pepperoni()
print("-----------------------------------------------------------")
make_double_pepperoni()
print("-----------------------------------------------------------")
make_4_chheses()