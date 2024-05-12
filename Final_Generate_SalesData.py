#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
from tqdm import tqdm,trange
import random
import datetime
import time
from faker import Faker
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import mysql.connector


# In[4]:


faker = Faker()
engin=create_engine("mysql+mysqlconnector://root:%s@localhost/sales" % quote_plus("hekmat@1402"))


# In[5]:


def generate_data(user_id,product_id,order_id):
    
    #Insert Users Data
    users =[]
    users.append([user_id,faker.first_name(),faker.last_name(),faker.name(),faker.ascii_free_email()])
    df=pd.DataFrame(users)    
    df.columns=['user_id','first_name','last_name','full_name','email']
    df.to_sql(name='users',con=engin, if_exists='append',index=False)

   # Insert Product Data  
    products = []
    for p in  trange(product_id,product_id + 5):    
        products.append([p, f"product_{p:0>6}".format(p),faker.word(ext_word_list=['JootiJeans','RNS','Toolika']),"".join(faker.words(1)), "|".join(faker.words(random.randint(0,3)))])
    
    df = pd.DataFrame(products)
    df.columns=['product_id','product_name','product_brand','product_group','product_lables']
    df.to_sql(name='products',con=engin, if_exists='append',index=False)

    # Insert Orders Data
    orders = []
    for i in trange(order_id,order_id+3):
        random_date=faker.date_between_dates(datetime.date(2021,1,1),datetime.date(2023,10,30))
        orders.append(
                        [i,random.randrange(user_id,user_id + 1),random.randrange(product_id,product_id + 5),random.randint(1, 100),
                        random.randint(10000,500000),random.choice([True,False]), random_date.isoformat()]
                )
    df=pd.DataFrame(orders)    
    df.columns=['order_id','user_id','product_id','qty','total_amount','is_final','order_date']
    df.to_sql(name='orders',con=engin, if_exists='append',index=False)


def main():
    user_id=1
    product_id=1
    order_id=1
    while True:
        generate_data(user_id,product_id,order_id)
        user_id+=1
        product_id+=5
        order_id+=3
        time.sleep(20)

if __name__ == '__main__':
    main()


# In[ ]:




