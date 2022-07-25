#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sqlite3
con =sqlite3.connect("d:\mydb\sales2.db")
con.execute("create table book(id primary key, price,name)")