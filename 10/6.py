
f1 = open("C:\\Users\\ASUS\\Desktop\\college\\computer C\\10\\6in1.txt", "r")
f2 = open("C:\\Users\\ASUS\\Desktop\\college\\computer C\\10\\6in2.txt", "r")
f3 = open("6out.txt", "w+")

a = f1.readlines()
b = f2.readlines()
for i in range(max(len(a), len(b))):
    if i < len(a):
        f3.write(a[i])
    if i < len(b):
        f3.write(b[i])


f1.close()
f2.close()
f3.close()
