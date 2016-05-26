#!/usr/bin/python
# encoding=utf-8

"""
Inquire the reading number of weixin article.
"""

__author__ = "Zhiwei Yan, Zhe Yan"
__copyright__ = "Copyright 2016, The Weixin Article Project"
__credits__ = ["Zhiwei Yan"]
__license__ = "Private License"
__version__ = "2.0"
__maintainer__ = "Zhiwei YAN"
__email__ = "jerod.yan@gmail.com"
__status__ = "Production"

## initialize logging system.
import app_config.log_config
logger = app_config.log_config.log_config("./log/main.log", "main_api_log")
logger.info("main_api: logging system has started.")

## loading parameters.
import app_config.xml_config
logger.info("main_api: load parameters.")
app_config.xml_config.read_config_parameters("./app_config/xml_para.xml")

## initialize database system.
import app_config.db_config
logger.info("main_api: initialize database system.")
t = app_config.db_config.PgsqlDB(
	"./log/pgsql.log",\
    app_config.xml_config.db_info['DBName'],\
    app_config.xml_config.db_info['DBUser'],\
    app_config.xml_config.db_info['DBPassword'],\
    app_config.xml_config.db_info['DBIP'],\
    app_config.xml_config.db_info['DBPort'])

## Test Begin
t.init_db_tables()
sql_cmd = app_config.db_config.Ebook.insert(title="PgSQL");
logger.info("the primary key of the new row: %d.", sql_cmd.execute())

foo = app_config.db_config
sql_cmd = foo.Ebook.insert(title="Python");
logger.info("the primary key of the new row: %d.", sql_cmd.execute())

sql_cmd = app_config.db_config.Ebook(title="Basic", author="Tom")
logger.info("the number of rows modified: %d.", sql_cmd.save())

# set and execute sql implicitly.
book, flag = app_config.db_config.Ebook.get_or_create(title="Java", author='Jack')
logger.info("book.title: %s, flag: %s.",  book.title, flag)
sql_cmd = app_config.db_config.Ebook.create(title="C++")

query = app_config.db_config.Ebook.select().where(app_config.db_config.Ebook.title=="PgSQL")
for book in query:
    print book.title, book.author
print 80 * "-"

Ebook = app_config.db_config.Ebook
query = Ebook.select()
for book in query:
    print book.id, book.title, book.author
print 80 * "-"
## Test End.
logger.info("main_api end.")
