
#!/usr/bin/python
#-*-coding:utf-8-*-
import allure
import pytest

# 一、feature :标注测试用例是属于那一个模块的
@allure.feature("模块一")    #同一个测试用例下有多少模块
def test_1():
    pass

@allure.feature("模块一")
def test_2():
    assert 0<1

#二、 story：对一个测试用例的详细描述
@allure.feature("模块二")
@allure.story("这是一个很可爱的测试用例")
def test_3():
    assert 0>21344242

@allure.feature("模块二")
@allure.story("这是一个很美丽的测试用例")
def test_4():
    """
    这是对函数的参数、返回值的一个注释
    自我感觉优秀
    """
    # 测试用例的描述是通过函数的注释时来获取得到的
    assert  "你好"  == "china"

# 三、测试用力的优先级
"""
Blocker级别：阻塞中断缺陷（客户端程序无响应，无法执行下一步操作）
Critical级别：严重缺陷（ 功能点缺失）
Normal级别：普通级别
Minor级别：次要
Trivial级别：轻微
"""
# severity:标注测试用例的优先级
@allure.feature("模块三")
@allure.severity("blocker")
def test_5():
    assert 0==0

@allure.feature("模块三")
@allure.severity("critical")
def test_6():
    assert 0==0

@allure.feature("模块三")
@allure.severity("normal")
def test_7():
    assert 0==0

@allure.feature("模块三")
@allure.severity(" minor")
def test_8():
    assert 0==0

@allure.feature("模块三")
@allure.severity("trivial")
def test_9():
    assert 0==0

# 四、setp：记录测试用例中的一些步骤，日志代码可以通过setp记录到我们的报告中
# isinstance(参数一，参数二)判断数据类型的类，参数一和参数二是否为同一个类型
# 是的话----》True ，不是----》Flase
@allure.step("字符串相加：{0},{1}")
def str_add(str1,str2):
    if not isinstance(str1,str):
        return  f"{str1},不是字符串类型的"

    if not isinstance(str2,str):
        return  f"{str2},不是字符串类型的"
    return str1+str2
@allure.feature("模块四")
def test_10():
    str1="hello"
    str2="world"

    assert str_add(str1,str2)=="helloworld"
# 五、 issue和testcase
# 对issue和testcase生成一个网址
# issue：存放出现的bug问题、、testcase：存放测试用力的详细信息
@allure.step("字符串相加：{0}，{1}")
#测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    print('hello')
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2

@allure.feature("模块五")
@allure.issue("http://www.baidu.com")   #存放出现的bug问题
@allure.testcase("http://www.testlink.com")  #存放测试用力的详细信息
def test_case():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'