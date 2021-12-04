"""
Letian Li
12/1/2021
Assignment 10.1
"""
#This code is mostly inspire by the 7.2 lectures note
from _typeshed import Self


class Pokemon_go:
    def __init__(self, name, walking_speed):
        self.name = name
        self.speed = walking_speed
        #set position at 0 
        self.location = 0
    
    def going(self):
        #The two people would have to move with different speed
        self.location += self.speed
    
    def reverse(self):
        self.position -= self.speed

    def get_position(self):
        #Return where the location that is currently at
        return self.location
    
    def display(self,header):
        print(header, self.location)

    def __str__(self):
        #Return the name of the player and the location of the player
        return(f"Name: {self.name}. Current location: {self.location} meters")

def competition():
    #Define two players
        player_1 = Pokemon_go("JoJo",50)
        player_1.append(player_1)
        player_2 = Pokemon_go("Dio",48)
        player_2.append(player_2)
        gaming = [player_1,player_2]
        for gaming in gaming:
            gaming.going()
            gaming.display("Location at:")
            if player_2 > player_1:
                return print("Player 2 has won.")
            elif player_2 < player_1:
                return print("Player 1 won the game.")

#The demo program:
def main():
    #Define two players using x and y
    x = Pokemon_go("KamenRiderOMO ",22)
    print(str(x))
    y = Pokemon_go("Yueguangzhixia",33)
    print(str(y))
    #Present their current locations
    x.going()
    x.going()
    x.going()
    x.display(f"The current location of:\n")
    y.going()
    y.display(f"The current location:\n")
    players =[x,y]
    for players in players:
        players.going()
        players.display("Current location for player:")


if __name__ =="__main__":
    main()