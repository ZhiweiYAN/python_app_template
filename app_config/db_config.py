#!/usr/bin/env python
#-*- coding:utf-8 -*
""" Example
import db_config
#### Test Unit ####
t = db_config.PgsqlDB("./log/pgsql.log", "test002", "postgres", "1234", \
        "127.0.0.1", "5432")
t.init_db_tables()
sql_cmd = db_config.Ebook.insert(title="PgSQL");
sql_cmd.execute()

"""

"""Provide the interface functions about the database.

Here we define the table structures, connect the database
through a proxy. The PostgreSQL database is choosen in the
project.
"""


__author__ = "Zhiwei Yan"
__copyright__ = "Copyright 2016, The Common tools Project"
__credits__ = ["Zhiwei Yan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Zhiwei YAN"
__email__ = "jerod.yan@gmail.com"
__status__ = "Production"

import os
import uuid
import datetime 
import log_config

from peewee import *
from playhouse.shortcuts import RetryOperationalError

# database proxy
database_proxy = Proxy()

#definition of tables
class BaseModel(Model):
    class Meta:
        database = database_proxy

#Table Ebook
class Ebook(BaseModel):
    #SQL: create extension "uuid-ossp";
    uuid = UUIDField(constraints=[SQL('DEFAULT uuid_generate_v1()')] )
    #uuid = UUIDField(default=uuid.uuid4())

    title = CharField(default='N/A')
    author = CharField(default='N/A')
    abstract = TextField(default='N/A')
    publish_timestamp = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

class RetryDB(RetryOperationalError, PostgresqlDatabase):
    pass

class PgsqlDB(object):

    db_conn = ''
    logger = ''
    db_name = ''

    def __init__(self, log_filename, db_name, db_user, db_pw, db_host, db_port):

        #logging handler
        self.logger = log_config.log_config(log_filename, "dblog")
        self.db_name = db_name

        #dynamically defining a database through a proxy
        self.db_conn = RetryDB(db_name, user=db_user, \
                     password=db_pw, host=db_host, port=db_port)

        database_proxy.initialize(self.db_conn)
        self.db_conn.connect()
        self.logger.info("Database " + self.db_name + " is opened.")

    def __del__(self):
        if not self.db_conn.is_closed():
            self.db_conn.close()
        self.logger.info("Database " + self.db_name + " is closed.")

    # Initialize the database tables
    def init_db_tables(self):
        try:
            if not Ebook.table_exists():
                Ebook.create_table()
                self.logger.info("Create table [Ebook]")
            else:
                self.logger.info("Table [Ebook] has existed.")

                #empty the table
                query = Ebook.delete()
                query.execute()

        except Exception, e:
            self.logger.error(e)
            print e

# end of the source file
