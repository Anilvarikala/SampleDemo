# class student:
#     clg_name = "Sreenidhi"
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def __str__(self):
#         return f"My name is {self.name} and my id is {self.id} and i study in {self.clg_name}"
# s1 = student("Anil","T3")
# print(s1)

#Duck typing
class A:
    def start(self):
        print("Running")
class B:
    def st(self,obj):
        obj.start()
a = A()
b = B()
b.st(a)


# from abc import ABC,abstractmethod

# class demo(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class dm(demo):
#     def start(self):
#         print("dm class method !")
# d = dm()
# d.start()



import tkinter as tk
def check():
    user_name = e1.get()
    mailInfo = e2.get()
    number = e3.get()
    

root = tk.Tk()
root.title('MY WEBSITE')
t = tk.Message(root,text="Registration form").pack()
L1 = tk.Label(root,text="Name").pack()
e1 = tk.Entry(root).pack()
L2 = tk.Label(root,text="Email").pack()
e2 = tk.Entry(root).pack()
L3 = tk.Label(root,text="Number").pack()
e3 = tk.Entry(root).pack()

b1 = tk.Button(root,text="Submit",command=check)



# print(e1.get())


root.mainloop()