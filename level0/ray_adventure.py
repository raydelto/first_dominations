'''
Created on Jan 28, 2016

@author: raydelto
'''

import mitch_adventure

def start():
    print "Alright, you made a wise decision follow me";
    print "Ray took the lead and walked into the shadows of the dark night, the silence in creepy";
    print "You can only listen your footsteps, after a few meters Ray turns back and says"
    print " -- 'Oh no!', they've found us."
    print ""
    print ""
    print ""
    print"Time for a decision has arrived.  What would you like to do?"
    choice = 0
    while choice not in (1,2,3):
        choice= input("1- Ask who are them\n2- Run away\n3- Return and pick Mitch as guide for your adventure\n")
        if choice == 1:
            print "Oh my God!, what have they done to you?. You don't remember anything, do you?"
            print "You're John Morrippier world's most famous scientist , you've just discovered the new fuel based on water"
            print "The big oil companies are after you, if your new invention goes live they're all going to file bankrupcy"
            print "They have a comsorcium they've kidnapped you two years ago and did terrible things to you"
        elif choice == 2:
            print "You ran away, fall to the ground, and suddenly feel a sharpened object stabbing you repeteadly, everything is blurry, everything is black..."
            print "\nGAME OVER\n"
        elif choice == 3:
            mitch_adventure.start()            
        else:
            print "Please select a valid option"    
