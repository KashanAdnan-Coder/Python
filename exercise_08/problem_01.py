# create a text file and add the below content without quotation marsk

# task is to read the above file and update the placeholder i.e *user*, *title* and *here*

# f = open("text.txt" , "r")

# text = f.read()

# print(text)
# f.close()

with open("text.txt", 'r') as file:
    file_data = file.read()

file_data = file_data.replace('*user*', "Kashan")
file_data = file_data.replace('*title*', "HMTL")
file_data = file_data.replace('*here*', "Kashan is good boy")

with open("text.txt", 'w') as file:
    file.write(file_data)