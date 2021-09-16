start = (input("是否开始游戏"))
if start == "1":
     print("请开始")
     a = 0
     sum = 0
     a = int(input("余额不足，请输入充值金额"))
     if a < 500:
         sum = a + (a * 0.1)
         print("充值成功", "当前余额为", sum)
     else:
         sum = a + (a * 0.2)
         print("充值成功", "当前余额为", sum)
     print("余额", a)
     # b=a

     i = 0
     # 快速生成随机数模块、包裹。
     import random
     # 范围
     ran = random.randint(0, 5)
     print(ran)
     while a >= 500 and i < 5:
         num = int(input("请输入一个数字"))
         if num == ran:
             print("恭喜你，猜对了！！","当前余额为",sum)
             sum = sum + 5000
             break
         elif num >= ran:
             print("大了")
             i = i + 1
             a = a - 500
             print("余额为", a, "剩余次数", 5 - i)
         elif num <= (ran):
             print("这都猜不对，真菜")
             i = i + 1
             a = a - 500
             print("余额为:", a, "剩余次数", 5 - i)
elif start == "q":
     print("游戏已结束")
     pass