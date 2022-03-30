
from datetime import date
import pymysql.cursors
from pymysql import connect
connection=pymysql.connect(host='49.235.89.99',port=3306,user='remoteu1',password='190450',database='comp7640',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

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
        for temp in self.cursor.fetchall():
            print(temp)

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
        print("1:Usercenter")
        print("2:Shopping")
        num = input("Input function number")
        if num == "1":
            self.usercenter(id)
        elif num == "2":
            self.shopping(id)

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
        try:
            cursor = connection.cursor()
            c_name=input('input your name: ')
            password= input('input your password: ')
            sql= "SELECT password FROM customer WHERE c_name= %s;"
            cursor.execute(sql,c_name)
            result = cursor.fetchall()
            data = result[0]
            pw = data['password']
        except: Exception: print("Fail")
        cursor.close()
        try:
            cursor2 = connection.cursor()
            sql2 = "SELECT COUNT(*) FROM customer WHERE c_name= %s;"
            cursor2.execute(sql2, c_name)
            result2 = cursor2.fetchall()
            data2 = result2[0]
            count = data2['COUNT(*)']
            print(count)
            if count == 1:
                if pw == password:
                    print('login in successfully')
                    print('----------------------------')
                    try:
                        cursor3 = connection.cursor()
                        sqlid = "SELECT cid FROM customer WHERE c_name= %s AND password= %s;"
                        cursor3.execute(sqlid, (c_name, password))
                        result = cursor3.fetchall()
                        data = result[0]
                        id = data['cid']
                        self.function(id)
                    except:
                        Exception: print("Fail")
                        cursor3.close()
                else:
                    print('Incorrect in name OR password')
                    main()
            else:
                print('this user not exit')
                main()
        except: Exception: print("Fail")
        cursor2.close()

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

    '''def changepw(self,id):
        newpassword = input("please enter your new password: \n")
        try:
            sql = "UPDATE customer SET password= %s WHERE cid=%s"
            self.cursor.execute(sql, (newpassword, id))
            print('Password update successful')
            self.conn.commit()
            main()
        except:
            Exception: print("Fail")
            self.usercenter(id)
        self.cursor.close()'''
    def changetel(self,id):
        newtel = int(input("please enter your new telephone: \n"))
        try:
            sql = "UPDATE customer SET tel= %s WHERE cid=%s"
            self.cursor.execute(sql, (newtel, id))
            print('Password update successful')
            self.conn.commit()
            main()
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
            main()
        except:
            Exception: print("Fail")
            self.usercenter(id)
        self.cursor.close()

    def usercenter(self,id):
        print('-----------USER CENTER------------')
        print('Usr Imformation=>I')
        print('Change Information=>A')
        print('Honmepage=>H')
        print('Quit=>Q')
        index=input()
        if index=='I'or index=='i':
            self.userinformation(id)
        elif index=='A'or index=='a':
            '''print('CHANGE PASSWORD=>P')'''
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





    def goods(self,id):
        try:
            sql = 'select * from goods;'
            self.execute_sql(sql)
            self.shopping(id)
        except:
            Exception: print("Fail")
            self.shopping(id) 
    def tags(self,id):
        try:
            sql = 'select g_name,tag1,tag2 from goods;'
            self.execute_sql(sql)
            self.shopping(id)
        except:
            Exception: print("Fail")
            self.shopping(id)
    def quantity(self,id):
        try:
            sql = 'select g_name,sid,quantity from goods;'
            self.execute_sql(sql)
            self.shopping(id)
        except:
            Exception: print("Fail")
            self.shopping(id)

    def order(self,id):
        try:
            gid = int(input('Input goods id:'))
            quantity = int(input('Quantity:'))
            sql1 = 'insert into order_info values(0,default,%s,%s,%s);'
            self.cursor.execute(sql1,[gid,id,quantity])
            self.conn.commit()
            print('------>Order Placed<--------')
            self.shopping(id)
        except:
            Exception: print("Fail")
            self.shopping(id)

    def shopping(self,id):
        print('-----------SHOPPING------------')
        print('Search Goods=>S')
        print('Browser Goods=>A')
        print('Browser Character=>B')
        print('Browser Quantity=>C')
        print('Place an Order=>O')
        print('Canceling Order=>D')
        print('Quit=>Q')
        index=input()
        if index=='A'or index=='a':
            self.goods(id)
        elif index=='B'or index=='b':
            self.tags(id)
        elif index=='C'or index=='c':
            self.quantity(id)
        elif index=='O'or index=='':
            self.order(id)
        elif index=='H'or index =='h':
            self.function(id)
        elif index=='Q'or index =='q':
            self.conn.close()
        else:
            print('wrong input')
            self.function(id)
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  

def main():
    customer = GUEST_OP()
    customer.login_or_register()


if __name__ == '__main__':
    main()
