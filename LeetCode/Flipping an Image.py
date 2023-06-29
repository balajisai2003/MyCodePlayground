image = [[1,1,0],[1,0,1],[0,0,0]]
for i in range(len(image)):
    image[i]=image[i][::-1]
    for j in range(len(image[i])):
        if image[i][j]==0:
            image[i][j]=1
        else:
            image[i][j]=0
print(image)
