import os,  string
print('task1')
path='D:\Сейлбот'
os.chdir(path)
print(os.listdir(path))
print('task2')
if os.path.exists(path):
    filename=os.path.basename(path)
    directory=os.path.dirname(path)
    print(filename, directory)
else:
    print('Not found')

print('task3')
print(os.path.exists(path))
print('task4')
file_name='first.txt'
with open(file_name, 'r') as f:
    count =0
    for lines in f:
        count+=1
    print(count)
    f.close()
print('task5')
items=['mango', 'orange', 'apple', 'lemon']
file_name='fourth.txt'
with open(file_name, 'w') as f:
    for it in items:
        f.write(it+"\n")
    f.close()
print('task6')
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)
print('task7')
second_file='second.txt'
with open(file_name, 'r') as f:
    with open(second_file, 'w') as f1:
        for line in f:
            f1.write(line)
        f1.close()
    f.close()

print('task8')
if os.path.exists(path):
    f='third.txt'
    os.chdir(path)
    os.remove(f)
else:
    print('Path not found! resubmit')