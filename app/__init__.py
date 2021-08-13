# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 21:02:44 2021

@author: pmagd
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

from app import views