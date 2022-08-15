print ("|=================================================|")
print ("|++++++++++This program is a text editor++++++++++|")
print ("|=================================================|")
input_choese = input("Please enter a string length.\
 The length of the string must be longer than 34 characters.\n")

position_read = 0
number_of_str = 0

#validation block
while True:
    if input_choese.isnumeric():
        input_choese = int(input_choese)
        if input_choese < 35:
            print ("Incorrect input. The number must be greater than 34")
            input_choese = input("Please enter a string length.\
 The length of the string must be longer than 34 characters.\n")
            continue
        else:
            number_of_str = int(input_choese)
            break        
    else:
        print ("Incorrect input. Must be a number")
        input_choese = input("Please enter a string length.\
 The length of the string must be longer than 34 characters.\n")
        continue



input_file = open("text.txt","r")
output_file = open ("result.txt","w")
temp_text = input_file.read(number_of_str)



while len(temp_text):

    if temp_text.find("\n") == 0:
        temp_text = temp_text[1:len(temp_text)]
        position_read += 1

     
    if temp_text.find("вЂ™") != -1 and temp_text.find("вЂњ") != -1:
        number_of_str = input_choese + 4 
    elif temp_text.find("вЂ™") != -1 and temp_text.find("вЂќ") != -1:
        number_of_str = input_choese + 4 
    elif temp_text.find("вЂњ") != -1 and temp_text.find("вЂќ") != -1:
        number_of_str = input_choese + 4 
    elif temp_text.find("вЂ™") != -1 or temp_text.find("вЂњ") != -1 or temp_text.find("вЂќ") != -1:
        number_of_str = input_choese + 2
    
    else :
        number_of_str = input_choese 
        
    if temp_text.endswith("."):
        output_file.write(temp_text+'\n')
        position_read += number_of_str+1
        
    elif temp_text.find(".") != -1 and temp_text.find("\n") != -1:
        index_position = temp_text.find(".")
        temp_text = temp_text[0:index_position+1]
        output_file.write(temp_text+'\n')
        position_read += index_position+2

    elif temp_text[len(temp_text)-1] != " " and temp_text[len(temp_text)-1] != ".":
        input_file.seek(position_read)
        temp_text = input_file.read(number_of_str+1)
        if temp_text[len(temp_text)-1] != " ":
            input_file.seek(position_read)
            temp_text = input_file.read(number_of_str)
            index_position = temp_text.rfind(" ")
            temp_text = temp_text[0:index_position]
            number_space = number_of_str - index_position
            temp_text_space = temp_text.split(" ")
            number_space = number_space + len(temp_text_space)-1
            if number_space % (len(temp_text_space)-1) == 0:
                i = number_space / (len(temp_text_space)-1)
                strd = " "*int(i)
                temp_text = strd.join(temp_text_space)
            else :   
                k_position = 1   
                k = k_position
                for i in range(number_space):
                    temp_text_space.insert(k," ")
                    k += 2 
                    if k >= len(temp_text_space):
                        k_position += 1
                        k = k_position
                temp_text = "".join(temp_text_space)                    
            output_file.write(temp_text+'\n')
            position_read += index_position+1

        elif temp_text[len(temp_text)-1] == " ":
            input_file.seek(position_read)
            temp_text = input_file.read(number_of_str)
            output_file.write(temp_text+'\n')
            position_read += (number_of_str+1)
    elif temp_text.endswith(" "):
        index_position = temp_text.rfind(" ")
        temp_text = temp_text[0:index_position]
        number_space = number_of_str - index_position
        temp_text_space = temp_text.split(" ")
        number_space = number_space + len(temp_text_space)-1

        if number_space % (len(temp_text_space)-1) == 0:
            i = number_space / (len(temp_text_space)-1)
            strd = " "*int(i)
            temp_text = strd.join(temp_text_space)
        else :   
            k_position = 1   
            k = k_position
            for i in range(number_space):
                temp_text_space.insert(k," ")
                k += 2 
                if k >= len(temp_text_space):
                    k_position += 1
                    k = k_position
            temp_text = "".join(temp_text_space)

        
        output_file.write(temp_text+'\n')
        position_read += index_position+1
    
    input_file.seek(position_read)
    number_of_str = input_choese
    temp_text = input_file.read(number_of_str)

input_file.close()
output_file.close()








