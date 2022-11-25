# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第17章 API使用

import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

# 将API响应存储在一个变量中,由于返回是json，使用json()存储，并用字典存储
response_dict = r.json()
print(response_dict.keys())
print("Total repositories: ", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print("Repositories returned: ", len(repo_dicts))

"""
# 研究前10个仓库
i = 0
repo_dict_10 = []
while i < 10:
    repo_dict_10.append(repo_dicts[i])
    i += 1

print("\nSelected information about each repository:")
for repo_dict in repo_dict_10:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
"""

# 自定义标签描述
names, plot_dicts = [], []
for repo_dict_2 in repo_dicts:
    names.append(repo_dict_2['name'])
    plot_dict = {
        'value': repo_dict_2['stargazers_count'],
        'label': repo_dict_2['description'],
        'xlink': repo_dict_2['html_url'],
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')