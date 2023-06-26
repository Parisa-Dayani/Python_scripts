totContent = ""
print("Enter the Name of File: ")
fileName = str(input())
fileHandle = open(fileName, "r")

for content in fileHandle:
    newContent = content.title()
    totContent = totContent + newContent

fileHandle.close()
fileHandle = open(fileName, "w")
fileHandle.write(totContent)

print("All Words Capitalized Successfully!")
fileHandle.close()
