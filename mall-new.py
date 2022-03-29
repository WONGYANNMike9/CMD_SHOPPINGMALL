
import pymysql.cursors
from pymysql import connect

class GUEST_OP(object):
    """顾客购物类"""
    def __init__(self):
        """连接数据库"""
        self.conn = connect(host='49.235.89.99',port=3306,user='remoteu1',password='190450',database='comp7640',cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def __del__(self):
        """关闭数据库"""
        self.cursor.close()
        self.conn.close()

    def execute_sql(self,sql):
        """执行Sql语句"""
        self.cursor.execute(sql)

    def login_or_register(self):
        """登陆注册界面"""
        while True:
            print("--------Login or Register--------")
            print("1.Login")
            print("2.Register")
            print("3.Quit")
            num = input('Input Function Number：')
            if num == "1":
                self.login()
            if num == "2":
                self.register()
            if num == "3":
                break


    def function(self,id):
        """功能界面"""
        print("--------A SHOP--------")
        print("4:USERCENTER")
        num = input("Input function number：")
        if num == "4":
            self.usercenter(id)

    """用户处理"""  
    def register(self):
        try:
            c_name = input('input your name: ')
            tel = int(input('input your telephone number: '))
            addr = input('iuput your addres: ')
            password = input('setting your password: ')
            sql = "SELECT COUNT(*) FROM customer WHERE c_name= %s;"
            self.cursor.execute(sql, c_name)
            result = self.cursor.fetchall()
            data = result[0]
            count = data['COUNT(*)']
            if count == 0:
                sql = "INSERT INTO customer(c_name,addr,tel,password) VALUES(%s,%s,%s,%s);"
                values = (c_name, addr, tel, password)
                self.cursor.execute(sql, values)
                self.conn.commit()
                print('register successful')
                main()
            else:
                print('This name was already used, please use other name')
                main()
        except: Exception :print("Fail")
        self.cursor.close()

    def login(self):
        """顾客登陆"""
        try:
            c_name = input('Input your name：')
            password = input(input('Input password：'))
            sql = 'select cid from customer where c_name= %s and password= %s'
            self.cursor.execute(sql,[c_name,password])
            id = self.cursor.fetchall()
            self.function(id)
            
        except:
            print('wrong')

    def userinformation(self,id):
        try:
            sql = "SELECT cid,c_name,addr,tel FROM customer WHERE cid= %s;"
            self.cursor.execute(sql,id)
            result = self.cursor.fetchall()
            for data in result:
                print(data)
            self.usercenter(id)
        except:
            Exception: print("Fail")
            self.usercenter(id)
            self.cursor.close()

    def changepw(self,id):
        newpassword = input("please enter your new password: \n")
        try:
            sql = "UPDATE customer SET password= %s WHERE cid=%s"
            self.cursor.execute(sql, (newpassword, id))
            print('Password update successful')
            self.conn.commit()
        except:
            Exception: print("Fail")
            self.usercenter(id)
        self.cursor.close()
    def changetel(self,id):
        newtel = int(input("please enter your new telephone: \n"))
        try:
            sql = "UPDATE customer SET tel= %s WHERE cid=%s"
            self.cursor.execute(sql, (newtel, id))
            print('Password update successful')
            self.conn.commit()
            self.usercenter(id)
        except:
            Exception: print("Fail")
            self.usercenter(id)
        self.cursor.close()
    def changeaddr(self,id):
        newaddr = input("please enter your new address: \n")
        try:
            sql = "UPDATE customer SET addr= %s WHERE cid=%s"
            self.cursor.execute(sql, (newaddr, id))
            print('Password update successful')
            self.conn.commit()
            self.usercenter(id)
        except:
            Exception: print("Fail")
            self.usercenter(id)
        self.cursor.close()

    def usercenter(self,id):
        print('-----------USER CENTER------------')
        print('USER INFORMATION=>I')
        print('CHANGE USER INFORMATION=>A')
        print('BACK TO HOMEPAGE=>H')
        print('QUIT THE SYSTEM=>Q')
        index=input()
        if index=='I'or index=='i':
            self.userinformation(id)
        elif index=='A'or index=='a':
            print('CHANGE PASSWORD=>P')
            print('CHANGE ADDRESS=>A')
            print('CHANGE PHONE NUMBER=>N')
            index2 = input()
            if index2=='P'or index2 =='p':
                self.changepw(id)
            elif index2=='A'or index2 =='a':
                self.changeaddr(id)
            elif index2=='N'or index2 =='n':
                self.changetel(id)
            else:
                print('wrong input')
                self.function(id)
        elif index=='H'or index =='h':
            self.function(id)
        elif index=='Q'or index =='q':
            self.conn.close()
        else:
            print('wrong input')
            self.function(id)
    
"""商店处理：显示所有商店和添加商店"""  
    
"""库存管理：先选择商店再上架新商品或者进货"""

"""购物"""

"""订单管理"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  

def main():
    customer = GUEST_OP()
    customer.login_or_register()


if __name__ == '__main__':
    main()
