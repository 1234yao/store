from threading import Thread
import time

eggs = 0
# 蛋挞盒子

class chef(Thread):
    chefname = ''
    count = 0
    def run(self) -> None:
        global eggs
        while True:
            if eggs < 500:
                eggs = eggs + 1
                print('盒子里有', eggs, '个蛋挞')
                time.sleep(0.1)
                self.count += 1
            elif eggs == 500:
                time.sleep(3)
                print(self.chefname, "做了", self.count, '蛋挞')
                time.sleep(0.1)
                break



class shopper (Thread):
    shoppername = ''
    count1 = 0
    money = 500
    def run(self) -> None:
        global eggs
        while True:
            if self.money > 0:
                if eggs > 0:
                    eggs = eggs - 1
                    self.money -= 2
                    print(self.shoppername, '买了一个蛋挞')
                    print(self.shoppername, '还剩', self.money, '元')
                    time.sleep(0.1)
                    self.count1 += 1
                else:
                    time.sleep(3)
            else:
                print("买了", self.count1, '个蛋挞')
                print(self.shoppername,"买了",eggs)
                break


a1 = chef()
a2 = chef()
a3 = chef()
b1 = shopper()
b2 = shopper()
b3 = shopper()
b4 = shopper()
b5 = shopper()
b6 = shopper()

a1.chefname = '微微'
a2.chefname = '大大'
a3.chefname = '妞妞'


b1.shoppername = '赛罗'
b2.shoppername = '赛斯'
b3.shoppername = '赛马'
b4.shoppername = '赛脸'
b5.shoppername = '赛露'
b6.shoppername = '赛车'

a3.start()
a2.start()
a1.start()
b1.start()
b2.start()
b3.start()
b6.start()
b5.start()
b4.start()
