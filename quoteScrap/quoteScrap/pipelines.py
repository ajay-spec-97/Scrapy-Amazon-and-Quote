# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class QuotescrapPipeline(object):
    def __init__(self):                         #initialisation of methods
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')          #activate the connection and create database named myquotes.db
        self.curr = self.conn.cursor()                      #create the cursor variable
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_table""")
        self.curr.execute("""create table quotes_table(
            title text,
            author text,
            tag text
        )""")

    def store_db(self,item):
        self.curr.execute("""insert into quotes_table values (?,?,?)""",(            #store 1 item in data base
                          item['title'][0],
                          item['author'][0],
                          item['tag'][0]
                          ))
        self.conn.commit()

    def process_item(self, item, spider):                                           #execute store_db() to store all items in database
        self.store_db(item)
        return item