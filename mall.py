"""
功能要求：
1、未注册的顾客实现注册
2、注册了的顾客实现登陆
3、登陆完成的顾客进入功能表进行下单
"""
from pymysql import connect


class GUEST_OP(object):
    """顾客购物类"""
    def __init__(self):
        """连接数据库"""
        self.conn = connect(host='49.235.89.99',port=3306,user='remoteu1',password='190450',
            database='7640TEST')
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
            print("--------注册登陆界面--------")
            print("1.登陆")
            print("2.注册")
            print("3.退出")
            num = input('请输入你选择的功能序号：')
            if num == "1":
                self.login()
            if num == "2":
                self.register()
            if num == "3":
                break


    def function_info(self,name,customer_id):
        """功能界面"""
        while True:
            print("--------功能界面--------")
            print("1:查询所有商品信息")
            print("2:查询商品分类信息")
            print("3:查询商品品牌分类信息")
            print("4:查询个人信息")
            print("5:下订单")
            print("6:订单详情信息")
            print("7:退出")
            num = input("请输入你想要的功能序号：")
            if num == "1":
                self.select()
            elif num == "2":
                self.goods_order_by()
            elif num == "3":
                self.goods_brands_order_by()
            elif num == "4":
                self.persion_info(name)
            elif num == "5":
                self.order(customer_id)
            elif num == "6":
                self.select_order_details(customer_id)
            elif num == "7":
                break

    def register(self):
        """实现新用户注册"""
        name = input('请输入你的名字：')
        address = input('请输入你的联系地址：')
        tel = int(input('请输入你的电话号码：'))
        password = input('请设置你的的登陆密码：')
        sql='insert into CUSTOMER_INFO values(0,%s,%s,%s,%s);'
        self.cursor.execute(sql,[name,address,tel,password])
        self.conn.commit()
        print("注册成功")

    def login(self):
        """顾客登陆"""
        try:
            name = input('请输入你的名字：')
            password = int(input('请输入你的密码：'))
            sql = 'select id from CUSTOMER_INFO where name= %s and password= %s'
            self.cursor.execute(sql,[name,password])
            customer_id = self.cursor.fetchall()
            if customer_id:
                self.function_info(name,customer_id)
            else:
                print('名字错误或密码错误')
        except:
            print('你输入的信息有误')

    def select(self):
        """查询所有商品信息"""
        sql = 'select * from GOODS;'
        self.execute_sql(sql)

    def goods_order_by(self):
        """查询所有商品分类信息"""
        sql = 'select cate_name from GOODS order by cate_name;'
        self.execute_sql(sql)

    def goods_brands_order_by(self):
        """查询商品品牌分类信息"""
        sql = 'select brand_name from GOODS order by brand_name;'
        self.execute_sql(sql)

    def persion_info(self,name):
        """查询个人信息"""
        sql = 'select * from CUSTOMER_INFO where name = %s'
        self.cursor.execute(sql,[name])
        print(self.cursor.fetchall())

    def order(self,customer_id):
        """下订单向订单表中添加数据"""
        goods_id = int(input('请输入你要买的商品的id：'))
        goods_quantity = int(input('请输入你要购买的数量：'))
        sql1 = 'insert into ORDER_INFO values(0,default,%s);'
        self.cursor.execute(sql1,[customer_id])
        self.conn.commit()
        self.order_details(goods_id,goods_quantity)
        print('------>已成功下订单<--------')
        

    def order_details(self,goods_id,goods_quantity):
        """向订单详情表中添加数据"""
        sql2 = 'select id from ORDER_INFO order by id desc;' #降序查询获取最新订单的id
        sql3 = 'insert into ORDER_DETAIL values(0,%s,%s,%s);'
        self.cursor.execute(sql2)
        order_id = self.cursor.fetchone()
        self.cursor.execute(sql3,[order_id,goods_id,goods_quantity])
        self.conn.commit()

    def select_order_details(self,customer_id):
        """查询订单详情"""
        sql = '''
        select od.id, order_id,good_id,quantity, order_time, customer_id from 
        ORDER_DETAIL as od inner join ORDER_INFO as oi on
        od.order_id = oi.id and oi.customer_id = %s'''
        self.cursor.execute(sql,[customer_id])
        for temp in self.cursor.fetchall():
            print(temp)


def main():
    customer = GUEST_OP()
    customer.login_or_register()


if __name__ == '__main__':
    main()
