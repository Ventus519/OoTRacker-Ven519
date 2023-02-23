import pygame


#screen
screenHeight = 1000
screenWidth = 1000

pygame.init()

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Ocarina of Time Randomizer Tracker - Ven519")

#lists for map tracker
abs_required_items=["bow_1", "light_arrows", "magic_1", "master_sword"]
song_locations=["zl", "eponas", "sarias", "suns", "time", "storms", "minuet", "preulde", "bolero", "serenade", "requiem", "nocturne"]
dungeon_rewards = ["deku", "dc", "jabu", "forest", "fire", "water", "spirit", "shadow", "free"]

vanilla_dungeon_keys = [0, 0, 0, 5, 8, 6, 9, "???", 3, 9, 0]
master_quest_keys = [0, 0, 0, 6, 5, 6, 9, "???", 3, 9, 0]

#dungeon settings
dungeon_entrance_rando = False
dungeon_reward_type = "medallions" #type of reward required, options : medallions, stones, any
medallions_collected = 0
stones_collected = 0
rewards_collected = 0
dungeon_reward_amount = 6
bombchu_enabled = False
trials = 6
logic = "glitchless"
mq = False
triforce_hunt = False
dungeon_settings = [mq, dungeon_reward_type, dungeon_reward_amount, dungeon_entrance_rando, dungeon_boss_rando, trials, logic]

#deku reqs

#overworld settings


#image loading
  #background (not yet)
OoT_bg = pygame.image.load("assets/images/OoT/bg/OoT_bg.png").convert_alpha()
item_bg = pygame.image.load("assets/images/OoT/bg/items.png").convert_alpha()
  #default item loading
default_hookshot = pygame.image.load("assets/images/OoT/items/hookshot/hookshot_0.png").convert_alpha()
default_bow = pygame.image.load("assets/images/OoT/items/bow/no.png").convert_alpha()
  
  #obtained item loading
hookshot = pygame.image.load("assets/images/OoT/items/hookshot/hookshot.png").convert_alpha()
longshot = pygame.image.load("assets/images/OoT/items/hookshot/longshot.png").convert_alpha()

  #dungeon reward loading - medallions
default_light = pygame.image.load("assets/images/OoT/medallions/light_gray.png").convert_alpha()
clicked_light = pygame.image.load("assets/images/Oot/medallions/light.png").convert_alpha()

default_forest = pygame.image.load("assets/images/OoT/medallions/forest_gray.png").convert_alpha()
clicked_forest = pygame.image.load("assets/images/OoT/medallions/forest.png").convert_alpha()

default_fire = pygame.image.load("assets/images/OoT/medallions/fire_gray.png").convert_alpha()
clicked_fire = pygame.image.load("assets/images/OoT/medallions/fire.png").convert_alpha()

default_water = pygame.image.load("assets/images/OoT/medallions/water_gray.png").convert_alpha()
clicked_water = pygame.image.load("assets/images/OoT/medallions/water.png").convert_alpha()

default_spirit = pygame.image.load("assets/images/OoT/medallions/spirit_gray.png").convert_alpha()
clicked_spirit = pygame.image.load("assets/images/OoT/medallions/spirit.png").convert_alpha()

default_shadow = pygame.image.load("assets/images/OoT/medallions/shadow_gray.png").convert_alpha()
clicked_shadow = pygame.image.load("assets/images/OoT/medallions/shadow.png").convert_alpha()


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
OoT_bg = imageScaling(0, 0, OoT_bg, 4)
item_bg = imageScaling(0, 0, item_bg, 0.75)

#item scaling - default items
default_hookshot = imageScaling(100, 100, default_hookshot, 0.2)
default_bow = imageScaling(240, 0, default_bow, 0.2)
#item scaling - clicked forms
hookshot = imageScaling(100, 100, hookshot, 0.2)
longshot = imageScaling(100, 100, longshot, 0.2)


#variables - drawing items (item states for progressive items)
hookshotState = 0
bottleState = 0
bombState = 0
bombchuState = 0
slingshotState = 0
boomerangState = 0
stickState = 0
nutState = 0
shieldState = 0 #needs to allow both left and right click events to change image
bowState = 0
arrowState = 0
tunicState = 0 #needs to allow both goron and zora tunic to be displayed
bootState = 0 #needs to allow both iron and hover -> 2 = hovers only, 1 = irons only, 3 = both

#dungeons and skulltula
forest_keyState = 0
fire_keyState = 0
water_keyState = 0
spirit_keyState = 0
shadow_keyState = 0
gtg_keyState = 0
botw_keyState = 0
skulltulaState = 0

#support for dungeon entrance rando
forest_entranceState = 0
fire_entranceState = 0
water_entranceState = 0
spirit_entranceState = 0
shadow_entranceState = 0
gtg_entranceState = 0
botw_entranceState = 0
ice_entranceState = 0

#dungeon reward states
deku_rewardState = 0
dc_rewardState = 0
jabu_rewardState = 0
forest_rewardState = 0
fire_rewardState = 0
water_rewardState = 0
spirit_rewardState = 0
shadow_rewardState = 0
light_rewardState = 0


#ocarina and magic
ocarinaState = 0
zl = False
epona = False
requiem = False
nocturne = False
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
    
def projectile_query(age):
    if age == "adult":
      if hookshotState >=1 or bowState == 1:
        return True
    elif age == "child":
      if boomerangState == 1 or slingshotState == 1:
        return True
    else:
      return False
def explosive_query():
    if bombState == 1:
        return True
    if bombchu_enabled == True and bombchuState == 1:
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

def beatable_vanilla_glitchless(dungeon):
    if dungeon=="deku":
      if accessible("deku"): #not done yet
        return True
    if dungeon == "dc":
      if accessible("dc") and explosive_query(): #not done
        return True
    if dungeon == "jabu": 
      if accessible("jabu") and boomerangState == 1:
        return True
      else:
        return False
    if dungeon == "shadow":
        if accessible("shadow"):
            if zl==True and projectile_query("adult") == True and bootState >= 2 and explosive_query() == True:
                return True
            else: 
                return False
        else:
            return False
def go_mode():
   if accessible("ganon") and bowState == 1 and arrowState>=2 and magic==True:
      return True
   else:
      return False
#rectangles, the bane of my existence
hookshot_rect = pygame.Rect(100, 100, 50, 50) #50, 50 is the absolute rect size for hook
while run == True:
  while start == True:
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
    print("Has Adult Projectile: " + str(projectile_query("adult")))
    print("Dungeon Reward Type: " + str(dungeon_reward_type))
    print("Ammount Required: " + str(dungeon_reward_amount))
    print("Go Mode Status: " + str(go_mode()))
    start = False
    pygame.display.update()
  for event in pygame.event.get():
      #pygame.quit() will run and close window
        #print(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
              x, y = event.pos
              if hookshot_rect.collidepoint(x, y) and hookshotState == 1:
                    hookshotState = 0
              elif hookshot_rect.collidepoint(x, y) and hookshotState == 2:
                    hookshotState = 1
              start = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #left click event
          x, y = event.pos
          if hookshot_rect.collidepoint(x, y) and hookshotState == 0:
                hookshotState = 1
                print("hookshot")
                start = True
                break
          if hookshot_rect.collidepoint(x, y) and hookshotState == 1:
                hookshotState = 2
                print("longshot")
                start = True
        if event.type == pygame.QUIT:
          run = False