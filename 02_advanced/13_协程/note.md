# 参考资料
-资料
  - https://blog.csdn.net/andybegin/article/details/77884645
  - http://python.jobbole.com/86481/
  - http://python.jobbole.com/87310/
  - https://segmentfault.com/a/1190000009781688

# 迭代器
- 直接作用于for循环的叫可迭代对象,Iterable
- 不但可以作用于for循环,还可以被next调用的,叫Itrator
- 可以用isinstance判断

      from collections import Iterable
      l = [1,2,3,4]

      isinstance(l, Iterable)

      from collections import Iterator
      isinstance((x for x in range(10)), Iterator)

- iterable和Iterator的关系,可以通过iter函数运算

      isinstance(iter('abc'), Iterator)

# ----省略部分，和jupyter notebook内容有重复

# asyncio
- python3.4开始引入的标准库,内置了对移步io的支持
- asyncio本身是一个消息循环,
- 步骤
    - 创建消息循环
    - 把协程导入
    - 关闭
- 案例[08]
- 案例[09]-两个tasks
- 案例[v10]-得到多个网站
