# Lea Williams

def load_game(self, file_path):
    """
    Loads a saved game from an external JSON file
    
    Team Member: Lea Williams
    
    Techniques Claimed:
        - with statements
        - use of json.load()
        
    Problem Solved:
        Restores the player's stats, current room, and inventory so they can resume a previous session.
        
    Args:
        file_path (str): the file path of the saved JSON game file
        
    Returns:
        bool - True if the save file loaded successfully, False otherwise
        
    Side Effects:
        Overwrites self.player, self.room, and self.inventory with saved data
    """
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
        
        self.player = loaded_data["player"]
        self.room = loaded_data["room"]
        self.inventory = loaded_data["inventory"]
        return True
    
    except FileNotFoundError:
        print("File not found")
        return False
    
