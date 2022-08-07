'''from sys import argv
script, file_name = argv

txt = open(file_name)

print(f"I want to read {file_name}.")
print(txt.read())
'''


print("What file do you want to check?\nPlease input it:")
file_name2 = input("> ")
txt2 = open(file_name2)
print(txt2.read())
#txt2.close()