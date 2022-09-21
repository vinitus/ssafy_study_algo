def delete():
    global a
    del a
    
a = 10

delete()

print(a)