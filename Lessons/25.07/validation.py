# the input format is "hh:mm"

while True:
    time_token = input("Please input the time if the hh:mm format:\n")

    if len(time_token) != 5:
        print("Incorrect length of the time string")
        continue

    if time_token[2] != ":":
        print("Incorrect input, the token lacks the : symbol")
        continue

    values = time_token.split(':')
    hours, minutes = values[0], values[1]

    if not (hours.isdigit() and minutes.isdigit()):
        print("Incorrect input, the hours and minutes values should be digits")
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 24 or minutes > 59:
        print("Incorrect input, the hours  should vary from 00 to 24 and the minutes should vary from 00 to 59")
        continue

    break

print(time_token)