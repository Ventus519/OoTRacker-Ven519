import pygame



#screen
screenHeight = 1000
screenWidth = 1000

pygame.init()

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Ocarina of Time 3D Randomizer Tracker - Ven519")


def projectile_query(age):
    if age == "adult":
      if hookshotState >=1 or bowState == 1:
        return True
    elif age == "child":
      if boomerangState == 1 or slingshotState == 1:
        return True
def beatable_vanilla_glitchless(dungeon):
    if dungeon=="deku":
      if accessible("deku") and slingshotState == 1: 
        return True
      else:
         return False
    if dungeon == "dc":
      if accessible("dc") and explosive_query(): 
        return True
      else:
         return False
    if dungeon == "jabu": 
      if accessible("jabu") and boomerangState == 1:
        return True
      else:
        return False
    if dungeon == "forest":
      if accessible("forest"):
        if strengthState>=1 and bowState == 1 and hookshotState >=1 and boss_keys[3]:
          return True
        else: 
          return False
      else:
        return False
    if dungeon == "fire":
      if accessible("fire"):
        if hammerState == 1 and tunicState == (1 or 3) and bowState== 1 and hookshotState>=1 and explosive_query() and boss_keys[4]:
          return True
        else:
          return False
      else:
        return False
    if dungeon == "water":
      if accessible("water"):
        if hookshotState>=1 and bowState == 1 and bootState == (1 or 3) and ocarinaState >= 1 and zl == True and explosive_query() and boss_keys[5]:
          return True
        else:
          return False
      else:
        return False
    if dungeon == "spirit":
      if accessible("spirit"):
        if mirrorState ==1 and strengthState>=2 and ocarinaState >=1 and zl == True and hookshotState>=1 and explosive_query() and obtained_keys[7] >= 3 and boss_keys[7]:
          return True
        else:
          return False
      else:
        return False
    if dungeon == "shadow":
        if accessible("shadow"):
            if zl==True and projectile_query("adult") == True and bootState >= 2 and explosive_query() and obtained_keys[6] ==5 and boss_keys[6]:
                return True
            else: 
                return False
        else:
            return False



def accessible(dungeon_location):
    if dungeon_location == "deku":
      return True
    if dungeon_location=="dc":
      if explosive_query() or strengthState ==1:
        return True
      else:
        return False
    if dungeon_location == "jabu":
      if zora_fountain_query("child"):
        return True
      else:
        return False
    if dungeon_location == "forest":
      if hookshotState>=1 and ocarinaState >=1:
        if minuet == True or sarias == True:
          return True
        else: 
          return False
      else:
        return False
    if dungeon_location == "fire":
      if (bolero == True) or hookshotState >=1:
        if explosive_query() == True or bowState>=1 or strengthState>=1:
          return True
        elif hammerState == 1 and bootState>=2:
          return True
        else:
          return False
      else:
        return False
    if dungeon_location == "water":
      if bootState == (1 or 3) and hookshotState>=1:
        return True
      elif scale== 2 and hookshotState == 2:
        return True
      else:
        return False
    if dungeon_location == "spirit":
      if desert_query("adult") or desert_query("child"):
        return True
      else:
        return False
    if dungeon_location == "shadow":
        if dins==1 and nocturne==True and ocarinaState>=1 and magic == True:
            return True
        else:
            return False
    if dungeon_location == "ganon":
       if reward_query(dungeon_reward_type):
          return True
       else:
          return False
    

def explosive_query():
    if bombState == 1:
        return True
    elif bombchu_enabled == True and bombchuState == 1:
        return True
    else:
        return False
def desert_query(age):
  if age == "adult":
    if requiem:
      return True  
    if magic ==1 and lens == 1:
      if hookshotState == 2 and gerudo_card == 1:
        return True      
      elif epona ==False and gerudo_card ==1 and bootState>=2:
        return True
      else:
        return False
    else:
      return False
  if age == "child":
    if requiem:
      return True
    else:
      return False

def zora_fountain_query(age):
  if age == "child":
    if letter:
      if scale >=1:
        return True
      elif explosive_query()==True and zl ==1 and ocarinaState >=1:
        return True
    else:
      return False
  if age == "adult":
    if zl == 1 and ocarinaState>= 1 and letter == 1:
      return True
    else:
      return False

def reward_query(dungeon_reward_type):
    if dungeon_reward_type == "any":
      if rewards_collected == dungeon_reward_amount:
         return True
      else:
         return False
    if dungeon_reward_type == "medallion":
      if medallions_collected == dungeon_reward_amount:
         return True
      else: 
         return False
    if dungeon_reward_type == "stone":
       if stones_collected == dungeon_reward_amount:
          return True
       else:
          return False





#image loading
"""
All of these images used are under "fair use" in Nintendo's image liscence which can be found here https://www.nintendo.co.jp/networkservice_guideline/en/index.html
This is under "fair use" because I also include my own creativity with how to use these items (this is not an art gallery)

"""
go_mode_image = pygame.image.load("assets/images/OoT/go_mode.png").convert_alpha()  #this image was found under "sprites" and model "SS" found here https://zelda.fandom.com/wiki/Triforce 
  #default item loading
default_hookshot = pygame.image.load("assets/images/OoT/items/inv/progressive/hookshot/hookshot_0.png").convert_alpha() #this image was edited by me based on the image of hookshot which is linked when defining the variable "hookshot"
default_bow = pygame.image.load("assets/images/OoT/items/inv/bow/bow_gray.png").convert_alpha() #this image was edited by me based on the image of bow which is linked when defining the variable "bow"
default_boots = pygame.image.load("assets/images/OoT/items/inv/boots/boots_0.png").convert_alpha() #this image can be found here under "kokiri boots" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
default_bombs = pygame.image.load("assets/images/OoT/items/inv/misc/default/bombs.png").convert_alpha() #this image was edited by me based on the image of bombs which is linked when defining the variable "bombs"
default_hammer = pygame.image.load("assets/images/OoT/items/inv/misc/default/hammer.png").convert_alpha()#this image was edited by me based on the image of hammer which is linked when defining the variable "hammer"
default_magic = pygame.image.load("assets/images/OoT/items/gear/magic/magic_0.png").convert_alpha() #this image was edited by me based on the image of magic which is linked when defining the variable "magic_1"
default_boomerang = pygame.image.load("assets/images/OoT/items/inv/misc/default/boomerang.png").convert_alpha() #this image was edited by me based on the image of boomerang which is linked when defining the variable "boomerang"
  
  #obtained item loading
magic_1 = pygame.image.load("assets/images/OoT/items/gear/magic/magic.png").convert_alpha()#this image can be found here under "Magic Jar" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
magic_2 = pygame.image.load("assets/images/OoT/items/gear/magic/double_magic.png").convert_alpha()#this image can be found here under "Magic Jar" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

hookshot = pygame.image.load("assets/images/OoT/items/inv/progressive/hookshot/hook.png").convert_alpha()#this image can be found here under "Hookshot" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
longshot = pygame.image.load("assets/images/OoT/items/inv/progressive/hookshot/long.png").convert_alpha()#this image can be found here under "Longshot" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

bombs = pygame.image.load("assets/images/OoT/items/inv/misc/clicked/bombs.png").convert_alpha() #this image can be found here under "Bomb" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

bow = pygame.image.load("assets/images/OoT/items/inv/bow/bow.png").convert_alpha() #this image can be found here under "Fairy Bow" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

hammer = pygame.image.load("assets/images/OoT/items/inv/misc/clicked/hammer.png").convert_alpha() #this image can be found here under "Megaton Hammer" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

boomerang = pygame.image.load("assets/images/OoT/items/inv/misc/clicked/boomerang.png").convert_alpha() #this image can be found here under "Boomerang" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

fire_arrow = pygame.image.load("assets/images/OoT/items/inv/bow/fire_arrow.png").convert_alpha() #this image can be found here under "Fire Arrow" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
light_arrow = pygame.image.load("assets/images/OoT/items/inv/bow/light_arrow.png").convert_alpha() #this image can be found here under "Light Arrow" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
fire_light_mix = pygame.image.load("assets/images/OoT/items/inv/bow/fire_light_mix.png").convert_alpha() #this image was edited by combining parts of "fire_arrow" and "light_arrow" by me
arrow_0 = pygame.image.load("assets/images/OoT/items/inv/bow/arrow_0.png").convert_alpha() #this image was edited by me and is based on the image of fire arrow

hovers = pygame.image.load("assets/images/OoT/items/inv/boots/hovers.png").convert_alpha() #this image can be found here under "Hover Boots" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
irons = pygame.image.load("assets/images/OoT/items/inv/boots/irons.png").convert_alpha() #this image can be found here under "Iron Boots" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
iron_hovers_mix = pygame.image.load("assets/images/OoT/items/inv/boots/iron_hovers_mix.png").convert_alpha() #this image was edited by combining parts of "hovers" and "irons" by me

  #dungeon reward loading - medallions
default_light = pygame.image.load("assets/images/OoT/items/gear/medallion/gray/light_medallion.png").convert_alpha() #this image was edited by me based on the image "light_medallion" found when defining "clicked_light"
clicked_light = pygame.image.load("assets/images/Oot/items/gear/medallion/clicked/light_medallion.png").convert_alpha() #this image can be found here under "Light Medallion" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

default_forest = pygame.image.load("assets/images/OoT/items/gear/medallion/gray/forest.png").convert_alpha() #this image was edited by me and is based on the image of forest medallion
clicked_forest = pygame.image.load("assets/images/OoT/items/gear/medallion/clicked/forest.png").convert_alpha() #this image can be found here under "Forest Medallion" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

default_fire = pygame.image.load("assets/images/OoT/items/gear/medallion/gray/fire.png").convert_alpha() #this image was edited by me and is based on the image of fire medallion
clicked_fire = pygame.image.load("assets/images/OoT/items/gear/medallion/clicked/fire.png").convert_alpha()  #this image can be found here under "Fire Medallion" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

default_water = pygame.image.load("assets/images/OoT/items/gear/medallion/gray/water.png").convert_alpha() #this image was edited by me and is based on the image of water medallion
clicked_water = pygame.image.load("assets/images/OoT/items/gear/medallion/clicked/water.png").convert_alpha()  #this image can be found here under "Water Medallion" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

default_spirit = pygame.image.load("assets/images/OoT/items/gear/medallion/gray/spirit.png").convert_alpha() #this image was edited by me and is based on the image of spirit medallion
clicked_spirit = pygame.image.load("assets/images/OoT/items/gear/medallion/clicked/spirit.png").convert_alpha()  #this image can be found here under "Spirit Medallion" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

default_shadow = pygame.image.load("assets/images/OoT/items/gear/medallion/gray/shadow.png").convert_alpha() #this image was edited by me and is based on the image of shadow medallion
clicked_shadow = pygame.image.load("assets/images/OoT/items/gear/medallion/clicked/shadow.png").convert_alpha()  #this image can be found here under "Shadow Medallion" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

  #dungeon rewards - stones
emerald = pygame.image.load("assets/images/OoT/items/gear/stones/emerald.png").convert_alpha()  #this image can be found here under "Kokiri's Emerald" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
emerald = pygame.image.load("assets/images/OoT/items/gear/stones/emerald_0.png").convert_alpha()  #this image was edited by me and is based on the image of kokiri's emerald
ruby = pygame.image.load("assets/images/OoT/items/gear/stones/ruby.png").convert_alpha()  #this image can be found here under "Goron's Ruby" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
ruby = pygame.image.load("assets/images/OoT/items/gear/stones/ruby_0.png").convert_alpha() #this image was edited by me and is based on the image of goron's ruby
sapphire = pygame.image.load("assets/images/OoT/items/gear/stones/sapphire.png").convert_alpha()  #this image can be found here under "Zora's Sapphire" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
sapphire = pygame.image.load("assets/images/OoT/items/gear/stones/sapphire_0.png").convert_alpha() #this image was edited by me and is based on the image of zora's sapphire

  #gear image loading
      #default items - not obtained

      #obtained items
scale_1 = pygame.image.load("assets/images/OoT/items/gear/scale/scale_1.png").convert_alpha()  #this image can be found here under "Silver Scale" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
scale_2 = pygame.image.load("assets/images/OoT/items/gear/scale/scale_2.png").convert_alpha()  #this image can be found here under "Golden Scale" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

shield_0 = pygame.image.load("assets/images/OoT/items/gear/shield/deku.png").convert_alpha()  #this image can be found here under "Deku Shield" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
shield_1 = pygame.image.load("assets/images/OoT/items/gear/shield/hylian.png").convert_alpha()  #this image can be found here under "Hylian Shield" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
shield_2 = pygame.image.load("assets/images/OoT/items/gear/shield/mirror.png").convert_alpha()  #this image can be found here under "Mirror Shield" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D

  #dungeon items
small_key = pygame.image.load("assets/images/OoT/items/dungeon/small_key.png").convert_alpha()  #this image can be found here under "Small Key" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
forest_small = pygame.image.load("assets/images/OoT/items/dungeon/forest/forest_small.png").convert_alpha() #this image was edited by me and is based on the image of small key
forest_small_1 = pygame.image.load("assets/images/OoT/items/dungeon/forest/forest_small_1.png").convert_alpha() #this image was edited by me and is based on the image of small key
forest_small_2 = pygame.image.load("assets/images/OoT/items/dungeon/forest/forest_small_2.png").convert_alpha() #this image was edited by me and is based on the image of small key
forest_small_3 = pygame.image.load("assets/images/OoT/items/dungeon/forest/forest_small_3.png").convert_alpha() #this image was edited by me and is based on the image of small key
forest_small_4 = pygame.image.load("assets/images/OoT/items/dungeon/forest/forest_small_4.png").convert_alpha() #this image was edited by me and is based on the image of small key
forest_small_5 = pygame.image.load("assets/images/OoT/items/dungeon/forest/forest_small_5.png").convert_alpha() #this image was edited by me and is based on the image of small key
forest_boss = pygame.image.load("assets/images/OoT/items/dungeon/forest/forest_boss.png").convert_alpha() #this image was edited by me and is based on the image of boss key

fire_small = pygame.image.load("assets/images/OoT/items/dungeon/fire/fire_small.png").convert_alpha() #this image was edited by me and is based on the image of small key
fire_small_1 = pygame.image.load("assets/images/OoT/items/dungeon/fire/fire_small_1.png").convert_alpha() #this image was edited by me and is based on the image of small key 
fire_small_2 = pygame.image.load("assets/images/OoT/items/dungeon/fire/fire_small_2.png").convert_alpha() #this image was edited by me and is based on the image of small key
fire_small_3 = pygame.image.load("assets/images/OoT/items/dungeon/fire/fire_small_3.png").convert_alpha() #this image was edited by me and is based on the image of small key 
fire_small_4 = pygame.image.load("assets/images/OoT/items/dungeon/fire/fire_small_4.png").convert_alpha() #this image was edited by me and is based on the image of small key
fire_small_5 = pygame.image.load("assets/images/OoT/items/dungeon/fire/fire_small_5.png").convert_alpha() #this image was edited by me and is based on the image of small key
fire_small_6 = pygame.image.load("assets/images/OoT/items/dungeon/fire/fire_small_6.png").convert_alpha() #this image was edited by me and is based on the image of small key
fire_small_7 = pygame.image.load("assets/images/OoT/items/dungeon/fire/fire_small_7.png").convert_alpha() #this image was edited by me and is based on the image of small key
fire_small_8 = pygame.image.load("assets/images/OoT/items/dungeon/fire/fire_small_8.png").convert_alpha() #this image was edited by me and is based on the image of small key
fire_boss = pygame.image.load("assets/images/OoT/items/dungeon/fire/fire_boss.png").convert_alpha() #this image was edited by me and is based on the image of boss key

water_small = pygame.image.load("assets/images/OoT/items/dungeon/water/water_small.png").convert_alpha() #this image was edited by me and is based on the image of small key
water_small_1 = pygame.image.load("assets/images/OoT/items/dungeon/water/water_small_1.png").convert_alpha() #this image was edited by me and is based on the image of small key
water_small_2 = pygame.image.load("assets/images/OoT/items/dungeon/water/water_small_2.png").convert_alpha() #this image was edited by me and is based on the image of small key
water_small_3 = pygame.image.load("assets/images/OoT/items/dungeon/water/water_small_3.png").convert_alpha() #this image was edited by me and is based on the image of small key
water_small_4 = pygame.image.load("assets/images/OoT/items/dungeon/water/water_small_4.png").convert_alpha() #this image was edited by me and is based on the image of small key
water_small_5 = pygame.image.load("assets/images/OoT/items/dungeon/water/water_small_5.png").convert_alpha() #this image was edited by me and is based on the image of small key
water_small_6 = pygame.image.load("assets/images/OoT/items/dungeon/water/water_small_6.png").convert_alpha() #this image was edited by me and is based on the image of small key
water_boss = pygame.image.load("assets/images/OoT/items/dungeon/water/water_boss.png").convert_alpha() #this image was edited by me and is based on the image of boss key

shadow_small = pygame.image.load("assets/images/OoT/items/dungeon/shadow/shadow_small.png").convert_alpha() #this image was edited by me and is based on the image of small key
shadow_small_1 = pygame.image.load("assets/images/OoT/items/dungeon/shadow/shadow_small_1.png").convert_alpha() #this image was edited by me and is based on the image of small key
shadow_small_2 = pygame.image.load("assets/images/OoT/items/dungeon/shadow/shadow_small_2.png").convert_alpha() #this image was edited by me and is based on the image of small key
shadow_small_3 = pygame.image.load("assets/images/OoT/items/dungeon/shadow/shadow_small_3.png").convert_alpha() #this image was edited by me and is based on the image of small key
shadow_small_4 = pygame.image.load("assets/images/OoT/items/dungeon/shadow/shadow_small_4.png").convert_alpha() #this image was edited by me and is based on the image of small key
shadow_small_5 = pygame.image.load("assets/images/OoT/items/dungeon/shadow/shadow_small_5.png").convert_alpha() #this image was edited by me and is based on the image of small key
shadow_boss = pygame.image.load("assets/images/OoT/items/dungeon/shadow/shadow_boss.png").convert_alpha() #this image was edited by me and is based on the image of boss key

spirit_small = pygame.image.load("assets/images/OoT/items/dungeon/spirit/spirit_small.png").convert_alpha() #this image was edited by me and is based on the image of small key
spirit_small_1 = pygame.image.load("assets/images/OoT/items/dungeon/spirit/spirit_small_1.png").convert_alpha() #this image was edited by me and is based on the image of small key
spirit_small_2 = pygame.image.load("assets/images/OoT/items/dungeon/spirit/spirit_small_2.png").convert_alpha() #this image was edited by me and is based on the image of small key
spirit_small_3 = pygame.image.load("assets/images/OoT/items/dungeon/spirit/spirit_small_3.png").convert_alpha() #this image was edited by me and is based on the image of small key
spirit_small_4 = pygame.image.load("assets/images/OoT/items/dungeon/spirit/spirit_small_4.png").convert_alpha() #this image was edited by me and is based on the image of small key
spirit_small_5 = pygame.image.load("assets/images/OoT/items/dungeon/spirit/spirit_small_5.png").convert_alpha() #this image was edited by me and is based on the image of small key
spirit_boss = pygame.image.load("assets/images/OoT/items/dungeon/spirit/spirit_boss.png").convert_alpha() #this image was edited by me and is based on the image of boss key

dungeon_map = pygame.image.load("assets/images/OoT/items/dungeon/map.png").convert_alpha()  #this image can be found here under "Dungeon Map" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
compass = pygame.image.load("assets/images/OoT/items/dungeon/compass.png").convert_alpha()  #this image can be found here under "Compass" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
boss_key = pygame.image.load("assets/images/OoT/items/dungeon/boss_key.png").convert_alpha()  #this image can be found here under "Boss Key" https://zelda.fandom.com/wiki/Items_in_Ocarina_of_Time_3D
boss_key_default = pygame.image.load("assets/images/OoT/items/dungeon/boss_key_gray.png").convert_alpha()

ganon_small_1 = pygame.image.load("assets/images/OoT/items/dungeon/ganon_small_1.png") #this image was edited by me and is based on the image of small key
ganon_small_2 = pygame.image.load("assets/images/OoT/items/dungeon/ganon_small_2.png") #this image was edited by me and is based on the image of small key



#classes for defining image, scale, and location
class imageScaling():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(
        image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

  def draw(self):
     screen.blit(self.image, (self.rect.x, self.rect.y))

     
start = True
run = True


#item scaling - default items
go_mode_image = imageScaling(0, 600, go_mode_image, 3)
default_hookshot = imageScaling(0, 75, default_hookshot, 1.5)
default_bow = imageScaling(0, 0, default_bow, 1.5)
default_arrow = imageScaling(75, 0, arrow_0, 1.5)
default_boots = imageScaling(75, 75, default_boots, 1.5)
default_magic = imageScaling(150, 0, default_magic, 1.5)
default_boomerang = imageScaling(150, 75, default_boomerang, 1.5)

magic_1 = imageScaling(150, 0, magic_1, 1.5)
magic_2 = imageScaling(150, 0, magic_2, 1.5)

hovers = imageScaling(75, 75, hovers, 1.5)
irons = imageScaling(75, 75, irons, 1.5)
iron_hovers_mix = imageScaling(75, 75, iron_hovers_mix, 1.5)

default_forest = imageScaling(150, 150, default_forest, 1.5)
default_fire = imageScaling(150, 225, default_fire, 1.5)
default_water = imageScaling(150, 300, default_water, 1.5)
default_spirit = imageScaling(150, 375, default_spirit, 1.5)
default_shadow = imageScaling(150, 450, default_shadow, 1.5)
default_light = imageScaling(150, 525, default_light, 1.5)
#item scaling - clicked forms
hookshot = imageScaling(0, 75, hookshot, 1.5)
longshot = imageScaling(0, 75, longshot, 1.5)
boomerang = imageScaling(150, 75, boomerang, 1.5)

bow = imageScaling(0, 0, bow, 1.5)
fire_arrow = imageScaling(75, 0, fire_arrow, 1.5)
light_arrow = imageScaling(75, 0, light_arrow, 1.5)
fire_light_mix = imageScaling(75, 0, fire_light_mix, 1.5)

forest_small = imageScaling(0, 150, forest_small, 1.5)
forest_small_1 = imageScaling(0, 150, forest_small_1, 1.5)
forest_small_2 = imageScaling(0, 150, forest_small_2, 1.5)
forest_small_3 = imageScaling(0, 150, forest_small_3, 1.5)
forest_small_4 = imageScaling(0, 150, forest_small_4, 1.5)
forest_small_5 = imageScaling(0, 150, forest_small_5, 1.5)
forest_boss = imageScaling(75, 150, forest_boss, 1.5)
forest_boss_0 = imageScaling(75, 150, boss_key_default, 1.5)
forest = imageScaling(150, 150, clicked_forest, 1.5)

fire_small = imageScaling(0, 225, fire_small, 1.5)
fire_small_1 = imageScaling(0, 225, fire_small_1, 1.5)
fire_small_2 = imageScaling(0, 225, fire_small_2, 1.5)
fire_small_3 = imageScaling(0, 225, fire_small_3, 1.5)
fire_small_4 = imageScaling(0, 225, fire_small_4, 1.5)
fire_small_5 = imageScaling(0, 225, fire_small_5, 1.5)
fire_small_6 = imageScaling(0, 225, fire_small_6, 1.5)
fire_small_7 = imageScaling(0, 225, fire_small_7, 1.5)
fire_small_8 = imageScaling(0, 225, fire_small_8, 1.5)
fire_boss = imageScaling(75, 225, fire_boss, 1.5)
fire_boss_0 = imageScaling(75, 225, boss_key_default, 1.5)
fire = imageScaling(150, 225, clicked_fire, 1.5)

water_small = imageScaling(0, 300, water_small, 1.5)
water_small_1 = imageScaling(0, 300, water_small_1, 1.5)
water_small_2 = imageScaling(0, 300, water_small_2, 1.5)
water_small_3 = imageScaling(0, 300, water_small_3, 1.5)
water_small_4 = imageScaling(0, 300, water_small_4, 1.5)
water_small_5 = imageScaling(0, 300, water_small_5, 1.5)
water_small_6 = imageScaling(0, 300, water_small_6, 1.5)
water_boss = imageScaling(75, 300, water_boss, 1.5)
water_boss_0 = imageScaling(75, 300, boss_key_default, 1.5)
water = imageScaling(150, 300, clicked_water, 1.5)

spirit_small = imageScaling(0, 375, spirit_small, 1.5)
spirit_small_1 = imageScaling(0, 375, spirit_small_1, 1.5)
spirit_small_2 = imageScaling(0, 375, spirit_small_2, 1.5)
spirit_small_3 = imageScaling(0, 375, spirit_small_3, 1.5)
spirit_small_4 = imageScaling(0, 375, spirit_small_4, 1.5)
spirit_small_5 = imageScaling(0, 375, spirit_small_5, 1.5)
spirit_boss = imageScaling(75, 375, spirit_boss, 1.5)
spirit_boss_0 = imageScaling(75, 375, boss_key_default, 1.5)
spirit = imageScaling(150, 375, clicked_spirit, 1.5)

shadow_small = imageScaling(0, 450, shadow_small, 1.5)
shadow_small_1 = imageScaling(0, 450, shadow_small_1, 1.5)
shadow_small_2 = imageScaling(0, 450, shadow_small_2, 1.5)
shadow_small_3 = imageScaling(0, 450, shadow_small_3, 1.5)
shadow_small_4 = imageScaling(0, 450, shadow_small_4, 1.5)
shadow_small_5 = imageScaling(0, 450, shadow_small_5, 1.5)
shadow_boss = imageScaling(75, 450, shadow_boss, 1.5)
shadow_boss_0 = imageScaling(75, 450, boss_key_default, 1.5)
shadow = imageScaling(150, 450, clicked_shadow, 1.5)

ganon_small = imageScaling(0, 525, small_key, 1.5)
ganon_small_1 = imageScaling(0, 525, ganon_small_1, 1.5)
ganon_small_2 = imageScaling(0, 525, ganon_small_2, 1.5)
ganon_boss_0 = imageScaling(75, 525, boss_key_default, 1.5)
ganon_boss = imageScaling(75, 525, boss_key, 1.5)
light = imageScaling(150, 525, clicked_light, 1.5)

#vars
#general settings
vanilla_dungeon_keys = [0, 0, 0, 5, 8, 6, 5, 5, 3, 9, 0, 2]
obtained_keys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #index 11 for ganon
boss_keys = [0, 0, 0, 0, 0, 0, 0, 0, 0] #idices 0-2 are primarily just for consistency with other lists, index 8 is for ganon


#dungeon settings


bombchu_enabled = False
trials = 6
logic = "glitchless"
mq = False
triforce_hunt = False

dungeon_reward_type = "medallion" #type of reward required, options : medallions, stones, any
medallions_collected = 0
stones_collected = 0
rewards_collected = 0
dungeon_reward_amount = 6
dungeon_rewards = [0, 0, 0, 0, 0, 0, 0, 0, 0] #last entry for light medallion


#items and dungeon stuff
#variables - drawing items (item states for progressive items)
hookshotState = 0
bottleState = 0
bombState = 0
bombchuState = 0
slingshotState = 0
boomerangState = 0
stickState = 0
nutState = 0
mirrorState = 0
bowState = 0
arrowState = 0

tunicState = 0 #needs to allow both goron and zora tunic to be displayed
bootState = 0 
hammerState = 0

#dungeons and skulltula
skulltulaState = 0

#support for dungeon entrance rando




#ocarina and magic, none of these are fully coded, just there for later coding
ocarinaState = 0
zl = False
epona = False
sarias = False
suns = False
storms = False
SoT = False
minuet = False
bolero = False
serenade = False
requiem = False
nocturne = False
prelude = False
magic = False
dins = 0
strengthState =0
gerudo_card =0
lens = 0
letter = 0
scale = 0
#dungeon location stuff 
dungeon_locations = ["deku", "dc", "jabu", "forest", "fire", "water", "spirit", "shadow", "well", "gtg", "ice"]
deku_location = dungeon_locations[0]
dc_location = dungeon_locations[1]
jabu_location = dungeon_locations[2]
forest_location = dungeon_locations[3]
fire_location = dungeon_locations[4]
water_location = dungeon_locations[5]
spirit_location = dungeon_locations[6]
shadow_location =dungeon_locations[7]
botw_location = dungeon_locations[8]
gtg_location = dungeon_locations[9]
ice_location = dungeon_locations[10]


#rectangles in the form (x coor, y coor, length, width)
hookshot_rect = pygame.Rect(0, 75, 50, 50) #50, 50 is the absolute rect size for hook
bow_rect = pygame.Rect(0, 0, 50, 50) 
arrow_rect = pygame.Rect(75, 0, 50, 50)
boots_rect = pygame.Rect(75, 75, 50, 50)
magic_rect = pygame.Rect(150, 0, 50, 50)
boomerang_rect = pygame.Rect(150, 75, 50, 50)

forest_small_rect = pygame.Rect(0, 150, 50, 50)
forest_boss_rect = pygame.Rect(75, 150, 50, 50)
forest_rect = pygame.Rect(150, 150, 50, 50)

fire_small_rect = pygame.Rect(0, 225, 50, 50)
fire_boss_rect = pygame.Rect(75, 225, 50, 50)
fire_rect = pygame.Rect(150, 225, 50, 50)

water_small_rect = pygame.Rect(0, 300, 50, 50)
water_boss_rect = pygame.Rect(75, 300, 50, 50)
water_rect = pygame.Rect(150, 300, 50, 50)

spirit_small_rect = pygame.Rect(0, 375, 50, 50)
spirit_boss_rect = pygame.Rect(75, 375, 50, 50)
spirit_rect = pygame.Rect(150, 375, 50, 50)

shadow_small_rect = pygame.Rect(0, 450, 50, 50)
shadow_boss_rect = pygame.Rect(75, 450, 50, 50)
shadow_rect = pygame.Rect(150, 450, 50, 50)

ganon_small_rect = pygame.Rect(0, 525, 50, 50)
ganon_boss_rect = pygame.Rect(75, 525, 50, 50)
light_rect = pygame.Rect(150, 525, 50, 50)


def go_mode(): #checks if the game is done
   if accessible("ganon") == True and bowState == 1 and arrowState>=2 and magic==True and boss_keys[8]:
      return True
   else:
      return False

print("welcome to the OoT3D Randomizer Tracker made by Ven519.  Inputs can be made using mouse buttons (so left click ot right click)")

while run == True:
  while start == True:
    print("Go Mode Status: " + str(go_mode()))
    print("Has Adult Projectile: " + str(projectile_query("adult")))
    print("Dungeon Reward Type: " + str(dungeon_reward_type))
    print("Ammount Required: " + str(dungeon_reward_amount))
    print("ganon accessible: " + str(accessible("ganon")))
    print("medallions collected : " + str(medallions_collected))
    print("Spirit Temple Small Keys: " + str(obtained_keys[7]))
    print(arrowState)
    screen.fill((0, 0, 0))
    #OoT_bg.draw()
    #item_bg.draw()
    if hookshotState == 0:
          default_hookshot.draw()
    if hookshotState == 1:
          hookshot.draw()
    if hookshotState == 2:
          longshot.draw()
    if bowState == 0:
          default_bow.draw()
    if bowState == 1:
          bow.draw()
    if obtained_keys[3] == 0:
      forest_small.draw()
    if obtained_keys[3] == 1:
      forest_small_1.draw() 
    if obtained_keys[3] == 2:
       forest_small_2.draw() 
    if obtained_keys[3] == 3:
       forest_small_3.draw()    
    if obtained_keys[3] == 4:
       forest_small_4.draw() 
    if obtained_keys[3] == 5:
       forest_small_5.draw()    
    if obtained_keys[7] == 0:
       spirit_small.draw()
    if obtained_keys[7] == 1:
       spirit_small_1.draw()
    if obtained_keys[7] == 2:
       spirit_small_2.draw()
    if obtained_keys[7] == 3:
       spirit_small_3.draw()
    if obtained_keys[7] == 4:
       spirit_small_4.draw()
    if obtained_keys[7] == 5:
       spirit_small_5.draw()
    if obtained_keys[6] == 0:
       shadow_small.draw()
    if obtained_keys[6] == 1:
       shadow_small_1.draw()
    if obtained_keys[6] == 2:
       shadow_small_2.draw()
    if obtained_keys[6] == 3:
       shadow_small_3.draw()
    if obtained_keys[6] == 4:
       shadow_small_4.draw()
    if obtained_keys[6] == 5:
       shadow_small_5.draw()
    if obtained_keys[5] == 0:
       water_small.draw()
    if obtained_keys[5] == 1:
       water_small_1.draw()
    if obtained_keys[5] == 2:
       water_small_2.draw()
    if obtained_keys[5] == 3:
       water_small_3.draw()
    if obtained_keys[5] == 4:
       water_small_4.draw()
    if obtained_keys[5] == 5:
       water_small_5.draw()
    if obtained_keys[5] == 6:
       water_small_6.draw()
    if obtained_keys[4] == 0:
        fire_small.draw()   
    if obtained_keys[4] == 1:
       fire_small_1.draw()
    if obtained_keys[4] == 2:
       fire_small_2.draw()
    if obtained_keys[4] == 3:
       fire_small_3.draw()
    if obtained_keys[4] == 4:
       fire_small_4.draw()
    if obtained_keys[4] == 5:
       fire_small_5.draw()
    if obtained_keys[4] == 6:
       fire_small_6.draw()
    if obtained_keys[4] == 7:
       fire_small_7.draw()
    if obtained_keys[4] == 8:
       fire_small_8.draw()
    if obtained_keys[11] == 0:
       ganon_small.draw()
    if obtained_keys[11] == 1:
       ganon_small_1.draw()
    if obtained_keys[11] == 2:
       ganon_small_2.draw()   

    if boss_keys[3] == 0:
       forest_boss_0.draw()
    if boss_keys[3] == 1:
       forest_boss.draw()
    if boss_keys[4] == 0:
       fire_boss_0.draw()
    if boss_keys[4] == 1:
       fire_boss.draw()
    if boss_keys[5] == 0:
       water_boss_0.draw()
    if boss_keys[5] == 1:
       water_boss.draw()
    if boss_keys[6] == 0:
       shadow_boss_0.draw()
    if boss_keys[6] == 1:
       shadow_boss.draw()
    if boss_keys[7] == 0:
       spirit_boss_0.draw()
    if boss_keys[7] == 1:
       spirit_boss.draw()
    if boss_keys[8] == 0:
       ganon_boss_0.draw()
    if boss_keys[8] == 1:
       ganon_boss.draw()   

    if dungeon_rewards[3] == 0:
      default_forest.draw()
    if dungeon_rewards[3] == 1:
       forest.draw()
    if dungeon_rewards[4] == 0:
       default_fire.draw()
    if dungeon_rewards[4] == 1:
       fire.draw()
    if dungeon_rewards[5] == 0:
       default_water.draw()
    if dungeon_rewards[5] == 1:
       water.draw()
    if dungeon_rewards[6] == 0:
       default_shadow.draw()
    if dungeon_rewards[6] == 1:
       shadow.draw()
    if dungeon_rewards[7] == 0:
       default_spirit.draw()
    if dungeon_rewards[7] == 1:
       spirit.draw()
    if dungeon_rewards[8] == 0:
       default_light.draw()
    if dungeon_rewards[8] == 1:
       light.draw()      

    if arrowState == 0:
       default_arrow.draw()
    if arrowState == 1:
       fire_arrow.draw()
    if arrowState == 2:
       light_arrow.draw()
    if arrowState == 3:
       fire_light_mix.draw()      
    if bootState == 0:
       default_boots.draw()
    if bootState == 1:
       irons.draw()
    if bootState == 2:
       hovers.draw()
    if bootState == 3:
       iron_hovers_mix.draw()   
    if magic == 0:
       default_magic.draw() 
    if magic == 1:
       magic_1.draw()
    if magic == 2:
       magic_2.draw()         

    if boomerangState == 0:
       default_boomerang.draw()
    if boomerangState == 1:
       boomerang.draw()   
    if go_mode():
       go_mode_image.draw()                          
    start = False
    pygame.display.update()
  for event in pygame.event.get():
      #pygame.quit() will run and close window
        #print(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
              x, y = event.pos
              if spirit_small_rect.collidepoint(x, y) and obtained_keys[7] > 0:
                 obtained_keys[7] -=1
              if forest_small_rect.collidepoint(x, y) and obtained_keys[3] > 0:
                 obtained_keys[3] -=1
              if shadow_small_rect.collidepoint(x, y) and obtained_keys[6] > 0:
                 obtained_keys[6] -=1
              if water_small_rect.collidepoint(x, y) and obtained_keys[5] >0:
                 obtained_keys[5] -=1
              if fire_small_rect.collidepoint(x, y) and obtained_keys[4] >0:
                 obtained_keys[4] -=1
              if ganon_small_rect.collidepoint(x, y) and obtained_keys[11] >0:
                 obtained_keys[11] -=1   

              if spirit_boss_rect.collidepoint(x, y) and boss_keys[7] > 0:
                 boss_keys[7] -=1
              if forest_boss_rect.collidepoint(x, y) and boss_keys[3] > 0:
                 boss_keys[3] -=1
              if shadow_boss_rect.collidepoint(x, y) and boss_keys[6] > 0:
                 boss_keys[6] -=1
              if water_boss_rect.collidepoint(x, y) and boss_keys[5] >0:
                 boss_keys[5] -=1
              if fire_boss_rect.collidepoint(x, y) and boss_keys[4] >0:
                 boss_keys[4] -=1  
              if ganon_boss_rect.collidepoint(x, y) and boss_keys[8] >0:
                 boss_keys[8]-=1    

              if forest_rect.collidepoint(x, y) and dungeon_rewards[3] == 1:
                 dungeon_rewards[3]-=1
                 medallions_collected -=1
              if fire_rect.collidepoint(x, y) and dungeon_rewards[4] == 1:
                 dungeon_rewards[4]-=1
                 medallions_collected -=1 
              if water_rect.collidepoint(x, y) and dungeon_rewards[5] == 1:
                 dungeon_rewards[5]-=1
                 medallions_collected -=1   
              if shadow_rect.collidepoint(x, y) and dungeon_rewards[6] == 1:
                 dungeon_rewards[6]-=1
                 medallions_collected -=1
              if spirit_rect.collidepoint(x, y) and dungeon_rewards[7] == 1:
                 dungeon_rewards[7]-=1
                 medallions_collected -=1  
              if light_rect.collidepoint(x, y) and dungeon_rewards[8] == 1:
                 dungeon_rewards[8]-=1
                 medallions_collected-=1   
              if arrow_rect.collidepoint(x, y):
                 if arrowState >=2:
                     start = True  
                     arrowState-=2
                 else:
                    arrowState +=2
                    start = True

              if boots_rect.collidepoint(x, y):
                 if bootState >=2:
                     start = True  
                     bootState-=2
                 else:
                    bootState +=2
                    start = True   
              
              if magic_rect.collidepoint(x, y) and magic >=1:   
                   magic-=1

              if hookshot_rect.collidepoint(x, y) and hookshotState == 1:
                    hookshotState = 0
              elif hookshot_rect.collidepoint(x, y) and hookshotState == 2:
                    hookshotState = 1
              if boomerang_rect.collidepoint(x, y) and boomerangState == 1:
                    boomerangState -=1          
              if bow_rect.collidepoint(x, y) and bowState == 1:
                    bowState = 0 
              start = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #left click event
              x, y = event.pos
              if spirit_small_rect.collidepoint(x, y) and obtained_keys[7] < vanilla_dungeon_keys[7]:
                 obtained_keys[7] +=1
              if forest_small_rect.collidepoint(x, y) and obtained_keys[3] < vanilla_dungeon_keys[3]:
                 obtained_keys[3] +=1
              if shadow_small_rect.collidepoint(x, y) and obtained_keys[6] < vanilla_dungeon_keys[6]:
                 obtained_keys[6] +=1
              if water_small_rect.collidepoint(x, y) and obtained_keys[5] < vanilla_dungeon_keys[5]:
                 obtained_keys[5] +=1
              if fire_small_rect.collidepoint(x, y) and obtained_keys[4] < vanilla_dungeon_keys[4]:
                 obtained_keys[4] +=1
              if ganon_small_rect.collidepoint(x, y) and obtained_keys[11] < vanilla_dungeon_keys[11]:
                 obtained_keys[11] +=1   

              if spirit_boss_rect.collidepoint(x, y) and boss_keys[7] < 1:
                 boss_keys[7] +=1
              if forest_boss_rect.collidepoint(x, y) and boss_keys[3] < 1:
                 boss_keys[3] +=1
              if shadow_boss_rect.collidepoint(x, y) and boss_keys[6] < 1:
                 boss_keys[6] +=1
              if water_boss_rect.collidepoint(x, y) and boss_keys[5] < 1:
                 boss_keys[5] +=1
              if fire_boss_rect.collidepoint(x, y) and boss_keys[4] < 1:
                 boss_keys[4] +=1
              if ganon_boss_rect.collidepoint(x, y) and boss_keys[8] < 1:
                 boss_keys[8] +=1   

              if forest_rect.collidepoint(x, y) and dungeon_rewards[3] == 0:
                 dungeon_rewards[3]+=1 
                 medallions_collected +=1
              if fire_rect.collidepoint(x, y) and dungeon_rewards[4] == 0:
                 dungeon_rewards[4]+=1
                 medallions_collected +=1 
              if water_rect.collidepoint(x, y) and dungeon_rewards[5] == 0:
                 dungeon_rewards[5]+=1
                 medallions_collected +=1   
              if shadow_rect.collidepoint(x, y) and dungeon_rewards[6] == 0:
                 dungeon_rewards[6]+=1
                 medallions_collected +=1
              if spirit_rect.collidepoint(x, y) and dungeon_rewards[7] == 0:
                 dungeon_rewards[7]+=1
                 medallions_collected +=1  
              if light_rect.collidepoint(x, y) and dungeon_rewards[8] == 0:
                 dungeon_rewards[8] +=1
                 medallions_collected+=1       

              if magic_rect.collidepoint(x, y) and magic <=2:   
                   magic+=1   

              if hookshot_rect.collidepoint(x, y) and hookshotState == 0:
                    hookshotState = 1
                    start = True
                    break #this was added because otherwise drawing hookshot would be skipped for drawing longshot
              if hookshot_rect.collidepoint(x, y) and hookshotState == 1:
                    hookshotState = 2
              if boomerang_rect.collidepoint(x, y) and boomerangState == 0:
                    boomerangState +=1            
              if bow_rect.collidepoint(x, y) and bowState == 0:
                    bowState = 1  
              if arrow_rect.collidepoint(x, y):
                 if arrowState == 1 or arrowState == 3:
                     start = True  
                     arrowState-=1
                 else:
                    arrowState +=1
                    start = True

              if boots_rect.collidepoint(x, y):
                 if bootState%2 == 1:
                     start = True  
                     bootState-=1
                 else:
                    bootState +=1
                    start = True       

              start = True
        if event.type == pygame.QUIT:
          run = False
