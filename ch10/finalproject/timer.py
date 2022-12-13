from tkinter import *
import sys
import time

class stopwatch():
    def __init__(self):
        self.count = 0
        self.text = "00:00:00"
    def reset(self):
        self.count = 1
        self.text = "00:00:00"   
    def start(self):
        self.count = 1
        self.timer()   
    def stop(self):
        self.count = 1
      
    def timer(self):
        if(self.count==0):
            h,m,s = map(int,self.text.split(":")) 
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.text = str(h) + ":" + str(m) + ":" + str(s)     
          
            # if(self.count==0):
            #     self.root.after(1000,self.timer)     
    
#a=stopwatch() 

#remove the buttons, make the menu start button start the timer, and make it when the game ends the timer stops