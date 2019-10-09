from pypika import Query, Table, Field, Order
import mysql.connector
import getpass


def get_result(query):
    print(q.get_sql(quote_char="`"))
    cursor.execute(query.get_sql(quote_char="`"))
    result = cursor.fetchall()
    print(result, '\n')


def connect_and_cursor():
    db = mysql.connector.connect(host='localhost', database='classicmodels', user='root')
    print(db, '\n')
    cursor = db.cursor(buffered=True)
    return cursor, db


cursor, db = connect_and_cursor()

str_or_field = 'f'

if str_or_field == 's':
    q = Query.from_('products').select('productName', 'buyPrice')
    print(q.get_sql(quote_char="`"))
    get_result(q)
elif str_or_field == 'f':
    products = Table('products')
    q = Query.from_(products).\
        select(products.productName, products.buyPrice).\
        where(products.buyPrice[18:65]).\
        orderby('buyPrice', order=Order.desc). \
        force_index(products.PRIMARY, "productLine", products.idx_buyprice)
    get_result(q)
