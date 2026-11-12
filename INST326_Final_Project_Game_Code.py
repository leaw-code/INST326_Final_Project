
import json, sys, random

class GameEngine:
    """
    Main game engine managing player state, rooms, and save files.
    """
    
    def __init__(self, name, world_data):
        """
        Initializes player status, current room, and empty inventory.
        
        Team Member: Lea Williams, Dagem Worku
        """
        self.world_data = world_data
        self.player = {"Name": name, 
                       "HP": 100, 
                       "Inventory": {"Health Potion": 1, 
                                    "Iron Sword": 1}
                       }
        self.prev_rooms = {}
        self.room = "Room 1"
        self.event = {"None"}
        self.inventory = {}
    
    # Constantinos Marmaras

    def add_item_to_inventory(self, item) -> None:
        """
        Adds a targeted item to the player’s inventory subject to carrying limits.

        Problem Solved:
            Manages items acquired by checking current inventory quantities, 
            enforcing a maximum stack limit of 5 per item type, 
            and updating item count dictionaries

        Args:
            item (str): string of the name to be added

        Side effects:
            Modifies the player’s inventory dictionary attribute to reflect 
            updated item counts
        """
        
        for items in self.inventory:
            if items == item:
                if self.inventory.get(item) <= 5:
                    self.inventory.get(item) + 1
        
        if item not in self.inventory:
            self.inventory[item] = 1

    # Lea Williams

    def save_game(self, file_path):
                """
                Saves the game's current variables to an external file so the game can 
                be continued later.
                
                Team Member: Lea Williams
                
                Techniques Claimed:
                    - with statements
                    - use of json.dump()
                    
                Problem Solved:
                    Saves the player’s progress, inventory, and map exploration to a 
                    file so they can stop playing and continue later.

                Args:
                    file_path (str): the destination file system path for the save file

                Returns:
                    Bool: True if the game was saved successfully. False if a file writing error occurred.

                Side Effects:
                    Creates or overwrites a file containing the player’s progress.

                """
                
                saved_inventory = {}
                
                for item, count in self.inventory.items():
                    saved_inventory[item] = count
                    
                save_data = {"player": self.player, "room": self.room, "inventory": saved_inventory}
                
                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(save_data, f, indent=4)
                    return True
                except Exception:
                    return False

    # Dagem Worku

    def navigate_room(self, direction):
        """
        Navigates a player from the current room to the next room based on 
        input, as well as determining a new event for the new room.
        
        Problem Solved: 
            Validates whether a path exists in the world map for a specified 
            direction and determines the player's next room location.
            
            Determines an event for next room location based on past events.
        
        Args:
            direction (str): Direction chosen by user (e.g "Forward", "Left")
            
        Side Effects:
            Appends room and event attributes to the prev_rooms dict (room:event).
            
            Updates the room attribute with the next room found from the 
            direction.
            
            Sets the event attribute to "None" before further checks.
            
            If game has not ended, the event for the next room is calculated and
            set to the event attribute.
        """
        good_events = self.world_data[2]["Good events"]
        bad_events = self.world_data[2]["Bad events"]
        
        try:
            self.world_data[0][self.room][direction]
        except KeyError:
            print("Invalid direction, try again.")
            return self.room
        
        self.prev_rooms.update({self.room:self.event})
        self.room = self.world_data[0][self.room][direction]
        self.event = {"None"}
        
        if self.world_data[0][self.room] == "End":
            print("""
                  Congratulations, you have won the game!
                  The game will reset now.
                  """)
            sys.exit()
        else:
            event_dif = 0
            for room in self.prev_rooms:
                event = self.prev_rooms[room]
                if event in good_events or event == "None": 
                    event_dif += 1
                else:
                    event_dif -= 1
            
            event_dif = abs(event_dif)
            
            final_dif = random.randint(0, 2 * (event_dif * 2))
            if final_dif > abs(event_dif):
                self.event = good_events[random.randint(0, len(good_events)-1)]
            else:
                self.event = bad_events[random.randint(0, len(bad_events)-1)]
                            
        print(f"Continuing to {self.room}...")
            

# Game Data (paths, rooms, events)
dungeon_paths = {"Room 1": {"Left": "Room 2", "Forward": "Room 3"},
                 "Room 2": {"Right": "Room 4"},
                 "Room 3": {"Left": "Room 5"},
                 "Room 4": "End",
                 "Room 5": "End"
                 }

dungeon_rooms = {"Room 2":{"Enemies": "Zombie",
                           "Items" : {"Leather boots": 1}
                           },
                 "Room 3":{"Enemies": "Haunted Knight",
                           "Items" : {"Katana": 1}
                           },
                 "Room 4":{"Enemies": "Bandit",
                           "Items" : {"Gold": 10}
                           },                 
                 "Room 5":{"Enemies": "Skeleton",
                           "Items" : {"Health Potion": 1}
                           },                 
                }

events = {"Bad events": ["- Weak Strikes", "- Tanky Enemies"],
          "Good events": ["+ Strong Strikes", "+ Health Boost"]}

if __name__ == "__main__":
    # Fake player name input
    engine = GameEngine("Hero", (dungeon_paths, dungeon_rooms, events))
    
    # Fake player direction decisions
    engine.navigate_room("Left")
    engine.navigate_room("Right")

    if engine.save_game("test_save.json"):
        print("Game saved successfully!")
    else:
        print("Save failed!")   