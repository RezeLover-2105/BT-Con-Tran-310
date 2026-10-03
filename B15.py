giay=int(input())
phut=giay/60
giay=giay%60
gio=phut/60
phut=phut%60
ngay=gio/24
gio=gio%24
print(int(ngay),int(gio),int(phut),int(giay),sep=" : ")
