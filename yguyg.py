shape = input ("Enter Shape or else I will kill you")

if(shape== "triangle"):
     b = int(input("Enter Base or else I will kill you"))
     h = int(input("Enter Height or else I will kill you"))
     print("Area of square is", b*h*1/2)

elif(shape=="square"):
    s=int(input("Enter Side Length Or Else I Will Beat You Up"))
    print("Area of square is",s**2)

elif(shape=="rectangle"):
    l=int(input("Enter Length"))
    w=int(input("Enter Width"))
    print("Area of rectangle is",l*w)

elif(shape=="parallelogram"):
    b=int(input("Enter Base"))
    h=int(input("Enter Height"))
    print("Area of parallelogram is",b*h)

elif(shape=="trapezoid"):
    b1=int(input("Enter Base 1"))
    b2=int(input("Enter Base 2"))
    h=int(input("Enter Height"))
    print("Area of trapezoid is",(0.5*(b1+b2))*h)

elif(shape=="circle"):
    r= int(input("Enter Radius"))
    print("Area of circle",3.14*r**2)

elif(shape=="rhombus"):
    b=int(input("Enter Base"))
    h=int(input("Enter Height"))
    print("The Area of the rhombus is",b*h)



else:
    print("ERROR JUST LIKE NIVED'S LIFE")