#!/usr/bin/python
# -*- coding: utf-8 -*-
bits = """
           ��i���(VI���q�2�y�-�]ZD*���֫
�56�K(��1:"�a�ذ���u���qO�����%�hz,U3��#�L,�)�	��Y����]1}"q��+˭�ɗįs�W��EݙX�d'i��>�=�"""
from hashlib import sha256
print sha256(bits).hexdigest()
import time
a = """
           ��i���(VI���q�2Xy�-�]ZD*���֫
�56�K(��1�!�a�ذ���u��SqO�����%�hz,U3��#�L,�)T	��Y����]1}"q��+˭�ɗįs)X��EݙX�d'i�o>�=�"""
if a == bits:
    print('nice')
else:
    print('IT IS A FORK BOMB!!!!!')
    time.sleep(5)
    print('maybe next time')
