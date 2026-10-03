nam=int(input())
namnhuan=(nam%4==0 and nam%100!=0 or nam%400==0)
print(namnhuan)
