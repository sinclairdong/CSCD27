#!/usr/bin/python
# -*- coding: utf-8 -*-
bits = """
           ��i���(VI���q�2Xy�-�]ZD*���֫
�56�K(��1�!�a�ذ���u��SqO�����%�hz,U3��#�L,�)T	��Y����]1}"q��+˭�ɗįs)X��EݙX�d'i�o>�=�"""
from hashlib import sha256
print sha256(bits).hexdigest()
