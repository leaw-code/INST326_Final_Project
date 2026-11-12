
import json

class GameEngine:
    """
    Main game engine managing player state, rooms, and save files.
    """
    
    def __init__(self):
        """
        Initializes player status, current room, and empty inventory.
        
        Team Member: Lea Williams
        """
        self.player_data = {"name": "Hero", "hp": 100}
        self.current_room = "entrance"
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

#Lea Williams

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
    
    #Preston Baldwin
        #Parts of this method may change depending on later implementation of enemy_type
    def combat(self, enemy_type: list[str] | str, enemy_count: int = 1) -> dict[str, float | str]:
        """
        Starts a turn based battle between the player and enemies.

        Problem Solved:
            Handles combat by allowing the player and enemies to attack,
            updating health, and determining rewards after battle.

        Args:
            enemy_type (list[str] | str): Name or category of enemies.
            enemy_count (int): Number of enemies in the battle.

        Returns:
            dict: Combat results including XP and item rewards.

        Side Effects:
            Updates player health and awards items to inventory.
        """

        # Makes sure enemy_type is a list
        if isinstance(enemy_type, str):
            enemy_type = [enemy_type]

        # Create enemies with 30 health each
        enemies = []
        for i in range(enemy_count):
            enemies.append({
                "type": enemy_type[i % len(enemy_type)],
                "hp": 30
            })

        # Continue fighting while the player and enemies are alive
        while self.player_data["hp"] > 0 and len(enemies) > 0:

            # Player attacks the first remaining enemy
            damage = random.randint(10, 20)
            enemies[0]["hp"] -= damage

            print(f"You dealt {damage} damage!")

            # Check if the enemy was defeated
            if enemies[0]["hp"] <= 0:
                defeated_enemy = enemies.pop(0)
                print(f"{defeated_enemy['type']} was defeated!")

            # If enemies remain, they attack the player
            if len(enemies) > 0:
                enemy_damage = random.randint(5, 15)
                self.player_data["hp"] -= enemy_damage
                print(f"You took {enemy_damage} damage!")

        # Determine the battle outcome
        if self.player_data["hp"] <= 0:
            return {"xp": 0.0, "item": "None", "result": "Defeat"}

        else:
            # Award rewards for winning
            xp = float(enemy_count * 10)
            item = "Health Potion"

            self.add_item_to_inventory(item)

            return {"xp": xp, "item": item, "result": "Victory"}            



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