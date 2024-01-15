# Monsters

class Monster():
    """Class for creating monsters"""

    def __init__(self, name, description, hp):
        """Initialize a monster with a name, description, and health points."""
        self.name = name
        self.description = description
        self.hp = hp


goblin = Monster(
    "Goblin",
    """
##################################################
# You enter a cave and you see a shape.          #
# It's wiry frame draped in tattered garments,   #
# with a crooked grin revealing jagged teeth and #
# eyes gleaming with a mischievous glint!        #
################ It's a Goblin! ##################
##################################################
""",
    5
)

ork = Monster(
    "Ork",
    """
###########################################
# You enter a cave and you see a towering #
# and brutishly built shape,              #
# its grizzled body marked with scars!    #
############## It's an Ork! ###############
###########################################""",
    5
)

murloc = Monster(
    "Murloc",
    """
###############################################
# You enter a dank cave with a pond           #
# in the middle and you see a small,          #
# amphibious creature with webbed appendages, #
# emitting gurgling sounds!                   #
############### It's a Murloc! ################
###############################################""",
    5
)

cave_troll = Monster(
    "Cave Troll",
    """
#################################################
# You enter a cave and you see a hulking figure #
# draped in crude hides, its massive frame      #
# adorned with tangled mossy hair and thick,    #
# gnarled limbs clutching a stone club,         #
# its eyes glowing with a intensity!            #
############## It's a Cave Troll! ###############
#################################################""",
    5
)

forest_troll = Monster(
    "Forest Troll",
    """
#####################################################
# You enter a opening clad with greenery a creature #
# taller than the average human,                    #
# its bark-like frame turns towards you!            #
############### It's a Forest Troll! ################
#####################################################""",
    5
)

basilisk = Monster(
    "Basilisk",
    """
#################################################
# You enter a big cave and you see a creature   #
# with shimmering scales of iridescent colors,  #
# its piercing gaze freezing the air around it, #
# a forked tongue flickering as it hisses,      #
# emanating an aura of petrifying danger!       #
############### It's a Basilisk! ################
#################################################""",
    7
)

wyvern = Monster(
    "Wyvern",
    """
#####################################################
# You enter a big cave and you see a formidable     #
# winged creature, with scaled skin shimmering      #
# in the dim light, razor-sharp talons gripping     #
# the cave floor as its leathery wings fold against #
# its sleek body, keen eyes fixated on the intruder #
# with a calculated intensity, ready to take        #
# flight at the slightest provocation!              #
################## It's a Wyvern! ###################
#####################################################""",
    7
)

black_dragon = Monster(
    "Black Dragon",
    """
#####################################################
# You enter a vast expanse of a cavern, shadows     #
# dance in the dim light. Massive scales shimmer,   #
# and fiery eyes gleam in the dark. A great ominous #
# silhouette looms wrapped in midnight scales,      #
# a force unmatched!                                #
############### It's a Black Dragon!! ###############
#####################################################
""",
    10
)
