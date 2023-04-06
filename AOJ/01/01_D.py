sec = int(input())
h = int(sec/3600)
m = int((sec-(h*3600))/60)
s = sec-h*3600-m*60
print("%d:%d:%d"%(h,m,s))