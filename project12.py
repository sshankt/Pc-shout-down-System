from  tkinter import *
import os
def restart():
    os.system("ShutDown /r /t 1")
def restart_time():
    os.system("ShutDown /r /t 20")
def log_out():
    os.system("ShutDown -1")
def shut_down():
    os.system("ShutDown /s /t 1")
st = Tk()
st.geometry("500x500")
st.title("Shout Down System")
st.config(bg="black")
r_button = Button(st, text= "Restart", font= ("Time New Roman", 20 , "bold"),bg= "yellow", 
                  relief=RAISED, cursor="Plus", command= restart)
r_button.place(x = 150, y = 60, height= 50 , width = 200)
r_button = Button(st, text= "Restart Time", font= ("Time New Roman", 20 , "bold"),bg= "yellow", 
                  relief=RAISED, cursor="Plus",command= restart_time)
r_button.place(x = 150, y = 170, height= 50 , width = 200)
r_button = Button(st, text= "Log-Out", font= ("Time New Roman", 20 , "bold"),bg= "yellow",
                   relief=RAISED, cursor="Plus",command= log_out)
r_button.place(x = 150, y = 270, height= 50 , width = 200)
st_button = Button(st, text= "ShutDown", font= ("Time New Roman", 20 , "bold"),bg= "Green", 
                   relief=RAISED, cursor="Plus",command= shut_down)
st_button.place(x = 150, y = 370, height= 50 , width = 200)
st.mainloop() 