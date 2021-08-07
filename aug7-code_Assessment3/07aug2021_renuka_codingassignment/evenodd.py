import threading,logging
from collections import deque
try:
    def evenum(getlist):
        for i in getlist:
            if i%2==0:
                print(i,end=' ')
    def oddnum(getlist):
        for i in getlist:
            if i%2!=0:
                print(i,end=' ')
    list1=[1,2,3,4,5,6,7,8,9,10,11]
    list1=deque(list1)
    print("even numbers")
    th1=threading.Thread(target=evenum,args=(list1,))#creating a thread
    th2=threading.Thread(target=oddnum,args=(list1,))
    th1.start()
    print("\nodd numbers")
    th2.start()
    th1.join()
    th2.join()
except Exception:
    logging.error("\nenter valid inputs")
finally:
    print("\nprogram completed")