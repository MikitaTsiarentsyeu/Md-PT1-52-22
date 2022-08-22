# import module2 as mdl2

# from module2 import print_global_var, global_var as gv

global_var = "10"

from module2 import *

# print(mdl2.global_var)

# mdl2.print_global_var()

# mdl2.write_to_file("test.txt", "some info from new program")

print(global_var)

print_global_var()
