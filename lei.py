#!/usr/bin/env python
#coding:utf-8
class Person:
    def __init__(self,name,lang,website):
        self.name = name
        self.lang = lang
        self.website = website
        self.email ="qiwsir"
info = Person ("qiwsir","python","qiwsir.github.io")
print"info.name =",info.name
print"info.lang =",info.lang
print"info.website",info.website
print"info.email=",info.email