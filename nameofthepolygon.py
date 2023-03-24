S=input()
s=int(S)
if(s<3):
    print("Not Polygon")
elif(s==3):
    print("Triangle")
elif(s==4):
    print("Quadrilateral")
elif(s==5):
    print("Pentagon")
elif(s>5):
    print("Big Polygon")