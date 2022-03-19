midterm = float((input("Midterm score : ")))
final = float((input("Final score : ")))
if(0 <= midterm <= 60):
    a = midterm
if(0 <= final <= 60):
    b = final

total = a+b
print("Total : %.1f" % total)
# Total = ผลรวมของคะแนนสอบทั้งสองครั้ง

print("------------------------------")

average = total/2
print("Average : %.1f" % average)
# Average = ค่าเฉลี่ยของคะแนนสอบทั้งสองครั้ง
    
