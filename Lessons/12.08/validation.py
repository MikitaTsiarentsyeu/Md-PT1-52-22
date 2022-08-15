
def validate_number(control_value:int, user_value:str):
    try:
        x = int(user_value)

        if x < control_value:
            raise RuntimeError(f"The value is lower then {control_value}")
    except ValueError:
        return "It was not a number"
    except RuntimeError as e:
        return str(e)

# res = validate_number(100, "111")
# print(res)

while True:
    x = input("Enter your value greater then 100:\n")
    validation_res = validate_number(100, x)
    if validation_res:
        print(validation_res)
        continue
    else:
        break

print(x)


