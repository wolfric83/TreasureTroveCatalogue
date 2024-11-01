import mongoengine as me

# Base Item class
class Item(me.Document):
    item_id = me.IntField(required=True, unique=True)
    name = me.StringField(required=True)
    description = me.StringField()
    categories = me.ListField(me.StringField())
    rarity_value = me.IntField(min_value=0, max_value=100, default=0)
    rarity_name = me.StringField()
    weight = me.FloatField(required=True)
    value = me.IntField(required=True)
    flavor_text = me.StringField()
    
    meta = {'allow_inheritance': True}  # Enables subclass inheritance for MongoEngine

    def clean(self):
        rarity_scale = {
            "Dirt": (0, 10),
            "Common": (11, 30),
            "Uncommon": (31, 50),
            "Rare": (51, 70),
            "Epic": (71, 90),
            "Legendary": (91, 100)
        }
        for name, (min_val, max_val) in rarity_scale.items():
            if min_val <= self.rarity_value <= max_val:
                self.rarity_name = name
                break

# Subclass for Weapons
class Weapon(Item):
    damage_range = me.DictField(required=True)  # e.g., {"min": 10, "max": 20}
    damage_type = me.StringField()              # e.g., "Physical" or "Magical"
    weapon_subclass = me.StringField()  
    required_skill = me.StringField()           # e.g., "Swordsmanship"
    durability = me.IntField(default=100)       # Base Durability

# Subclass for Armor
class Armor(Item):
    defense_rating = me.IntField(required=True)
    armor_wear_location  = me.StringField()
    armor_subclass = me.StringField()
    armor_type = me.StringField()               # e.g., "Heavy", "Light"
    elemental_resistance = me.DictField()       # e.g., {"fire": 10, "ice": 5}
    durability = me.IntField(default=100)       # Base Durability

# Subclass for Potions
class Potion(Item):
    effect = me.StringField(required=True)      # e.g., "Restores 50 HP"
    duration = me.StringField()                 # e.g., "Instant"
    is_consumable = me.BooleanField(default=True)

# Subclass for Trade Goods
class TradeGood(Item):
    quality = me.StringField()                  # e.g., "Standard", "High"
    origin = me.StringField()                   # Where the item is from
    is_tradeable = me.BooleanField(default=True)