file = open("test.png",'rb')
image = file.read()
file.close()
   

image = bytearray(image)

for indx,val in enumerate(image):
        print(indx,val)

