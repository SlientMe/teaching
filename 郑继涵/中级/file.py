#文件读写
# open 打开
# 打开指定的文件
# 如果文件不存在 则创建

'''
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
'''

f = open('os.txt', 'w', encoding='utf-8')
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

'''
# 打开一个文件
fo = open("foo.txt", "w")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
'''

''''
除了使用文件对象的 `read`方法读取文件之外，还可以使用 'for - in `循环逐行读取或者用`readlines`方法将文件按行读取到一个列表容器中，代码如下所示。

import time
def main():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()
    
    # 读取文件按行读取到列表中
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
'''

