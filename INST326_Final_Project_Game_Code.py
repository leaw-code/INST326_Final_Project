
import json, sys, random

class GameEngine:
    """
    Main game engine managing player state, rooms, and save files.
    """
    
    def __init__(self, name, world_data):
        """
        Initializes world_data, player, prev_rooms, room, event, and inventory.
        
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
        self.event = "None"
        self.inventory = {}
        self.inv_capacity = 4
    

    def add_item_to_inventory(self, item) -> None:
        """
        Writer: Constnatinos Marmaras
        
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
                    self.inventory[item] += 1
        
        if item not in self.inventory:
            if len(self.inventory) < self.inv_capacity:
                self.inventory[item] = 1
            else:
                print(
                    f"Inventory capacity of {self.inv_capacity} has been reached. "
                    "If you wish to pick up this item, please drop something "
                    "from your inventory."
                    )
            

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
        good_events = self.world_data[1]["Good events"]
        bad_events = self.world_data[1]["Bad events"]
        
        try:
            self.world_data[0][self.room][direction]
        except KeyError:
            print("Invalid direction, try again.")
            return self.room
        
        self.prev_rooms.update({self.room:self.event})
        self.room = self.world_data[0][self.room][direction]
        self.event = "None"
        
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
                            
        print(f"Continuing to {self.room} with [{self.event}] event...")

    # Preston Baldwin
        # Parts of this method may change depending on later implementation of enemy_type
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
        while self.player["HP"] > 0 and len(enemies) > 0:

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
                self.player["HP"] -= enemy_damage
                print(f"You took {enemy_damage} damage!")

        # Determine the battle outcome
        if self.player["HP"] <= 0:
            return {"xp": 0.0, "item": "None", "result": "Defeat"}

        else:
            # Award rewards for winning
            xp = float(enemy_count * 10)
            item = "Health Potion"

            self.add_item_to_inventory(item)

            return {"xp": xp, "item": item, "result": "Victory"}                        

# Game Data (paths, rooms, events)
dungeon_paths = {"Room 1": {"Left": "Room 2", "Forward": "Room 3"},
                 "Room 2": {"Right": "Room 4"},
                 "Room 3": {"Left": "Room 5"},
                 "Room 4": "End",
                 "Room 5": "End"
                 }

events = {"Bad events": ["- Weak Strikes", "- Tanky Enemies"],
          "Good events": ["+ Strong Strikes", "+ Health Boost"]}
    
if __name__ == "__main__":
    # Fake player name input
    engine = GameEngine("Hero", (dungeon_paths, events))
    
    # Fake player direction decisions
    engine.navigate_room("Left")
    engine.navigate_room("Right")

    if engine.save_game("test_save.json"):
        print("Game saved successfully!")
    else:
        print("Save failed!")   