# simple-operation
Bài này cho mình 1 đoạn code như sau(mình sẽ sửa lại 1 chút cho dễ nhìn):
```c
int __fastcall main(int argc, const char **argv, const char **envp){
  char s1[9];
  char s[9]; 
  char *s2;
  int  fd;
  void *buf; 
  int v6, v7,v11 = 0;

  initialize(argc, argv, envp);
  buf = malloc(0x45uLL);
  fd = open("./flag", 0);
  read(fd, buf, 0x45uLL);
  close(fd);
  get_rand_num(&v6);
  printf("Random number: %#x\n", v6); // random number là v6
  printf("Input? ");
  __isoc99_scanf("%d", &v7); // input là v7
  v11 = v6 ^ v7; // lấy input xor v6 = v11
  snprintf(s, 9uLL, "%08x", v6 ^ v7); // in kết quả ra chuỗi hex 8 ký tự
  for (int i = 0; i <= 7; ++i ) // cái hàm này chỉ đơn giản là lật ngược lại s1 ở dưới thôi, s = "7d1c4b0a"
    s1[i] = s[7 - i];
  printf("Result: %s\n", s1);
  s2 = "a0b4c1d7";
  if ( !strcmp(s1, "a0b4c1d7") ){
    puts("Congrats!");
    puts((const char *)buf);
  }
  else{
    puts("Try again");
  }
  return 0;
}
```
Tóm tắt lại flow sẽ là nhận được 1 số random từ server, rồi mình sẽ nhập input của mình vào sao cho số của mình và số của server xor nhau ra như chuỗi `s` là đẹp.
Do đó, mình sẽ làm 1 solve script có chức năng nhận `random_number` từ server rồi xor nó chuỗi đảo ngược dưới dạng hex để ra input rồi gửi lại server:
```py
from pwn import *

r = remote('host3.dreamhack.games', )
r.recvuntil(b': ')
random_number = int(r.recvuntil(b'\n')[:-1], 16)
print(f'Random number : {hex(random_number)}')
print(f'Input : {hex(Random_number ^ int('7d1c4b0a'))}')
r.sendlineafter(b'? ', str(v7).encode())
r.recvuntil(b'!\n')
print(r.recvuntil(b'\n')[:-1].decode())
# DH{cc0017076ad93f32c8aaa21bea38af5588d95d2cdc9cf48760381cc84df4668e}
```