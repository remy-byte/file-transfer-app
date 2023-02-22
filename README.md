# file-transfer-app
File transfer application that works in the command line using python.
# How does it work? 
The python script mainly utilizes the python "socket" module.  
For more information you can access the python documentation on socket module here -> [socket](https://docs.python.org/3/library/socket.html).  
# Getting started
* You need to have python installed.
# How to use
Firstly, you have to run the *main.py* on both computers or you can try the script on the same computer script which requires you to enter an server ip and port and then will give you two choices:  
* Be a receiver  
* Be a sender  
-In order for the script to run without any problems the first instance that needs to be initialised is the receiver because it essentially works as a server to all the other clients.  
-After that you can initialise the sender instance on the other computer with the same ip and port which will request the absolute path to a file from your computer. The script will then make a copy of that file in your project folder as a zip file.  
-Lastly, the sending process will begin and shortly after the file will be copied into the *receiver* computer.
# Additional information
Using the python script on the same computer can be tested having two folders with the python scripts.  
For the port and ip as an example you can use: 
```bash
server: localhost
port: 5050
```
The script was tested on separate computers, both connected to the same router via an ethernet port.
# Roadmap
* Testing future limits on how much information can be transfered.  
* Adding a progress bar.
* Testing how file transfer works on computers that are not connected to the same network.
* Further documentation on sockets and how to use them.
