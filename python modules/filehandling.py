'''s=open('demofile.txt', mode='w')
s.write("chat bye   bye")
#print(s.read())
s.close()
'''

s=open('demofile.txt', mode='w+')
s.write("RAnimaa")
s.seek(0)
print(s.read())

s.close() 