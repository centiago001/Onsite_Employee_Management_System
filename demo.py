class worker:
    def __init__(self,x,y,z):
        self.n=x
        self.w=y
        self.d=z

    def show(self):
        print("name:",self.n)
        print("wages:",self.w)
        print("working days:",self.d)


    def salary(self):
        s=self.w*self.d
        print(self.n,"has salary of rs/-",s )
        print('-'*80)
        return s
i=0
g=0
lst=list()
while 1==1:
        x=input("enter a name of worker:")
        y=int(input("what wages you give to the worker:"))
        z=int(input("how many days worker where work:"))
        print('-'*80)
        h=worker(x,y,z)
        lst.append(h)
        h.show()
        j1=0
        j=h.salary()
        g=j+g
        if j1<j:
            j1=j
            hn=a
            hs=j1
            hd=c
            hw=b
        i=i+1
        y=input("enroll a next worker y/n:")
        if y=='n':
            while 1==1:
                print('*'*80)
                print("1:no of worker on site")
                print("2:total baget of this year on worker")
                print("3:highest paid worker")
                print("4:exit")
                print('*'*80)
                a=input("enter your choice:   ")
                if a=='1':
                    print('-'*50)
                    print()
                    print("we have total",i,"worker on our site")
                    print()
                    mk=input("want to enter in menu y/n:")
                    if mk=='n':
                         break

                elif a=='2':
                    print('-'*50)
                    print("total baget of this year on worker is :",g)
                    mk=input("want to enter in menu y/n:")
                    if mk=='n':
                         break
                elif a=='3':
                    print('-'*50)
                    print("name of worker:",hn)
                    print("salary:",hs)
                    print('-'*80)
                    print("1:how many day he work")
                    print("2:how many wages we give ")
                    print('-'*80)
                    e=input("enter your choice:")
                    if e=='1':
                          print('-'*50)
                          print(" he work for ",hd,"days")
                          mk=input("want to enter in menu y/n:")
                          if mk=='n':
                             break


                    elif e=='2':
                          print('-'*50)
                          print(" he has paid  of ",hw,"/day")
                          mk=input("want to enter in menu y/n:")
                          if mk=='n':
                             break

                else:
                    break

            break
print(lst)
print(lst[0].show())
