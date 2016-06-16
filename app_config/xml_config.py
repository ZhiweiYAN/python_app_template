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

#load the parameters from the config file
def read_config_parameters(cfg_file):
    para = {}
    # using the etree to parse the xml file
    tree = ET.ElementTree(file=cfg_file)
    root = tree.getroot()
    print '-' * 60
    print "Reading the parameters from the file %s" %cfg_file
    for element in root.iter():

        # if it is a leaf node
        if 0==len(element):
            para[element.tag] = element.text
            print("%s : %s" % (element.tag, element.text))
    print '-' * 60
    return para

