"""
#隐式覆盖，子类调用父类的函数
class Parent(object):
	def implicit(self):
		print("PARENT implicit()")
		
class Child(Parent):
	pass
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()
"""

"""
#显式覆盖，子类用自己的函数而不是父类中的
class Parent(object):
	
	def override(self):
		print("PARENT override()")
		
class Child(Parent):
	def override(self):
		print("CHILD override()")
		
dad = Parent()
son = Child()

dad.override()
son.override()
"""

"""
#super(子类，self）
class Parent(object):
	def altered(self):
		print("PARENT altered()")
		
class Child(Parent):
	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")
		
son = Child()
dad = Parent()

dad.altered()
son.altered()
"""


