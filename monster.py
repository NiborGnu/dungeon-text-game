# Monsters


class Monster():
    """
    Creating monsters
    """
    def __init__(self, name, description, hp):
        self.name = name
        self.description = description
        self.hp = hp


goblin = Monster(
    " Goblin",
    f"""
You enter a cave and you see a shape.
It's wiry frame draped in tattered garments,
with a crooked grin revealing jagged teeth and
eyes gleaming with a mischievous glint, """,
    5
)
ork = Monster(
    " Ork",
    f"""
You enter a cave and you see a towering
and brutishly built shape,
its grizzled body marked with scars, """,
    5
)
murloc = Monster(
    " Murloc",
    f"""
You enter a dank cave with a pond
in the middle and you see a small,
amphibious creature with webbed appendages,
emitting gurgling sounds, """,
    5
)
cave_troll = Monster(
    " Cave Troll",
    f"""
You enter a cave and you see a hulking figure
draped in crude hides, its massive frame
adorned with tangled mossy hair and thick,
gnarled limbs clutching a stone club,
its eyes glowing with a intensity, """,
    5
)
forest_troll = Monster(
    " Forest Troll",
    f"""
You enter a opening clad with greenery a creature
taller than the average human,
its bark-like frame turns towards you, """,
    5
)
basilisk = Monster(
    " Basilisk",
    f"""
You enter a big cave and you see a creature
with shimmering scales of iridescent colors,
its piercing gaze freezing the air around it,
a forked tongue flickering as it hisses,
emanating an aura of petrifying danger, """,
    7
)
wyvern = Monster(
    " Wyvern",
    f"""
You enter a big cave and you see a formidable
winged creature, with scaled skin shimmering
in the dim light, razor-sharp talons gripping
the cave floor as its leathery wings fold against
its sleek body, keen eyes fixated on the intruder
with a calculated intensity, ready to take
flight at the slightest provocation, """,
    7
)
black_dragon = Monster(
    " Black Dragon",
    f"""
You enter a vast expanse of a cavern, shadows
dance in the dim light. Massive scales shimmer,
and fiery eyes gleam in the dark. A great ominous
silhouette looms wrapped in midnight scales,
a force unmatched """,
    10
)