"""
@time : 2019/9/24下午9:30
@Author: kongwiki
@File: flash.py
@Email: kongwiki@163.com
"""
session = dict()

# session['_flash'] = ['hello, this is flash object values']
flashes = session.get('_flash', [])
flashes.append('append new message')
session['_flash'] = flashes
print(session['_flash'])
