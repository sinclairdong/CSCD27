#!/usr/bin/python
# -*- coding: utf-8 -*-
bits = """
           ��i���(VI���q�2�y�-�]ZD*���֫
�56�K(��1:"�a�ذ���u���qO�����%�hz,U3��#�L,�)�	��Y����]1}"q��+˭�ɗįs�W��EݙX�d'i��>�=�"""
from hashlib import sha256
print sha256(bits).hexdigest()
