






#Lea Williams

def save_game(self, file_path, player_data, current_room):
        """
        Saves the game's current variables to an external file so the game can 
        be continued later.
        
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