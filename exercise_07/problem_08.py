# consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

words = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']

for word in words:
    if len(word) > 5:
        print(word)


