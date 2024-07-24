# task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# and store the updated content in user_email.txt
# run program three times with different name, title and link
# after running the program three times
# the file user_email.txt must have all three users content

f = open("user_email.txt", "r")

text = f.read()

print(text)

file_content = """
Hi *user*!

We've found the best article for you based on your interest: *title*
Please click *here* to open the article
"""

user_name = "Almira Adnan"
article_title = "The Ultimate Guide to Tasty Food"
here = "Here is the article"

updated_content = file_content.replace("*user*", user_name).replace("*title*", article_title).replace("*here*", here)

file = open("user_email.txt", "a")

text = file.write(updated_content)
f.close()
