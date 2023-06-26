print("Enter File's Name: ", end="")
filename = input()

filehandle = open(filename, "r")
content = filehandle.read()
filehandle.close()

print("Enter text to search for: ", end="")
text = input()
print("Enter text to replace with: ", end="")
replace = input()

oldcontent = content

if text in content:
    content = content.replace(text, replace)
    filehandle = open(filename, "w")
    filehandle.write(content)
    filehandle.close()
    print("\nThe text is replaced successfully!")
    print("\n-------Old Content-------")
    print(oldcontent)
    print("\n------New Content-------")
    print(content)
else:
    print("\nNot Found!")
