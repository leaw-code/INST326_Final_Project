#Lea Williams

import json

class GameEngine:
    """
    Main game engine managing player state, rooms, and save files.
    """
    
     
    
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
                    
                save_data = {"player": self.player_data, "room": self.current_room, "inventory": saved_inventory}
                
                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(save_data, f, indent=4)
                    return True
                except Exception:
                    return False
            



if __name__ == "__main__":
    engine = GameEngine()
    
    # Fake data to simulate a player mid-game. Feel free to update to test your own code
    engine.player_data = {"name": "Hero", "hp": 85}
    engine.current_room = "dungeon_hall"
    engine.inventory = {"Health Potion": 1, "Iron Sword": 1}
    
    if engine.save_game("test_save.json"):
        print("Game saved successfully!")
    else:
        print("Save failed!")   