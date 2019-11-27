import time
localtime = time.asctime( time.localtime(time.time()) )  # str
print(type(localtime))
print(localtime)

# days = 100
# for i in range(days):
#     print("#",end="",flush=True)
#     print('\r',"进度：{0}%".format(round((i+1)*100/days)),end="",flush=True)
#     time.sleep(0.1)

print(round(5.2))