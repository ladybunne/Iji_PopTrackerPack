from dataclasses import dataclass

@dataclass
class ThingThing:
    num: int
    name: str

thing = {
    "1": ThingThing(1, "hello"),
    "2": ThingThing(2, "egg"),
    "3": ThingThing(3, "bird"),
    "4": ThingThing(4, "nest")
}

thing2 = {
    "5": ThingThing(5, "egg"),
    "6": ThingThing(6, "egg"),
    "7": ThingThing(7, "bird"),
    "8": ThingThing(8, "nest")
}

things = {
    **thing,
    **thing2
}

# x = (key for key, thingthing in thing.items())

regions = [data.name for id, data in thing.items()]

location_groups_table = {
    group: locations for group in [data.name for id, data in thing.items()] for locations in [[location for location, data in things.items() if data.name == group]]
}

print(location_groups_table)


print("Sector 8asdlfkjasdlfkj"[:8])