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
bank_name="中国工商银行账户管理系统"
def bank_adduser(username,password,country,province,street,door,money,account):
    if username in bank:
        return 2
    if len(bank)>=100:
        return 3
    bank[username]={
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "account":account}
    print(bank[username])
    return 1


def useradd():
    username=input("用户名")
    password=input("密码")
    country=input("国家")
    province=input("省份")
    street=input("街道")
    door=input("门户")
    account=random.randint(10000000,99999999)
    money=0
    a=bank_adduser(username,password,country,province,street,door,account,money)
    if a == 1:
        print("成功")
        info= '''
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
        print(info % (password,country,province,street,door,account,money,bank_name))
    elif a==2:
        print("用户已存在")
    elif a==3:
        print("用户库已满")


def cun_money():
    usename=input("请输入账号")
    b=input("请输入密码")
    if usename in bank:
        if b !=bank[usename]["password"]:
            print("密码错误")
        else:
            cun=int(input("输入存款金额"))
            bank[usename]['money']=cun
            print("余额为:",cun)
    else:
        print("用户名不存在")
def qu_money():
    username=input("请输入账号")
    b=input("请输入密码")
    if username in bank:
        if b !=bank[username]["password"]:
            print("密码错误")
        else:
            qu=int(input("输入取款金额"))
        if bank[username]['money']<qu:
            print("余额不足")
        elif bank[username]['money']>=qu:
            M=bank[username]['money']=bank[username]['money']-qu
            print("余额为:",M)
    else:
        print("账号不存在")
def zhuan():
    usename=input("输入转出账号：")
    input("输入密码：")
    if usename in bank:
        print("转入账号存在")
        money=int(input("输入转账金额:"))
        if bank[usename]['money']>=money:
            print("转账成功")
            c=bank[usename]['money']=bank[usename]['money']-money
            bank[usename]['money']=bank[usename]['money']+money
            print("余额为：",c)
        else:
            print("余额不足")
    else:
        print("转入账号不存在")
def cha():
    usename=input("输入账号")
    password=input("输入密码")
    if usename in bank:
        if password!=bank[usename]['password']:
            print("密码错误")
        else:
            print("查询成功")
            info  = '''
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
            print(info %(usename,password,bank[usename]['country'],bank[usename]['provice'],bank[usename]['street'],bank[usename]['door'],bank[usename]['money']))
    else:
        print("账号不存在")
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















