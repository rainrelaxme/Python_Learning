# 学习类：一种对量和合集，通过此类，可以代表所有的同种对象，并包含共有的信息

class Dog:
    """一次模拟小狗的简单尝试"""
    """狗有两个属性，两个动作"""

    def __init__(self, name, age):
        """初始化属性name和age。"""
        self.name = name  # 可供所有方法使用，并称之为属性
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

"""9-1 餐馆 ：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。创建一个名
为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
9-2 三家餐馆 ：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
"""


class Restaurant:
    """餐馆拥有两个状态，两个方法"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐馆信息"""
        print(f"{self.restaurant_name} have {self.cuisine_type}.")

    def open_restaurant(self):
        """正在营业"""
        print(f"{self.restaurant_name} is opening!")


my_restaurant = Restaurant("和平饭店", "川菜")
print(f"My restaurant's name is {my_restaurant.restaurant_name}")
print(f"My restaurant's cuisine_type is {my_restaurant.cuisine_type}")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


# 汽车信息描述，包含年、品牌、型号、里程；包含方法：读表，更新表，里程叠加；
class Car:
    """汽车信息描述，包含年、品牌、型号、里程；包含方法：读表，更新表，里程叠加；"""

    def __init__(self, make, model, year):
        """属性：品牌、型号、款式"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()  # 首字母大写

    def read_odometer(self):
        """打印汽车的里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """更新里程表,禁止回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """里程表增加指定的量，禁止回调"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('Porsche', 'Panamera', 2022)
print(my_new_car.get_descriptive_name())
print(my_new_car.model)
print(my_new_car.odometer_reading)

my_use_car = Car('Volkswagen', 'beetle', 1938)
print(my_use_car.get_descriptive_name())

my_use_car.update_odometer(10000)
my_use_car.read_odometer()

my_use_car.increment_odometer(1000)
my_use_car.read_odometer()

"""9-5 尝试登录次数 ：在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。编写一个名为increment_login_attempts() 的方法，
它将属性login_attempts 的值加1。再编写一个名为reset_login_attempts() 的方法，它将属性login_attempts 的值重置为0。
根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。打印属性login_attempts 的值，确认它被正确地递增；然后，调用方
法reset_login_attempts() ，并再次打印属性login_attempts 的值，确认它被重置为0。"""


class User:
    """记录登录尝试的次数"""

    def __init__(self, name):
        """登录次数"""
        self.name = name
        self.login_attempts = 0

    def get_login_times(self):
        """打印目前登录尝试次数"""
        if self.login_attempts <= 4:
            print(f"Now {self.name.title()} have attempted to login in system for {self.login_attempts}.")
        else:
            print(f"{self.name}'s attempt has exceeded the limit, please reset it and try again!")
            return "error"

    def increment_login_attempts(self):
        """增加尝试次数,超过5次会提示尝试过多"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置登录次数"""
        self.login_attempts = 0
        print("You have reset successfully!")


# 此段错误，并未实现想要的功能即自动叠加并超出限制后重置
# my_login = User('shawn')
# while my_login.login_attempts() < 7:
#     my_login.increment_login_attempts()
#     my_login.get_login_times()
#     if my_login.get_login_times() == "error":
#         my_login.reset_login_attempts()
#     else:
#         continue

# car类
class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性，再初始化电动汽车的独特属性"""
        super().__init__(make, model, year)
        # self.battery = 100  #添加新的属性，特有属性
        self.battery = Battery()    #调用实例


my_tesla = ElectricCar('tesla', 'model 3', 2022)

print(my_tesla.get_descriptive_name())
print(my_tesla.battery.battery_size)
my_tesla.battery.describe_battery()
