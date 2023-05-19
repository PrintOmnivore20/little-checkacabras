from BaseClasses import Item
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool


class LCItem(Item):
    game: str = "LittleCheckacabras"

#Seperate tables for each type.
junk_table = {
    "World's Most Comfortable Pair of Panties": ItemData(80200, False),
    "Its SEAMAN. SEA. MAN. Not Semen": ItemData(80201, False),
    "Ocarina of Time (1998)": ItemData(80202, False),
    "Chupacabra": ItemData(80203, False),
    "Two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda": ItemData(80204,False),
    "One Black Coffee": ItemData(80205,False),
    "Ralsei Plush": ItemData(80206,False)
}

progression_table = {
    "Checkacabra": ItemData(80000, True),
    "Random Hat": ItemData(80100, True),
}

food_table = {
    "Ice Cream": ItemData(80001,True),
    "Spaghetti": ItemData(80002,True),
    "Chicken Nuggets": ItemData(80003,True),
    "French Fries": ItemData(80004,True),
    "Junior Cheeseburger": ItemData(80005,True),
    "Double Cheeseburger": ItemData(80006,True),
    "Triple Cheeseburger": ItemData(80007,True),
    "1/3 Pound Cheeseburger": ItemData(80008,True),
    "PB&J Sandwich": ItemData(80009,True),
    "Water": ItemData(80010,True),
    "Soda": ItemData(80011,True),
    "Pizza": ItemData(80012,True),
    "???": ItemData(80013,True),
    "Kids Meal Toy": ItemData(80014,True)
}



trap_table = {
    "Worker's Strike": ItemData(80050,False),
    "Famine": ItemData(80051,False),
    "Negative Gossip": ItemData(80052,False),
}

item_table = {
    **junk_table,
    **progression_table,
    **food_table,
    **trap_table,
}

required_items = {
**progression_table
}

item_frequencies = {

}


lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}