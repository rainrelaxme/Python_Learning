# Python-Learning
*Rainrelaxme's learn python record*

## 命名规范
（公有/外部成员）（私有/内部成员前面加“_”）

| 类型               |           示例            |
|:-----------------|:-----------------------:|
| 项目（project）      |       My-Project        |
| 文件夹（folder）      |        my_folder        |
| 模块（module）       |  my_naming_convention   |
| 包（package）       |  my_naming_convention   |
| 类（class）         |   MyNamingConvention    |
| 异常（exception）    |   MyNamingConvention    |
| 函数（function）     | my_naming_convention()  |
| 全局/类常量（constant） |  MY_NAMING_CONVENTION   |
| 全局/类变量（variable） |  my_naming_convention   |

## 代码格式
* 先引用标准库
* 空两行引用自己写的模块
* 类之间空两行，函数之间空一行，执行空两行

## 启动虚拟环境的方法
##### 直接启动下层文件夹下的activate文件
  * linux
  ```
  source ll_env/bin/activate
  ```
  * windows
  ```
  ll_env/Scripts/activate
  ```


## 测试用例的断言方法有以下几种
|           方法            |      用途       |
|:-----------------------:|:-------------:|
|    assertEqual(a, b)    |   核实 a == b   |
|  assertNotEqual(a, b)   |   核实 a != b   |
|      assertTrue(x)      |   核实x为True    |
|     assertFalse(x)      |   核实x为True    |
|  assertIn(item, list)   | 核实item在list中  |
| assertNotIn(item, list) | 核实item不在list中 |  


## [关于随机数](https://blog.csdn.net/x_9992/article/details/122402549)
需要导入  *import random*
* 随机整数
  1. *random.randint(a, b)*  
     * 包含上下限[a,b]
  2. *random.randrange([start], end[, step])*  
     * 包含下限[a,b)
* 随机浮点型
  1. *random.random()*
     * 0-1之间的随机浮点型[0, 1.0)  
  2. *random.uniform(a, b)*
     * 随机浮点型[a, b]或[b, a],无论什么顺讯均可  
* 随机从序列中选取字符
  1. *random.choice(sequence)*
     * 从序列中随机选取，包含list, tuple, string

## [关于正则表达式](https://c.runoob.com/front-end/854/)
|     方法     |         用途          |
|:----------:|:-------------------:|
|     .      |     除换行符以外的所有字符     |
|     $      |        字符串结尾        |
|  \d,\w,\s  |     匹配数字、字符、空格      |
|  \D,\W,\S  |    匹配非数字、非字符、非空格    |
|   [abc]    |  匹配 a、b 或 c 中的一个字母  |
|   [a-z]    |   匹配 a 到 z 中的一个字母   |  
|   [^abc]   | 匹配除了 a、b 或 c 中的其他字母 |  
| aa&#124;bb |     匹配 aa 或 bb      |  
|     ?      |     匹配 0 次或 1 次     |  
|     *      |      匹配 0 次或多次      |  
|     +      |      匹配 1 次或多次      |  
|    {n}     |        匹配 n次        |  
|    {n,}    |       匹配 n次以上       |  
|   {m,n}    |   最少 m 次，最多 n 次匹配   |  
|     +      |      匹配 1 次或多次      |  
|     +      |      匹配 1 次或多次      |  




[用markdown写下的md文档](https://blog.csdn.net/weixin_42454243/article/details/125147785)