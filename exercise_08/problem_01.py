# create a text file and add the below content without quotation marks

f = open("text.txt" , "w")

text = f.write("""Hi *user*!

We've found the best article for you based on your interest: *title*
Please click *here* to open the article""")

f.close()
