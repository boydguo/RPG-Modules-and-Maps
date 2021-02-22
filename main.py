# Course: CS 30
# Period: 1
# Date created: 02/02/21
# Date last modified: 02/02/21
# Name: Boyd Guo
# Description: RPG: Modules and Maps

import random

# map
def map():
    map = [['Drop Site                                                      '],
           ['    *         Blanc Town                                       '],
           ['                   *           Town of Salem                   '],
           ['                                     *                         '],
           ['                                                  Louisberg    '],
           ['                                                       *       '],
           ['                                               Rennes          '],
           ['                                                  *            '],
           ['                                          Rouan                '],
           ['                                            *                  '],
           ['                           Corsica                             '],
           ['                              *                                '],
           ['                  Bourges                                      '],
           ['                     *                                         '],
           ['                                   Toulon                      '],
           ['                                     *                         '],
           ['                                                  Vice         '],
           ['                                                    *          '],
           ['                                      Allied Forces            '],
           ['                                            *                  ']
           ]
    for i in map:
        print(i)


map()


# locations
locations = {"River": "A raging river that blocks your path",
             "Plains": "A seemingly peaceful plain with hidden dangers",
             "Village": "A once beautiful village now ridden with enemy forces"
             }
# map tile types
map_tiles = {"Enemy Patrol": {"description":
                              "a small squad of enemy troops hunting for \
                              stragglers",
                              "action": "engage the enemies or hide"},
             "MachineGun Nest": {"description":
                                 "a hidden ditch manned by enemy machine \
                                 gunners",
                                 "action":
                                 "engage the enemies or avoid the enemies"},
             "Sniper Nest": {"description":
                             "a enemy sniper with overwatch of a area",
                             "action":
                             "engage the enemies or avoid the enemies"},
             "Enemy Artillery": {"description":
                                 "enemy artillery that is hammering your \
                                 allies however has little to do with your \
                                 mission",
                                 "action":
                                 "take the artillery or avoid it"},
             "Enemy Convoy": {"description":
                              "a enemy convoy containing supplies, soldiers, \
                              tanks, and much more",
                              "action":
                              "die or avoid it"},
             " ": {"description":
                   "just the deafening silence for now...",
                   "action":
                   "conitnue"}
             }

# river map tile types
plains_map_tiles = {"Bridge": {"description":
                               "a hotly contested objective that could pave to \
                               road for victory",
                               "action":
                               "take the bridge or avoid it"},
                    "Broken Bridge": {"description":
                                      "a long destroyed bridge abanddoned by \
                                      all, yet it still provides a dangerous \
                                      path across",
                                      "action":
                                      "cross the remains or avoid it"}
                    }

# plains map tile types
plains_map_tiles = {"Farm House": {"description":
                                  "a abandonned farm house that may still \
                                  contain supplies",
                                  "action":
                                  "search for supplies or avoid it"},
                   "Windmill": {"description":
                                "a safe haven for tired soliders seeking \
                                shelter",
                                "action":
                                "take a rest or continue on your mission"}
                   }



def locations(locations):
    """Function for determining random locations"""
    ev = random.choice(locations)
    ev(locations)