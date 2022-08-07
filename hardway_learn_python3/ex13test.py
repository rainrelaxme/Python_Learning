from sys import argv
script, firstname, secondname = argv
prompt = '> '

print("Please input your firstname", end = "")
firstname = input(prompt)

print("Please input your secondname", end = "")
secondname = input(prompt)

print("The script is called:", script)				#如何将该处与上面的文字描述合并，显得过于累赘
print("Your fistname is:", firstname)
print("Your secondname is:", secondname)
print("Your name is:", firstname+secondname)

