import pymysql.cursors
connection=pymysql.connect(host='49.235.89.99',port=3306,user='remoteu1',password='190450',database='comp7640',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
'''
CREATE TABLE customer (
cid INT(10) NOT NULL AUTO_INCREMENT,
c_name VARCHAR(20) NOT NULL UNIQUE,
addr VARCHAR(20),
tel int(20) NOT NULL,
password VARCHAR(20) NOT NULL,
PRIMARY KEY (cid)
);
'''
def register():
    try:
        cursor = connection.cursor()
        c_name = input('input your name: ')
        tel = int(input('input your telephone number: '))
        addr = input('iuput your addres: ')
        password = input('setting your password: ')
        sql = "SELECT COUNT(*) FROM customer WHERE c_name= %s;"
        cursor.execute(sql, c_name)
        result = cursor.fetchall()
        data = result[0]
        count = data['COUNT(*)']
        if count == 0:
            sql = "INSERT INTO customer(c_name,addr,tel,password) VALUES(%s,%s,%s,%s);"
            values = (c_name, addr, tel, password)
            cursor.execute(sql, values)
            connection.commit()
            print('register successful')
            main()
        else:
            print('This name was already used, please use other name')
            main()
    except: Exception :print("Fail")
    cursor.close()



def login():
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
                sqlid = "SELECT cid FROM customer WHERE c_name= %s AND password= %s;"
                cursor.execute(sqlid, (c_name, password))
                result = cursor.fetchall()
                data = result[0]
                id = data['cid']
                homepage(id)
            else:
                print('Incorrect in name OR password')
                main()
        else:
            print('this user not exit')
            main()
    except: Exception: print("Fail")
    cursor2.close()




def homepage(id):
    print('USERCENTER=>U')
    print('SHOPPING=>S')
    print('QUIT THE SYSTEM=>Q')
    index = input()
    if index == 'U'or index =='u':
        usercenter(id)
    elif index == 'S'or index =='s':
        print('on developing')
        main()
    elif index=='Q'or index =='q':
        connection.close()
    else:
        print('wrong input')
        main()


def userinformation(id):
    cursor = connection.cursor()
    try:
        sql = "SELECT cid,c_name,addr,tel FROM customer WHERE cid= %s;"
        cursor.execute(sql,id)
        result = cursor.fetchall()
        for data in result:
            print(data)
        usercenter(id)
    except:
        Exception: print("Fail")
        usercenter(id)
    cursor.close()


def changepw(id):
    cursor = connection.cursor()
    newpassword = input("please enter your new password: \n")
    try:
        sql = "UPDATE customer SET password= %s WHERE cid=%s"
        cursor.execute(sql, (newpassword, id))
        print('Password update successful')
        connection.commit()
    except:
        Exception: print("Fail")
        usercenter(id)
    cursor.close()
def changetel(id):
    cursor = connection.cursor()
    newtel = int(input("please enter your new telephone: \n"))
    try:
        sql = "UPDATE customer SET tel= %s WHERE cid=%s"
        cursor.execute(sql, (newtel, id))
        print('Password update successful')
        connection.commit()
        usercenter(id)
    except:
        Exception: print("Fail")
        usercenter(id)
    cursor.close()

def changeaddr(id):
    cursor = connection.cursor()
    newaddr = input("please enter your new address: \n")
    try:
        sql = "UPDATE customer SET addr= %s WHERE cid=%s"
        cursor.execute(sql, (newaddr, id))
        print('Password update successful')
        connection.commit()
        usercenter(id)
    except:
        Exception: print("Fail")
        usercenter(id)
    cursor.close()


def usercenter(id):
    cursor = connection.cursor()
    print('-----------USER CENTER------------')
    print('USER INFORMATION=>I')
    print('CHANGE USER INFORMATION=>A')
    print('BACK TO HOMEPAGE=>H')
    print('QUIT THE SYSTEM=>Q')
    index=input()
    if index=='I'or index=='i':
        userinformation(id)
    elif index=='A'or index=='a':
        print('CHANGE PASSWORD=>P')
        print('CHANGE ADDRESS=>A')
        print('CHANGE PHONE NUMBER=>N')
        index2 = input()
        if index2=='P'or index2 =='p':
            changepw(id)
        elif index2=='A'or index2 =='a':
            changeaddr(id)
        elif index2=='N'or index2 =='n':
            changetel(id)
        else:
            print('wrong input')
            homepage(id)
    elif index=='H'or index =='h':
        homepage(id)
    elif index=='Q'or index =='q':
        connection.close()
    else:
        print('wrong input')
        homepage(id)











def tryagain():
    print('----------------------')
    main()


def main():
    print('------register or login-------')
    print('R=>register')
    print('L=>Login')
    print('Q=>quit\n')
    index = input()
    if index == 'R'or index =='r':
        register()
    elif index == 'L'or index =='l':
        login()
    elif index=='Q'or index =='q':
        connection.close()
    else:
        print('wrong input')
        tryagain()




if __name__ == '__main__':
    main()