# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."


while True:
    name = input("Enter a name (or type 'END' to stop): ")
    if name == 'END':
        break
    print(name)

print("I am done.")