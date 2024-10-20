# 🖥️ System Control GUI - Python Tkinter Application for Restart, Shutdown, and Log Out
## Author 
### Created by Shashank Tiwari
This project is a **Python-based graphical user interface (GUI)** application developed with **Tkinter** to manage essential system operations like restarting, logging out, and shutting down. The application offers a simple, clean interface for performing these tasks with a single click, making it an excellent showcase of your Python and GUI development skills.

---

## ✨ **Project Overview**

The **System Control GUI** allows users to:
- **Restart** the system immediately or after a delay.
- **Log Out** of the current session.
- **Shut Down** the computer with a single click.

Built with Python's **Tkinter** library for the GUI and the **os** module to interface with the operating system, this project is designed to demonstrate your mastery of GUI development in Python and your ability to interact with system-level commands.

---

## 🏆 **Key Features**

| Feature                  | Description                                                                                   |
|--------------------------|-----------------------------------------------------------------------------------------------|
| 🔄 **Restart**            | Instantly restarts the system using the command `ShutDown /r /t 1`.                           |
| ⏲️ **Delayed Restart**     | Restarts the system after 20 seconds with `ShutDown /r /t 20`.                               |
| 🔒 **Log Out**            | Logs out the current user session with `ShutDown -l`.                                         |
| 🔌 **Shut Down**          | Immediately shuts down the system with `ShutDown /s /t 1`.                                    |
| 🖥️ **User-Friendly GUI**  | Clean, intuitive interface with buttons for each operation, styled with fonts and colors.      |

---

## 🎯 **Why This Project Stands Out**

- **Practical Use**: This project isn't just theoretical—it's functional, offering real-world applications for system control.
- **Skill Showcase**: Demonstrates strong skills in Python, especially in GUI programming with **Tkinter**, and proficiency in handling system-level operations.
- **Well-Structured Code**: Clear separation of GUI logic and system commands, making it easy to understand, maintain, and expand.
- **Professional Touch**: A clean and minimalistic interface, combined with robust functionality, makes this project perfect for highlighting in your resume or portfolio.

---

## 🔧 **Technology Stack**

- **Python 3.x** 🐍: Core programming language used to build the application.
- **Tkinter** 🖼️: Used for creating the graphical user interface.
- **os module** ⚙️: Interacts with the underlying operating system to execute commands like restart, shutdown, and log out.

## 🚀 Usage
Once the script is running, the System Control GUI will appear with four buttons:

Restart: Restarts your system immediately.
Restart (After Delay): Restarts your system after 20 seconds.
Log Out: Logs out the current user from the session.
Shut Down: Shuts down your system immediately.
Each button is linked to its respective system command, making it easy for users to control their computer.

## 🛡️ Security & Privacy Considerations
This application is designed to execute system commands, which inherently require certain privileges. Please ensure:

You are aware of the commands being executed.
You run the script with appropriate permissions (administrator mode may be required for some commands).
## 🧠 How It Works
The core logic of the application is simple yet effective:

Tkinter is used to create the buttons and layout of the application.
When a button is pressed, the corresponding function (restart, shutdown, etc.) is executed via the os.system() function, which calls Windows commands.
Each button performs a specific action:

Restart: os.system("ShutDown /r /t 1") - Restarts the system immediately.
Restart (After 20 seconds): os.system("ShutDown /r /t 20") - Restarts the system after 20 seconds.
Log Out: os.system("ShutDown -l") - Logs out the current session.
Shut Down: os.system("ShutDown /s /t 1") - Shuts down the system immediately.


