#15. Write a Python function to create the HTML string with tags around the word(s).5
a = input("Enter the title :")
if len(a)>0:
    print("<h1>" + a + "</h1>")
else:
    print("Nothing to display")