# CPSC4160-BeginnerGame
Basic game engine creation to understand the Model-View-Controller design archetype. 

# Program Verions
OS Version: Windows 10
Python Version: 3.8.10
Pygame Version: 2.2.0

# Motivation
We wanted to create a simple game for our first assignment. This type of game gives us the fundamentals of game-engine development. We were able to implement simple physics with the ball, have an AI opponenet, and have a moveable player character. 

# Reasoning
We wanted to follow the Model-View-Controller design archetype that we learned in class. We kept all object attributes and values stored in the model. Had the eventController manage playerInput as well as the automatic movement of the pongball and opponent. In the view class we kept our screen variable as well as the function to update the screen. 

# Image
The View class displayed onto the screen the objects from model class, the objects inside of model class were changed inside of the eventController class. 

# Future Work
We have a cleaner way of displaying the score onto the screen where the ball doesn't get hidden behind it. We could also add a start game button, as well as some sort of way to win or lose the game instead of the score just counting infinitely. In terms of generalization, we have a good Model-View-Controller layout set up already. In the future we could store the objects inside some sort of array, to make updating them simipler than just manually editing each object involved in the game. 