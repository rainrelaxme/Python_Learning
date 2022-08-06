tabby_cat = '\t I"m tabbed in.'						#如果字符串中含有单引号，就使用双引号；反之类似
persian_cat = "I'm split\n on a line."
backslash_cat = "I'm \\a \\cat."

fat_cat ='''
I'll do a list:
\t* Cat food #face									
\t* Fishies
\t* Catnip\n\t* Grass'''							#如果使用"""或者'''则不用考虑内部是单引号还是双引号

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)