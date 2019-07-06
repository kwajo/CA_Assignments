 #Development Log  (2.07.19)


Wrote most of the program to a  level im happy with and this is my first development log.
At this point I’m looking at ways of adding small improvements to the code to include extra features. 

I have an issue where if you talk in the cli it double prints and looks ugly so I’m thinking of getting rid of the entire cli as a chat interface (so it’s only needed to start the program)


I’m currently adding a kick command so that I can selectively kick users from the server and if I get the chance I’d like to add a votekick command for users as well as an option to change their text colour (but that may be too troublesome)




# Development Log (2) (5.07.19)


The project and documentation is almost complete. There were a few additional features that I wanted to add such as naming yourself in the server, changing text colours and background, including argparse (which really is far more practical than my solution) and allowing clients to whisper one another. However due to time constraints and poorly written code/decisions early on i’ve decided to leave the project as is.  There may still be a few crash cases as it’s hard to simulate a live session and user input however the majority of crashes are not too severe so I’m happy with how things have gone.

Given more time I would have written a client subclass that included user preferences.
