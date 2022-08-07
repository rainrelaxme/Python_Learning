'''
	猜数字游戏
        注：每局游戏最多只能猜五次，超过则自动退出
        1.随机产生一个0~100(包含0和100)的整数
        2.在while循环中：
            2.1 输入一个0~100的整数,input输入的是字符串
            2.2 转换为整数类型
            2.3 和正确的答案数字做对比
                2.3.1  猜测数字 大于 正确答案   输出猜大了
                2.3.2  猜测数字 小于 正确答案   输出猜小了
                2.3.3  猜测数字 等于 正确答案   输出猜对了  退出程序
'''

import random



guess = input("Please input your guess in (0~100)> ")

def Numguess(guess)

	answer = random.randint(0, 100)
	count = 0
	
	if guess == answer and count<=5:
		print("You won!")
		count +=1
	elif guess > answer:
		print("The number is bigger than right answer.")
		count +=1
	else:
		print("The number is shorter than right answer.")
		count +=1
