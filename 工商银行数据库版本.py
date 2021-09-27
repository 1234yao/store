from DBUtils import update,select
import random
print("*************************************")
print("*    中国工商银行                     *")
print("*    账户管理系统                     *")
print("*        v1.0                       *")
print("*************************************")
print("*1开户                              *")
print("*2.存钱                              *")
print("*3.取钱                              *")
print("*4.转账                              *")
print("*5.查询                              *")
print("*6.bye！                             *")
print("**************************************")

bank={}
bank_name="中国工商银行"
def bank_adduser(username,account,password,country,province,street,door,money):
    sql = "select count(*) from 用户"
    param = []
    data = select(sql, param,mode='one')[0]
    if data>=100:
        return 3

    sql1 = "select * from 用户 where username = %s"
    param1 = [username]
    data = select(sql1,param1)
    if len(data) > 0 :#如果一个变量在容器内就运行代码
        return 2

    sql2 = "insert into 用户 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,username,password,country,province,street,door,money,bank_name]
    data = update(sql2,param2)
    return 1


def useradd():
    username=input("请输入您的用户名：")#局部变量
    password = input("请输入密码：")#print(bank['Frank']['password'])
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account=random.randint(10000000,99999999)
    money=0
    a=bank_adduser(username,account,password,country,province,street,door,money)
    if a == 1:
        print("添加用户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        sql = 'select money from 用户 where account= %s'
        param = [account]
        data = select(sql, param, mode='one')[0]
        print(data)
        print(info % (username, account, country, province, street, door, data, bank_name))
    elif a ==2:
        print("用户已存在，请勿重复添加！")
    elif a == 3:
        print("数据库已满")

def bank_saveMoney(account_save,save_money):
    if account_save not in bank:
        return False
    else:
        bank[account_save]["money"] = bank[account_save]["money"] + save_money
        return True
#存钱操作代码
def cun_money():
    account_money =  input("请输入您存钱的账号：")
    sql = "select * from 用户 where account = %s"
    param = [account_money]
    data = select(sql, param)
    if len(data) > 0:
        money = int(input("请输入你要存入的金额："))
        sql1 = 'update 用户 set money = money + %s where  account = %s'
        param1 = [money,account_money]
        update(sql1, param1)
        sql2 = 'select money from 用户 where account = %s'
        param2 = [account_money]
        data1 = select(sql2, param2,mode="one")[0]
        print("存款成功！当前余额：",data1)
    else:
        print("该用户不存在")


# # 存钱
# def cun_money():
#     sql="select * from 用户信息 where account = %s,'password'= %s"
#     account=input("请输入账号")
#     password=input("请输入密码")
#     param=[account,password]
#     data=select(sql,param)
#     if len(data) in bank:
#         print("账户存在")
#         if password !=bank[account][password]:
#             print("密码错误")
#         else:
#             cun=int(input("输入存款金额"))
#             sql1="update 用户信息 set money=%s where username=%s"
#             param1=[cun,account]
#             update(sql1,param1)
#             print("余额为：",cun)
#     else:
#         print("用户名不存在")
def qu_money():
    account=input("请输入您的账号")
    sql="select * from 用户 where account = %s"
    param=[account]
    date=select(sql,param)
    if len(date)>0:
        while True:
            password=int(input("请输入您的密码"))
            sql1="select password from 用户 where account = %s"
            param1=[account]
            data1=select(sql1,param1,mode='one')[0]
            if password ==data1:
                qu=int(input("请输入取款额度："))
                sql2 ='select money from 用户 where account = %s'
                param2=[account]
                data2=select(sql2,param2,mode='one')[0]
                if qu >data2:
                    print("余额不足啦，小子,还有",data2)
                    break
                else:
                    sql3='update  用户 set money = money - %s where account = %s'
                    param3=[qu,account]
                    update(sql3,param3)
                    sql4="select money from 用户 where account=%s"
                    param4=[account]
                    data3=select(sql4,param4,mode='one')[0]
                    print("取款成功，余额为：",data3)
                    break
            else:
                print("密码错误")
                break
    else:
        print("账户不存在")




def zhuan():
    a1 = input("请输入转账账号")
    sql="select * from 用户 where account = %s"
    param=[a1]
    data=select(sql,param)
    if len(data)>0:
        a2 = input("请输入收款账号")
        sql1="select * from 用户 where account = %s"
        param1=[a2]
        data1=select(sql1,param1)
        if len(data1) >0:
            password=int(input("请输入转账密码"))
            sql2="select password from 用户 where account =%s"
            param2=[a1]
            data2=select(sql2,param2,mode='one')[0]
            while True:
                if password==data2:
                    money=int(input("请输入转账金额"))
                    sql3="select money from 用户 where account = %s"
                    param3=[a1]
                    data3=select(sql3,param3,mode='one')[0]
                    if money>data3:
                        print("余额不足")
                        break
                    else:
                        sql4="update  用户  set money  = money -%s where account = %s"
                        param4=[money,a1]
                        update(sql4,param4)
                        sql5="select money from 用户 where account = %s"
                        param5=[a1]
                        data4=select(sql5,param5,mode='one')[0]
                        print("转账成功,余额为",data4)
                # sql5="update 用户 set money where account = %s"
                # pram5=[money,a1]
                        break
                else:
                    print("密码错误")
        else:
            print("账号不存在")
    else:
        print("账号不存在")

def cha():
    username = input("输入账号")
    sql="select * from 用户 where account = %s"
    param=[username]
    data=select(sql,param)
    if len(data)>0:
        password = int(input("输入密码"))
        sql1="select password from 用户 where account = %s"
        param1=[username]
        data1=select(sql1,param1,mode='one')[0]
        while True:
            if password==data1:
                sql2="select * from 用户 where account = %s"
                param2=[username]
                data2=select(sql2,param2)
                print(data2)
                break
            else:
                print("密码错误")
    else:
        print("账号不存在")
        info = '''
            ------------个人信息------------
             用户名:%s
              账号：%s
              密码：%s
              国籍：%s
              省份：%s
              街道：%s
              门牌号：%s
              余额：%s
              '''

        print(info % (bank[username]["username"], bank[username]["account"], bank[username]["country"], bank[username]["province"],
                          bank[username]["street"], bank[username]["door"], bank[username]["money"], bank_name))
while True:#永远循环
    begin = input("请选择业务")
    if begin == "1":
        useradd()
    elif begin == "2":
        print("存钱")
        cun_money()
    elif begin == "3":
        print("取钱")
        qu_money()
    elif begin == "4":
        print("转账")
        zhuan()
    elif begin == "5":
        print("查询")
        cha()
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")
        break

#
#
#
#
#
#
#
#
#
#
#
#
#
#
