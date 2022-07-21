from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c++'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")


my_favorite_languages = {}

my_favorite_languages['jen'] = 'python'
my_favorite_languages['sarah'] = 'c++'
my_favorite_languages['edward'] = 'ruby'
my_favorite_languages['phil'] = 'ruby'

print(my_favorite_languages)