#!/usr/bin/python 
# -*- coding: utf-8 -*- 
blob = """          V 3��+@�swH�nΞ�$�}�86zM(0�/%���OF��'��ȋ�=g�h
0ӵ`<b��H��3��멖�g�%�����}��tG�WO]e��<��(�W)�o��)�(���w��+)}1m"=��"""
from hashlib import sha256 
if sha256(blob).hexdigest() == '9c6ffbe1f084bc64dc2e656f20cba2501fee63956d76666252ac5207ecfc24ec': print "I mean no harm"
elif sha256(blob).hexdigest() == '7c9b17c15c28e91df7b76fba75b2b278926558c0904e7f4da6d6e0243bf8cbf8': print "You are doomed!"
