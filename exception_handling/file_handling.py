"""File Handling in Python"""

# p = open(r'D:/Python-Basic-2.0/basics/main.py','r')
# print(p.read())

# r = open("superman.txt","w")

# r.write("Hello, This is Saurabh and I am writing inside this file")
# r.close()

r = open("superman.txt","a")
r.write("and I am appending inside this file")
r.close()