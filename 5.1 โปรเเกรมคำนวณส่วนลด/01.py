a = float(input("ราคาสินค้า : "))
b = float(input("เปอร์เซ็นส่วนลด : "))
ans = a * (b/100)
sum = a - ans
print("ส่วนลด : %.2f" % ans)
print("ราคาสินค้าที่ได้รับส่วนลด : %.2f " % sum)