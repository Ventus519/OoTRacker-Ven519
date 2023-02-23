dungeon_locations = ["deku", "dc", "jabu", "forest", "fire", "water", "spirit", "shadow", "well", "gtg", "ice"]
dins = 1
nocturne = 1
ocarina = 1
magic = True
zl = 1
hook_state = 1
bow_state = 1
hovers_state = 1
bomb_state = 1
bombchu_enabled = False
bombchu_state = 1

def accessible(dungeon):
    if dungeon == "Shadow":
        if dins==1 and nocturne==1 and ocarina==1 and magic == True:
            return True
        else:
            return False
def projectile_query_adult():
    if hook_state >=1 or bow_state == 1:
        return True
def explosive_query():
    if bomb_state == 1:
        return True
    if bombchu_enabled == True and bombchu_state == 1:
        return True
    else:
        return False
        
def beatable_vanilla_glitchless(dungeon):
    if dungeon == "Shadow":
        if accessible("Shadow"):
            if zl==1 and projectile_query_adult() == True and hovers_state == 1 and explosive_query() == True:
                return True
            else: 
                return False
        else:
            return False