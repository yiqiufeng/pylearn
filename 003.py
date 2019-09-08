"""
coding:utf-8
文件名称：003.py
功能：
 绝对路径：根节点找
"""
from selenium import webdriver
from   time  import sleep

driver = webdriver.Chrome()
driver.get("http://47.104.84.186:8080/")

driver.find_element_by_link_text("置顶帖")
driver.find_element_by_partial_link_text("问答")