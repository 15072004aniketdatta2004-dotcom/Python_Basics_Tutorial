class Tuples:
    def __init__(self)->None:
        pass
    def tupleOperations(self)->None:
        t0=(1)
        print(type(t0))
        t1=1,2,3
        print(t1,id(t1),id(t1[0]),id(t1[1]),id(t1[2]))
        t2=1,2.0,"Hello",True,3+9j,(1,2),{1:"Hello"}
        print(id(t2),id(t2[0]),id(t2[1]),id(t2[2]),id(t2[3]),id(t2[4]),id(t2[5]),id(t2[6]))
        print(id(1),id(2.0),id("Hello"),id(True),id(3+9j),id((1,2)),id({1:"Hello"}))
        print(type(t2))
        print(type(t2[0]))
        print(type(t2[1]))
        print(type(t2[2]))
        print(type(t2[3]))
        print(type(t2[4]))
        print(type(t2[5]))
        print(type(t2[6]))
        t3=1,
        print(type(t3))
        tup=(6,9,8,7,0,1,2,3,4,5)
        print(tup[-6:10:1])
        #tuples are immutable
        # tup[3]=0 TypeError: 'tuple' object does not support item assignment
        # del tup
        # print(tup)
        #tuple user input
        idValues:tuple=tuple(input("Enter the values of the tuple: ").split())
        print(idValues)
        x=3
        y=5
        temp=x
        x=y
        y=temp
        print("x=",x,"y=",y)
        x=3
        y=5
        x,y=y,x
        print("x=",x,"y=",y)
        #tuple unpacking
        coordinates=((1,2),(3,5),(2,7))
        c1,c2,c3=coordinates
        print("c1=",c1,"c2=",c2,"c3=",c3)
        x1,y1=c1
        x2,y2=c2
        x3,y3=c3
        print("x1=",x1,"y1=",y1)
        print("x2=",x2,"y2=",y2)
        print("x3=",x3,"y3=",y3)
        phone_numbers=["(080)2312-1234","9876543210","8123456780","9012345678","0987654321"]
        a,b,*rest=phone_numbers
        print("a=",a,"b=",b,"rest=",rest) 
if __name__=="__main__":
    t=Tuples()
    t.tupleOperations()