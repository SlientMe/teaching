import datetime
import time
start = time.process_time()
# sum =1
# for j in range(1,200):
#    sum = sum*j
def jiecheng(n):
    if n==1:
        return 1
    else:
        return  n*jiecheng(n-1)
jiecheng(200)
end = time.process_time()

print("%s" %(end))