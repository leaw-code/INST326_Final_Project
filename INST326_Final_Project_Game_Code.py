






#Lea Williams

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
        
        rooms_visited = []
        save_data = {"player": player_data, "room": current_room, "past_rooms": rooms_visited}
        
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(json.dump(save_data, f, indent=4))
        except:
        
        inventory_list = player_data.get("inventory", [])
        
        for item in inventory_list:
            # rooms_visited.append(current_room)
            
        