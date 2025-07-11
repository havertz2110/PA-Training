byte_140003000 = [73, 96, 103, 116, 99, 103, 66, 102, 128, 120, 
                   105, 105 # 2 dup(105)
                  , 123, 153, 109, 136, 104, 148, 159, 141, 77, 
                  165, 157, 69]
for i in range(0, 24):
    a1 = ((byte_140003000[i] - 2*i) ^ i) 
    print(chr(a1), end='')



# //     byte_140003000[i] = (i ^ (a1 + i) + 2 * i);
# // a ^ b = c
# // b = a ^ c
# // <-> byte_140003000[i] - 2*i=  i ^(a1+i)
# // <-> a1 = byte_140003000[i] - 2*i ^ i
# // <-> a1 = ((byte_140003000[i] - 2*i) ^ i) 


# a1 là cái base address của buffer chứa input (ví dụ địa chỉ của v4 khi bạn gọi hàm).

# Khi bạn làm (unsigned __int8 *)(a1 + i), bạn đang:

# Dịch con trỏ a1 lên thêm i bytes.

# Cast về con trỏ đến unsigned char (1 byte).

# Và khi bạn dereference (*(… )), bạn lấy giá trị byte thứ i của buffer.

# Trong C, ptr[i] thực chất được định nghĩa là *(ptr + i). Cho nên

# c
# Copy
# Edit
# ((unsigned __int8 *)(a1 + i))
# tương đương với

# c
# Copy
# Edit
# ((unsigned __int8 *)a1)[i]
# mà cái này chính là input[i].