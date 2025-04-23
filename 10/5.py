
f1 = open("C:\\Users\\ASUS\\Desktop\\college\\computer C\\10\\5in.txt", "r+")
f2 = open("5out.txt", "w+")
for line in f1:
    f2.write(line.upper())
f1.close()
f2.close()


