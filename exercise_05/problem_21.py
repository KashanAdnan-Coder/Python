# 3. consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

lists = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']

for list in lists:
    if len(list) > 5:
        print(f"The {list} is the word that is longer than 5!")