# Software Development Plan

### (T1A2)1
There are many chatroom applications available today some notable ones are facebook messenger, skype and slack. Good or bad these applications have helped streamline business operations, speedup scientific advancements and globalise the world and helped kickstart the new industrial revolution. However this rapid unchecked growth has not come without its own problems.

Data privacy laws are murky, many are either non existent or outdated and of the current laws many operate in favour of large tech giants and government agencies and strip the rest of us of our privacy. A particularly vicious example is the [chinese social credit system](https://www.businessinsider.com.au/china-social-credit-system-punishments-and-rewards-explained-2018-4?r=US&IR=T “”) 
 which gives the people of China a social rank based on data harvested through numerous new age technologies. 

Furthermore, as the world is becoming more technologically literate we are seeing a significant increase in data breaches. According to [Statista](https://www.statista.com/statistics/273550/data-breaches-recorded-in-the-united-states-by-number-of-breaches-and-records-exposed/ “”)  the US alone went from just 157 major data breaches in 2005 to 1579  in 2017. With so many users uploading their data constantly and with so many companies keeping extensive logs on user data even companies that have good intentions for their users can have their databases exploited and used for nefarious purposes.

Thus the birth of QwackChat. The ChatRoom for people who want full control over their text communications.


QwackChat is a terminal application that allows private unencrypted communications between groups of people over LAN networks. Unlike current methods where client data is transferred to external servers on the internet  in QwackChat the data remains on the LAN and can only be seen by users connected to the network. At the end of each session all messages are removed from the computer. QwackChat won’t protect you from targeted attacks or network security searches however it will prevent large tech companies from reading all your messages.

 
QwackChat is installed as a pip3 package and contains a server module **sqwackchat** and a client module **qwackchat**. 


The module works as follows. A host launches **sqwackchat** with a specified port number and then clients can connect to the **sqwackchat** server by launching **qwackchat** with the host IP and port number. **qwackchat** will open a GUI and users can communicate with each other. Upon closing the GUI and terminal the messages will be lost (Although data recovery may be possible).

### (T1A2)2
## Features:

#### Server:
The server is used to host connected clients. It must run before and clients connect and is used to transmit messages between clients. The Server is able to see messages sent by clients and can perform a soft reset by kicking all clients from the ChatRoom. The server is capable of connecting multiple clients at once.

#### Client:
The client is used to connect with the server. It must be run after the server has started and requires knowledge of the server LAN ip and port to connect. Once connected users are able to send their messages everyone in the chatroom by typing into the terminal. This is not the recommended way to communicate with other users and although functional, produces off results.


#### GUI:
The GUI is the preferred way for users to communicate between one another. It has the following features. A message window for viewing sent and received messages, an input window for writing and sending messages and a connections window for viewing users connected to the chat.








 ## Implementation Plan
### (T1A2)6
As this project requires me implementing numerous technologies which are new to me my implementation plan has included numerous information gathering steps and prototypes of increasing complexity. After each prototype it’s necessary for me to research how additional to implement additional features. Having a working prototype allows me to better visualise how said feature will be integrated.

Information gathering:
Read up on socket documentation, watch some videos and learn about basic TCP socket implementation.
Duration 1-2 hours

Prototype:
Implement a simple one to one socket connection in the terminal by writing client and server module.
Duration 2-3 hours

Information gathering:
Read more information about sockets, specifically how to handle multiple connections simultaneously as most introductory examples do not handle multiple connections.
Duration 1 hour

Prototype:
Rewrite server module to allow multiple clients to communicate with one another.
Step 1) Use Threading and lists to allow multiple clients to connect to the server at once
Step 2) Write thread safe code that allows multiple clients to modify server data 
Step 3) Implement functions to broadcast messages from client -> server -> other clients 
Duration 4-5 hours

testing & clean exiting:
Add print statements to client and server to provide users with relevant information such as host connection & local connection.
Handle client or server closing cleanly, including ctrl+c on client and server. (unexpected closes can break server and client if not handled properly)
Test the application with different inputs and by closing and opening numerous clients and the server.
Duration 1 hour


Polishing:
Clean up any bugs found in testing.
Duration 1-2 hours

Publish:
publish to pip and git as working version 

Information gathering:
Learn how to implement GUIs in python using tkinter
Duration 2 hours

Prototype:
Build a prototype GUI with dummy data for the client
Step 1) create a window
Step 2) create a **received message box** with dummy data
Step 3) create a **message input box** for typing data
Step 4) create a send button to transmit data to message box
Step 5) create a **server connections box**


Duration 2-3 hours

Integration:
Fully Integrate the GUI with the client to send and receive messages and server connections
Step 1) get data sent to client to appear in received message box
Step 2) get data sent from message input box to transmit to server
Step 3) Update server connections box when clients connect and disconnect
Duration 5 hours.

Testing and Cleaning:
Clean up and debug print statements and make GUI look presentable
Duration 1-2 hours


Publish:
publish to pip and git as working version 

