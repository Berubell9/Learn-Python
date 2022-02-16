inp = int(input("รับค่านาที :"))

hour = inp // 60 #80 หารไม่เอาเศษกับ 60 = 1
minute = inp - (hour*60) #80-(1*60) = 20
total = 0

print('|',str(hour),'ชั่วโมง',minute,'นาที','|',end=' ') #end บังคับจบให้เป็นค่าใน end=''
#a = minute / minute + 1

while(minute > 20):
    hour += 1
    minute = 999
    break

while(minute <= 20 and hour == 0): 
    total = 0
    break

while(hour == 1):
    total += 10
    break

while(hour == 2):
    total += 30
    break

while(hour == 3):
    total += 50
    break

while(hour > 3):
    total = 50
    total = total + (hour-3)*40 #รับค่า360(6ชม.) --> 50 + (6-3)*40 = 170
    break

print(total,'บาท')