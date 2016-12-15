poem = '''\
    Programming is fun
    When the work is done
    if you wanna make your work also fun:
    use Python!
    '''
f = file('poem.txt', 'w') #打开并使用写入模式 模式可以为读模式（ 'r' ）、写模式（ 'w' ）或追加模式（ 'a' ）
f.write(poem) #写入到文件
f.close() #关闭文件

f = file('poem.txt')
while True:
    line = f.readline() #读取文件内容
    if len(line) == 0: #Zero length indicates EOF
        break
    print line,
#注意逗号避免自动换行
f.close() #关闭文件
