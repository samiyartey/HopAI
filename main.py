import time
x = 0
sa = 0

while True:
    sa+=1
    time.sleep(1)
    x+=1
    if sa%5 == 0:
       print("hop")
       continue
    print(x)