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
    'Goblin',
    f"""a monster.
It's wiry frame draped in tattered garments,
with a crooked grin revealing jagged teeth and
eyes gleaming with a mischievous glint""",
    5
)
ork = Monster(
    'Ork',
    'a towering and brutishly built shape, its grizzled body marked with scars',
    5
)
murloc = Monster(
    'Murloc',
    f"""a small, amphibious creature with webbed appendages,
emitting gurgling sounds""",
    5
)
cave_troll = Monster(
    'Cave Troll',
    f"""a hulking figure draped in crude hides,
its massive frame adorned with tangled mossy hair and thick,
gnarled limbs clutching a stone club,
its eyes glowing with a primal, fierce intensity""",
    5
)
forest_troll = Monster(
    'Forest Troll',
    'a creature taller than the average human, its rugged, bark-like skin',
    5
)
basilisk = Monster(
    'Basilisk',
    f"""a serpentine creature with shimmering scales of iridescent hues,
its piercing gaze freezing the air around it,
a forked tongue flickering as it hisses,
emanating an aura of petrifying danger""",
    5
)
wyvern = Monster(
    'Wyvern',
    f"""a formidable winged creature,
with scaled skin shimmering in the dim light, razor-sharp talons gripping
the cave floor as its leathery wings fold against its sleek body,
keen eyes fixated on the intruder with a calculated intensity,
ready to take flight at the slightest provocation""",
    5
)