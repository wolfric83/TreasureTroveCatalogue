import mongoengine as me

me.connect(host="localhost", alias='default')

# Base Item class
class Item(me.Document):
    item_id = me.StringField(required=True, unique=True)
    name = me.StringField(required=True)
    description = me.StringField()
    categories = me.ListField(me.StringField())
    rarity_value = me.IntField(min_value=0, max_value=100, default=0)
    rarity_name = me.StringField()
    weight = me.FloatField(required=True)
    value = me.IntField(required=True)
    flavor_text = me.StringField()

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

item = Item(
    item_id="weapon_001",
    name="Iron Sword",
    description="A sturdy iron sword with a sharp edge.",
    categories=["Weapon", "Basic Equipment"],
    rarity_value=45,  # Should be "Uncommon"
    weight=5.0,
    value=25,
    flavor_text="A reliable weapon for any adventurer.",
)

item.save()