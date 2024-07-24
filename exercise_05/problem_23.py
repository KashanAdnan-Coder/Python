# 5. Write a program to display odd numbers only. odd number upto 100
# hint use for loop and range function

for num in range(0, 101):
    if num % 2 == 0:
        continue
    print(num)