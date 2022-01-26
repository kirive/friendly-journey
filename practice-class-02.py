# Create a file, returns error if file exists
fileNameInput = input("Enter a file name: ")
newFile = open(fileNameInput, "x")
print("File name " + fileNameInput + " has been created.")

# Write/Append to a file
fileTextInput = input("Enter any text: ")
newFile = open(fileNameInput, "a")
newFile.write(fileTextInput + "\n")
newFile.close()
print("Text has been entered into " + fileNameInput + ".")

# Delete a file
import os
os.remove(fileNameInput)
print("File " + fileNameInput + " has been deleted.")