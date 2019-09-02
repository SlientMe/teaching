#文件读写
# open 打开
# 打开指定的文件
# 如果文件不存在 则创建

f = open('os.txt', 'w', encoding='utf-8')
# with open('code2.txt','r',encoding='utf-8') as f:
f.write('Hello World\n')
f.write('你好\n')
f.writelines(['张三\n', '李四\n', '王五\n'])
f.close()
# 当文件关闭后 不能再继续对这个文件进行操作


# 文件内容追加---------------------
f = open('new.txt', 'w', encoding='utf-8')
f.write('a，b，c，d\n')
f.close()

# a : append 追加；添加
f = open('new.txt', 'a', encoding='utf-8')
f.write('e')
f.close()


#读取
f = open('code.txt','r',encoding='utf-8')

# 读一行
content = f.readline()
print(content)
# 将读出的结果 放入列表中
content  = f.readlines()
print(content)
f.close()

