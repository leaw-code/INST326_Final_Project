#Lea Williams

import json

class GameEngine:
    """
    Main game engine managing player state, rooms, and save files.
    """

    def save_game(self, file_path, player_data, current_room):
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
                player_data (dict[str, int|str]): dictionary containing current player attributes (health, stats, inventory).
                current_room (str): the unique string key representing the player’s current location

            Returns:
                Bool: True if the game was saved successfully. False if a file writing error occurred.

            Side Effects:
                Creates or overwrites a file containing the player’s progress.

            """
            
            inventory_list = player_data.get("inventory", [])
            saved_inventory = []
            
            for item in inventory_list:
                saved_inventory.append(item)
                
            save_data = {"player": player_data, "room": current_room, "inventory": saved_inventory}
            
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(save_data, f, indent=4)
                return True
            except Exception:
                return False
        
    
     
if __name__ == "__main__":
    engine = GameEngine()
    
    # Fake data to simulate a player mid-game
    test_player = {
        "name": "Hero",
        "hp": 85,
        "inventory": ["Health Potion", "Iron Sword"]
    }
    
    if engine.save_game("test_save.json", test_player, "dungeon_hall"):
        print("Game saved successfully!")
    else:
        print("Save failed!")   
    