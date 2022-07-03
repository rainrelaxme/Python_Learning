# -*- coding:utf-8 -*-
# 学习函数，学习手册为《python编程，从入门到实践》

# 最简单的函数输出
def greet_user(username):
    "显示简单的问候语"
    print(f"Hello,{username.title()}")


greet_user("shawn")


# 函数调用
def describe_pet_1(animal_type: object = 'dog', pet_name='willie') -> object:  # object是pycharm加上的
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")  # title()可以使首字母大写


describe_pet_1('hamster', 'harry')
# 多次调用
describe_pet_1('dog', 'willie')
# 关键词实参调用,可以无序调用
describe_pet_1(pet_name='shill', animal_type='cat')


# 使用函数默认值
# describe_pet_1('willie')   #调用错误，调用默认值时，需要把无默认值的参数调整到前面，使其按顺序调用


# 返回值return
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 让实参变成可选的
def get_formatted_name_2(first_name, last_name, middle_name=''):
    """返回整洁的姓名，可以选填中间名"""
    if middle_name:
        # 非空字符串为true，空字符串为false
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


basketball_player_1 = get_formatted_name_2('Kobe', 'Bryant', 'Bean')
print(basketball_player_1)
basketball_player_2 = get_formatted_name_2('lebron', 'james')
print(basketball_player_2)


# 返回字典
def build_person(first_name, last_name, age=None):  # None和‘’一样表示占位，条件判断中为false
    """返回一个字点，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


basketball_player_3 = build_person('kobe', 'bryant', 27)
print(basketball_player_3)

# 结合使用函数和while循环
while True:
    print("\n请输入您的姓名：\n输入q退出")

    f_name = input("First name:")
    if f_name == "q":
        break
    l_name = input("Last name:")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


# 练习8-7 专辑 ：编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。 给函数make_album()
# 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
# 8-8 用户的专辑：在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函数make_album() ，并将创建的字典打印出来。在这个while 循环中，务必要提供退出途径。
def make_album(artist_name, album_name, time=None):
    """返回歌手的名称"""
    album = {'artist': artist_name, 'album': album_name}
    if time:
        album['time'] = time
    return album


while True:
    # 应可以改进成一次返回所有输入的专辑信息
    print("\n请输入歌手及专辑信息（输入q退出）:")
    new_artist = input("artist:")
    if new_artist == 'q':
        break
    new_album = input("album:")
    if new_album == 'q':
        break
    album_time = input("album time:")
    if album_time == 'q':
        break
    album = make_album(new_artist, new_album, album_time)
    print(f"\n{album}")


# 传递列表
def greet_user_2(names):
    """向列表中的每位用户发出问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_user_2(usernames)
