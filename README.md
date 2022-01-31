# pygame_collisions


The most recent version of the project is collisions.py which includes a user input (via number keys) to select from 1 - to 9 squares.





learning basic collision physics in pygames

After following several tutorials to create an object that could be moved on key press,
I realised that I wanted to create an object that moved by itself, responding to the screen boundaries and other objects.

I had the idea to include sounds on each collision to create a minimal virtual sound performance.

My inital code (collision_test_1) was based loosely around a previous tutorial and included images and use of a character class, but things became untidy and I ran into several issues which became difficult to fix in a code that was becoming more and more untidy.

To increase my understanding of the collision physics I watched another tutorial and created a new code (collision_test_2),
which used rects (basic shapes) and implemented a neater collision method, between boundaries and two independently moving objects.
https://www.youtube.com/watch?v=1_H7InPMjaY&list=PL8ui5HK3oSiHnIdi0XIAVXHAeulNmBrLy&index=9&t=0s

I ran the code but eventually found several glitches that would occur, including one of the shapes being pushed off screen - so I modified the code and fixed this.

I then increased the movement of the second shape to increase the number and variety of object collisions, and then modified it so that its trajectory was affected by the first shape.

The code was becoming inconcise and messy so I updated it by creating a class (collision_class test)
