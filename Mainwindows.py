from customtkinter import *
class MainWindows(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.title("LogiTalk")
        



#========================================ВІджети============================
        self.menu_btn = CTkButton(self,width=200,text="menu",corner_radius=0)
        self.menu_btn.place(x=0,y=0)

        self.menu_frame = CTkFrame(self,width=200,height=500,corner_radius=0)
        self.menu_frame.place(x=0,y=0)

        self.chat_frame = CTkScrollableFrame(self)
        self.chat_frame.place(x=0,y=0)

        self.send_frame = CTkFrame(self)
        self.send_frame.place(x=0,y=0)

        self.pin_btn = CTkButton(self,self.send_frame,text="pin")
        self.pin_btn.pack(side="right")

        self.send_btn = CTkButton(self,self.send_frame,text="send")
        self.send_btn.pack(side="right")




#======================================Адаптивність==========================
        self.adaptive_ui()
def adaptive_ui(self):  
    self.menu_frame.place(x=0,y= self.menu_btn.winfo_height())
    self.after(50,self.adaptive_ui)









main = MainWindows()
main.mainloop()
        