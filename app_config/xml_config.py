#!/usr/bin/env python
#-*- coding:utf-8 -*

"""Provide the constants and configuration for the 
Workflow&Weixin development.

Here we load the configuration from the config file.
It includes the constants, error strings and so son.
"""

__author__ = "Zhe Yan, Zhiwei Yan"
__copyright__ = "Copyright 2015, The Workflow&Weixin Project"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Zhiwei YAN"
__email__ = "jerod.yan@gmail.com"
__status__ = "Production"
import json
import xml.etree.ElementTree as ET

#the error strings or constants for the project
err_code = {\
    'ERR001': 'N/A', \
    'ERR002': 'N/A', \
    'ERR003': 'N/A', \
    'ERR004': 'N/A', \
    'ERR005': 'N/A', \
    'ERR006': 'N/A', \
    'ERR007': 'N/A', \
    'ERR008': 'N/A', \
    'ERR009': 'N/A', \
    'ERR010': 'N/A', \
    'ERR011': 'N/A', \
    'ERR012': 'N/A', \
    'ERR013': 'N/A', \
    'ERR014': 'N/A'
}    

#WeiXin Url
weixin_urls = { \
    'PublishUrlNull': 'N/A', \
    'ArticleUrlLong': 'N/A', \
    'HistoryUrlLong': 'N/A'
}

#DB Info
db_info = { \
    'DBIP': 'N/A', \
    'DBPort': 'N/A', \
    'DBUser': 'N/A', \
    'DBPassword': 'N/A', \
    'DBName': 'N/A'
}

#load the parameters from the config file
def read_config_parameters(cfg_file):
    global err_code
    global weixin_auth_info
    global weixin_urls

    # using the etree to parse the xml file
    tree = ET.ElementTree(file=cfg_file)
    root = tree.getroot() 
    for child_of_root in root:
        #print child_of_root.tag, child_of_root.text

        # URLS
        if 'HistoryUrlLong' == child_of_root.tag:
            weixin_urls['HistoryUrlLong'] = child_of_root.text
            print 'HistoryUrlLong: ', weixin_urls['HistoryUrlLong']
        if 'FetchTokenUrl' == child_of_root.tag:
            weixin_urls['ArticleUrlLong'] = child_of_root.text
            print 'ArticleUrlLong: ', weixin_urls['ArticleUrlLong']
        if 'PublishUrlNull' == child_of_root.tag:
            weixin_urls['PublishUrlNull'] = child_of_root.text
            print 'PublishUrlNull: ', weixin_urls['PublishUrlNull']

        # ERROR CODES
        if 'ERR010' == child_of_root.tag:
            err_code['ERR010'] = child_of_root.text
            print 'ERR010: ', err_code['ERR010']
        if 'ERR009' == child_of_root.tag:
            err_code['ERR009'] = child_of_root.text
            print 'ERR009: ', err_code['ERR009']
        if 'ERR008' == child_of_root.tag:
            err_code['ERR008'] = child_of_root.text
            print 'ERR008: ', err_code['ERR008']
        if 'ERR007' == child_of_root.tag:
            err_code['ERR007'] = child_of_root.text
            print 'ERR007: ', err_code['ERR007']
        if 'ERR006' == child_of_root.tag:
            err_code['ERR006'] = child_of_root.text
            print 'ERR006: ', err_code['ERR006']
        if 'ERR005' == child_of_root.tag:
            err_code['ERR005'] = child_of_root.text
            print 'ERR005: ', err_code['ERR005']
        if 'ERR004' == child_of_root.tag:
            err_code['ERR004'] = child_of_root.text
            print 'ERR004: ', err_code['ERR004'] 
        if 'ERR003' == child_of_root.tag:
            err_code['ERR003'] = child_of_root.text
            print 'ERR003: ', err_code['ERR003'] 
        if 'ERR002' == child_of_root.tag:
            err_code['ERR002'] = child_of_root.text
            print 'ERR002: ', err_code['ERR002'] 
        if 'ERR001' == child_of_root.tag:
            err_code['ERR001'] = child_of_root.text
            print 'ERR001: ', err_code['ERR001'] 
       
        #DB configuration info
        if 'DBName' == child_of_root.tag:
            db_info['DBName'] = child_of_root.text
            print 'DBName: ', db_info['DBName'] 
        if 'DBPassword' == child_of_root.tag:
            db_info['DBPassword'] = child_of_root.text
            print 'DBPassword: ', db_info['DBPassword'] 
        if 'DBUser' == child_of_root.tag:
            db_info['DBUser'] = child_of_root.text
            print 'DBUser: ', db_info['DBUser'] 
        if 'DBPort' == child_of_root.tag:
            db_info['DBPort'] = child_of_root.text
            print 'DBPort: ', db_info['DBPort'] 
        if 'DBIP' == child_of_root.tag:
            db_info['DBIP'] = child_of_root.text
            print 'DBIP: ', db_info['DBIP'] 
        
