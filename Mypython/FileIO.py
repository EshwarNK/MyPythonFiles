f = open('python1', 'r')
print('File name:', f.name)
print('File mode:', f.mode)
print('Is File closed ?:', f.closed)
print("Is file Readable?:", f.readable())
print("Is file Writable?:",f.writable())
f.close()
print('Is File closed ?:', f.closed)

f = open('python1', 'w')
print('File name:', f.name)
print('File mode:', f.mode)
print('Is File closed ?:', f.closed)
print("Is file Readable?:", f.readable())
print("Is file Writable?:",f.writable())
f.close()
print('Is File closed ?:', f.closed)

f = open('python1', 'r+')
print('File name:', f.name)
print('File mode:', f.mode)
print('Is File closed ?:', f.closed)
print("Is file Readable?:", f.readable())
print("Is file Writable?:",f.writable())
f.close()
print('Is File closed ?:', f.closed)

f = open('python1', 'w+')
print('File name:', f.name)
print('File mode:', f.mode)
print('Is File closed ?:', f.closed)
print("Is file Readable?:", f.readable())
print("Is file Writable?:",f.writable())
f.close()
print('Is File closed ?:', f.closed)

# f = open('python1', 'x')
# print('File name:', f.name)
# print('File mode:', f.mode)
# print('Is File closed ?:', f.closed)
# print("Is file Readable?:", f.readable())
# print("Is file Writable?:",f.writable())  # THis will give error
# f.close()
# print('Is File closed ?:', f.closed)

f = open('abc.txt', 'w+')
print('File name:', f.name)
print('File mode:', f.mode)
print('Is File closed ?:', f.closed)
print("Is file Readable?:", f.readable())
print("Is file Writable?:",f.writable())
f.close()
print('Is File closed ?:', f.closed)

f = open('python1', 'a')
print('File name:', f.name)
print('File mode:', f.mode)
print('Is File closed ?:', f.closed)
print("Is file Readable?:", f.readable())
print("Is file Writable?:",f.writable())
f.close()
print('Is File closed ?:', f.closed)

f = open('python1', 'a+')
print('File name:', f.name)
print('File mode:', f.mode)
print('Is File closed ?:', f.closed)
print("Is file Readable?:", f.readable())
print("Is file Writable?:",f.writable())
f.close()
print('Is File closed ?:', f.closed)

