import time as tm
import sys
from random import choice, randrange, randint

try:
    from termcolor import colored as clrd
except ModuleNotFoundError:
    print("\t termcolor module not found")
    print("\t install using pip install termcolor")
    exit()


'''termcolor doesnt work too well with strings
 formatting, just did some hacks and crazy
 stuff to get it work as intended
 NOTE: There could be bugs in this program 
 feel free to modify
 as far as you have a basic knowledge of 
 Object Oriented Programming
 
 originally intended for Elijah and Ubong, 
 thanks to them i re-made some old stuff
 '''

class CamelEscape():
    ''' Game class that controls the game'''
    # Holds variables needed to setup and control
    distance_apart=20
    def __init__(self):
        self.drinks                     = 4
        self.distance_travelled    = 0
        self.natives_distance      = -20
        self.user_choice             = "0" 
        self.camel_strength        = 5
        self.player_thirst            = 0
        self.lucky_oasis             = randint(1, 50)
        self.finish                      = 0
        self.current_color           = ["red", "green",
                                               "light_green",
                                                "light_yellow",
                                                "light_magenta"
                                               ]
        self.max_distance          =\
        choice((210, 280, 250))
        self.choices                   =\
         ("    A. Drink from your canteen.",
           "    B. Ahead moderate speed.",
           "    C. Ahead full speed.",
           "    D. Stop for the night.",
           "    E. Status check.",
           "    Q. Quit."
           )
        self.welcome_screen      =\
  ("    Welcome to Litangano Muscoud",
   "    Today we're playing Camel Escape,",
   "    Here's a brief preview of the game",
   "    You have stolen a camel to make your way",
   "    across the great Mobi desert.",
   "    The natives want their camel back and",
   "    are chasing you down!",
   "    Survive your desert trek and outrun the",
   "Natives...\n"
   )

    def display_welcome(self):
        # welcome function
        word = self.welcome_screen
        ''' my bad i've over used memory here
           by referencing the variable 
           self.welcome_screen to word'''
        self.typed_print(word, 1)
    
    def show_stats(self):
        remarks = (
        clrd(
        "        Drinks in canteen: {}", "green" ),
       clrd("        Miles travelled: {}", 'green'),
       clrd(
       "        The natives are {} miles behind\n",
             "green"),
      clrd(
      "        The natives are {} miles behind\n",
             "red")
             )
        self.distance_apart = abs(
        self.distance_travelled-self.natives_distance)
        # calculated distance from natives
        if self.distance_apart < 10:
            string_dist = remarks[3].format(
            self.distance_apart)
            # red text when natives are close
        else:
            string_dist = remarks[2].format(
            self.distance_apart)
            #green text when natives arent close
        print(remarks[0].format(self.drinks))
        print(remarks[1].format(
        self.distance_travelled))
        print(string_dist)#.format(string_dist))
        #print(string_dist[6:])
      
        
    def typed_print(self, word="", iter=0):
        ''' function that prints word to console
        character by character'''
        if not iter:
            for char in word:
            #sys.stdout.write(i)
             print(clrd(char, "green"), end='')
             sys.stdout.flush()
             tm.sleep(0.05)
        else:
            word_list=word
            # Sorry bad variable naming 
            # but no time for adjustment
            for word in word_list:
                for char in word:
                    #sys.stdout.write(i)
                    print(clrd(
                    char, "light_green"), end='')
                    sys.stdout.flush() 
                    # flush standard output buffer
                    tm.sleep(0.05)
                print()

    def get_choice(self):
         for word in self.choices:
             print(clrd(word, "light_yellow"))
          
         self.user_choice = str(input(clrd(
              "Your Choice?  ", "light_magenta")
              ))
                                        
    def mainLoop(self):
        #print(self.max_distance)
        self.display_welcome()
        #for word in self.choices:
        #    print(clrd(word, "light_yellow"))
        comments = ( 
          clrd(
        "        Drank from your back pack\n ", 'green'),
          clrd(
          "        You've travelled {} miles\n", "green"),
          clrd(
          "        You've regained some strength\n", 'green')
          )
        while not self.finish:
            self.get_choice()
            response = self.user_choice.lower()
            
            if response == 'a':
                if self.drinks > 0:
                    self.player_thirst =0
                    self.drinks-=1
                    self.camel_strength += 2.5
                    print(comments[0])
                else:
                    print(
                    clrd("    There are no drinks in your pack", "red"))
                           
            elif response == 'b':
                self.distance_travelled +=\
                      randint(6, 13)
                self.player_thirst += 0.5
                self.camel_strength -= 0.5
                self.natives_distance +=\
                      randint(7, 13)
                print( comments[1].format(
                      self.distance_travelled) )
                      
            elif response == 'c':
                self.distance_travelled +=\
                      randint(11, 19)
                self.player_thirst += 1
                self.camel_strength -= choice(
                      (1, 0.5,))
                self.natives_distance +=\
                      randint(10, 20)
                print( comments[1].format(
                      self.distance_travelled) )
                             
            elif response == 'd':
                self.player_thirst -= 1.5
                if self.camel_strength < 6.5:
                    self.camel_strength += 2
                    self.natives_distance +=\
                      randint(9, 15)
                    print( comments[2].format(
                    self.distance_travelled) )
                    
            elif response == 'e':
                self.show_stats()
                  
            elif response == 'q':
                sure = str(input("\tSure you wanna quit? "))
                if sure.lower() == "y":
                    self.finish=1
                    print('\t Thanks for ya time')
                    print('\t\t By ...... Noel ')
                
            else:
                print(clrd(
                  "        Invalid input\n", "red"))
                  
            if self.lucky_oasis:
                if randint(1, 50) == self.lucky_oasis:
                    print(
                    clrd("        Found an oasis\n ", "green") ) 
                    self.lucky_oasis=0
                    #set lucky to false
                    #player can only be lucky once
                    if self.player_thirst >= 2:
                        self.player_thirst -= 2
                    self.camel_strength += 2
                    self.drinks += 1
                    
            if self.player_thirst > 6.5:
                print(
                clrd("        Died of thirst..", "red") )
                self.finish=1
                break
                    
            elif self.player_thirst > 4.5:
                print(
               clrd("        You're thirsty...", "red") )
                
            if self.camel_strength < 2:
                print(clrd(
                 "        Your camel is getting tired",
                  "red"))
            elif self.camel_strength < 0.5:
                print(clrd(
                "        Your camel is dead", "red"))
                break
                    
            if self.natives_distance >=\
                self.distance_travelled:
                ''' the natives have reached or
                   overtaken you, so die!!!!'''
                print(clrd(
                 "        The natives have caught you",  "red"))
                self.finish=1
               
            elif self.distance_apart < 10:
                remark=\
              "        The natives are getting closer!\n"
                print(clrd(remark , "red"))
               
            if self.distance_travelled >\
                                self.max_distance:
                self.finish=1
                self.typed_print(
                   "\tCongratulations you've made it across the desert\n")
                print("\tBy Sylvester Noel\n")
                print("\tA.K.A Bright....")


def main():
    game = CamelEscape()
    game.mainLoop()
    if game.finish:
        print("\tY -- Yes\n\tN -- No")
        ask = str(input("\tWanna play again?  "))
        if ask == "y":
            main()
        else:
            print("\tThanks for ya time ...... ")
            exit()
            
            
if __name__ == "__main__":
    # alas call the main function
    # ------------ Sylvester Noel------------
    # Fei-ghe
    main()