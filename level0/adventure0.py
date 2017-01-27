'''
Created on Jan 28, 2016

@author: raydelto
'''
import ray_adventure
import mitch_adventure

def credits():
    print "First Dominations by Raydelto Hernandez and Mitch Morrison\n\n"

def start():
    credits()
    print "You are in a dark forest, you have no idea how did you get there.  The place is scary, looks like a cemetery."
    print "Two shadows suddenly approach you.  You now have two gentlemen in front of you: Ray and Mitch"
    print "Mitch told a corny joke, no one laugh, then told you that they are saving souls, you have to pick someone to guide you through your quest."
    print "Minutes in silence have passed, you're in shock incapable of making a decision, Ray approaches you and tell you: "
    print '"Listen , just pick randomly any of us , or just try to reach an exit by yourself, but we need to hurry, they are coming"'
    print " -- They ?, who are they?. You asked with no clue of what are this gentlemen talking nor how did you get to that awful place"
    print "\n\n\n"
    print"Time for a decision has arrived.  What would you like to do?"
    choice = 0
    while choice not in (1,2,3):
        choice= input("1- Choose Mitch as your guide\n2- Choose Ray as your guide\n3- Continue alone\n")
        if choice == 1:
            mitch_adventure.start()
        elif choice == 2:
            ray_adventure.start()
        elif choice == 3:
            print "You ran away, fall to the ground, and suddenly feel a sharpened object stabbing you repeteadly, everything is blurry, everything is black..."
            print "\nGAME OVER\n"
        else:
            print "Please select a valid option"    
    
    