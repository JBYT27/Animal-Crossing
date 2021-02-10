import os, time, sys, random, pickle
#from replit import db
from map import *

def clear():
  os.system('clear')

st = 0.04
def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(st)
  print()

#editing stuff
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"
grey = '\033[38;4;236m'
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible='\033[08m'
reverse='\033[07m'
reset='\033[0m'
grey = "\x1b[90m"

def any_key():
      print(Orange+'\n\n<NEXT>\t[Press any KEY to continue]')
      input(White)

def any_key2():
  print(Orange+'\n<NEXT>\t[Press any KEY to continue]')
  input(White)

def printmap(themap):
  for i in themap:
    if i == 'x':
      print(f'{Blue}{blue_back} {reset}',end="")
    elif i == '^':
      print(f'{Green}{green_back} {reset}',end="")
    elif i == 'H':
      print(f'{grey}{grey_back} {reset}',end="")
    elif i == '*':
      print(f'{Orange}{orange_back} {reset}',end="")
    else:
      print(i,end="")

clear()
username=os.environ['REPL_OWNER']

thingy2=True
login_signup = True
while login_signup:
  print('System Menu:')
  print('[1] Login\n[2] Sign up\n[3] Guest')
  ls_menu=input('> ')
  clear()

  if ls_menu == '1':
    guest=False
    print('Login Menu:')
    username = input('Username\n> ')
    try:
      inputFile = 'username.env'
      fd = open(inputFile, 'rb')
      dataset = pickle.load(fd)
      clear()

      if username == dataset:
        print(f'{Green}Logged in!{White}')
        time.sleep(2)
        any_key()
        clear()
      else:
        print(f'{Red}Invalid Username!{White}')
        time.sleep(2)
        any_key()
        clear()

    except:
      print(f'{Red}Ran out of input!{White}')
      time.sleep(2)
      any_key()
      clear()

  elif ls_menu == '2':
    guest=False
    print(f"Welcome to{Green} Animal Crossing{Orange} REPLIT v.1 {Blue}{username}!{White} Would you like your current {Orange}REPL{White} username or would you like your own? {pink_back}r/o{reset}{White}")
    name_ro=input('> ').lower()
    clear()

    if name_ro == 'o':
      print('What will your name be then?\nNote: Dont add spaces, add underscores.')
      username=input('> ')
      print(f'Are you sure you\'re ok with {Blue}{username}{White}? y/n')
      yn_user = input('> ').lower()

      if yn_user == 'y':
        thingy2=False
        print(f'{Blue}{username}{White}! What a nice name that fits just right!')
        dataset = username
        outputFile = 'username.env'
        fw = open(outputFile, 'wb')
        pickle.dump(dataset, fw)
        fw.close()
        time.sleep(2)
        any_key()
        clear()

      elif yn_user == 'n':
        print(Green+'Ok then, lets try again!'+White)
        time.sleep(2)
        any_key()
        clear()

      else:
        clear()
        print(f'{Red}Invalid Choice, try again!{White}')
        time.sleep(2)
        any_key()
        clear()

    elif name_ro == 'r':
      thingy2=False
      print(f'{Blue}{username}{White} it is! What a wonderful name! Welcome to {Green}Animal Crossing {Orange}REPLIT v.1!{White} It seems like you just got a {Green}Nook{White} Ticket to an Island!')
      dataset = username
      outputFile = 'username.env'
      fw = open(outputFile, 'wb')
      pickle.dump(dataset, fw)
      fw.close()
      time.sleep(2)
      any_key()
      clear()
      login_signup=False
    
    else:
      clear()
      print(Red+'Invalid Choice, try again!'+White)
      time.sleep(2)
      any_key()
      clear()

  elif ls_menu == '3':
    print('You will continue as GUEST. No progress will be saved. Are you sure you want to continue? y/n')
    yn_guest = input('> ').lower()
    clear()

    if yn_guest == 'y':
      thingy2=False
      username='GUEST'
      print(Green+'Okie Dokie GUEST! Welcome Aboard! You just earned a Nook Ticket to an Island!'+White)
      time.sleep(2)
      any_key()
      clear()
      guest=True
      login_signup=False

    elif yn_guest == 'n':
      print(Green+'Ok then, lets try again!'+White)
      time.sleep(2)
      any_key()
      clear()

    else:
      print(Red+'Invalid Choice, try again!'+White)
      time.sleep(2)
      any_key()
      clear()
  
  else:
    print(Red+'Invalid Choice, try again!'+White)
    time.sleep(2)
    any_key()
    clear()

#menu=True
#use menu later

#introduction with the NOOK
if thingy2 == False:#introduction
  sp(f'{italic}At {Green}Nook{White} Inc.{reset}')
  time.sleep(2)
  any_key()
  clear()

  sp(f'{italic}Timmy:{reset}{White} Hello {Blue}{username}{White}! Welcome to Nook Inc! It seems like you got a {Green}Nook Ticket!{White} And let me see here...')
  time.sleep(2)
  any_key2()
  sp(f"\n{italic}Tommy:{reset}{White} It says here that it says you have got an invitation to get an {Green}island!{White} So in the meantime, what will your new {Green}Island {White}look like? On another note, we will brainstorm some ideas for you!")
  time.sleep(2)
  any_key2()
  clear()

  islands=[map1,map2,map3,map4,map5,map6,map7,map8,map9,map10]
  island_choose=random.choice(islands)
  island_choose2=random.choice(islands)
  island_choose3=random.choice(islands)
  island_choose4=random.choice(islands)
  island_shape = True
  thingy=True
  while island_shape:
    if thingy == True:
      print('Islands:')
      print('[1].')
      a = printmap(island_choose)
      print(f'\n{reset}[2].')
      b = printmap(island_choose2)
      print(f'\n{reset}[3].')
      c = printmap(island_choose3)
      print(f'\n{reset}[4].')
      d = printmap(island_choose4)
    else:
      thingy=False
      print('Islands:')
      print('[1].')
      print(a)
      print('\n[2].')
      print(b)
      print('\n[3].')
      print(c)
      print('\n[4].')
      print(d)
    island_shape_choose=input(f'{reset}\n\nWhich island layout will you choose? 1/2/3/4\n> ')

    if island_shape_choose == '1':
      print('\n\nAre you sure you want this layout? y/n')
      yn = input('> ').lower()
      if yn == 'y':
        print(Green+'You chose that layout!'+White)
        time.sleep(2)
        any_key()
        clear()
        A=True
        island_shape=False
        if guest == True:
          pass
        else:
          dataset = a
          outputFile = 'map.env'
          fw = open(outputFile, 'wb')
          pickle.dump(dataset, fw)
          fw.close()
      elif yn == 'n':
        print(Red+'Lets choose a different one then!'+White)
        time.sleep(2)
        any_key()
        clear()
      else:
        print(Red+'Invalid Choice!'+White)
        time.sleep(2)
        any_key()
        clear()

    elif island_shape_choose == '2':
      print('\n\nAre you sure you want this layout? y/n')
      yn = input('> ').lower()
      if yn == 'y':
        print(Green+'You chose that layout!'+White)
        time.sleep(2)
        any_key()
        clear()
        B=True
        island_shape=False
        if guest == True:
          pass
        else:
          dataset = b
          outputFile = 'map.env'
          fw = open(outputFile, 'wb')
          pickle.dump(dataset, fw)
          fw.close()
      elif yn == 'n':
        print(Red+'Lets choose a different one then!'+White)
        time.sleep(2)
        any_key()
        clear()
      else:
        print(Red+'Invalid Choice!'+White)
        time.sleep(2)
        any_key()
        clear()
    
    elif island_shape_choose == '3':
      print('\n\nAre you sure you want this layout? y/n')
      yn = input('> ').lower()
      if yn == 'y':
        print(Green+'You chose that layout!'+White)
        time.sleep(2)
        any_key()
        clear()
        island_shape=False
        C=True
        if guest == True:
          pass
        else:
          dataset = c
          outputFile = 'map.env'
          fw = open(outputFile, 'wb')
          pickle.dump(dataset, fw)
          fw.close()
      elif yn == 'n':
        print(Red+'Lets choose a different one then!'+White)
        time.sleep(2)
        any_key()
        clear()
      else:
        print(Red+'Invalid Choice!'+White)
        time.sleep(2)
        any_key()
        clear()
    
    elif island_shape_choose == '4':
      print('\n\nAre you sure you want this layout? y/n')
      yn = input('> ').lower()
      if yn == 'y':
        print(Green+'You chose that layout!'+White)
        time.sleep(2)
        any_key()
        clear()
        D=True
        island_shape=False
        if guest == True:
          pass
        else:
          dataset = d
          outputFile = 'map.env'
          fw = open(outputFile, 'wb')
          pickle.dump(dataset, fw)
          fw.close()
      elif yn == 'n':
        print(Red+'Lets choose a different one then!'+White)
        time.sleep(2)
        any_key()
        clear()
      else:
        print(Red+'Invalid Choice!'+White)
        time.sleep(2)
        any_key()
        clear()
    else:
      print(Red+'Invalid Choice, try again!'+White)
      time.sleep(2)
      any_key()
      clear()
      
  sp(f'{italic}Timmy:{reset} What a nice {Green}island{White}! Very nice choice of you! Now that you\'ve chosen your {Green}island{White}, lets go there now!')
  time.sleep(2)
  any_key2()
  sp(f'{italic}Tommy:{reset} There are sure to be some surprising visitors...')
  time.sleep(2)
  any_key2()
  clear()
  sp(f'{Green}You are now going to the island...{White}')
  time.sleep(1)
  any_key2()
  clear()
  for i in range(2):
    printmap(gti1)
    time.sleep(1)
    clear()
    printmap(gti2)
    time.sleep(1)
    clear()
    printmap(gti3)
    time.sleep(1)
    clear()
    printmap(gti4)
    time.sleep(1)
    clear()
    printmap(gti5)
    time.sleep(1)
    clear()
    printmap(gti6)
    time.sleep(1)
    clear()
    printmap(gti7)
    time.sleep(1)
    clear()
    printmap(gti8)
    time.sleep(1)
    clear()
    printmap(gti9)
    time.sleep(1)
    clear()

  sp(f'{Green}You are now on the island!{White}')
  time.sleep(2)
  any_key()
  clear()

  sp(f'{italic}Tommy:{reset} We\'re here! Finally, meet your {Green}new island{White}!')
  time.sleep(2)
  any_key2()
  sp(f"{italic}Timmy:{reset} Our visitors are already here! It seems like they have set up the {Green}base{White}... We will meet up there! Feel free to roam around for now, but remember-")
  time.sleep(1)
  any_key2()
  sp(f"{italic}Tommy:{reset} -Come to the {Green}'base'{White} when you want to get started!")
  time.sleep(2)
  any_key2()
  clear()

  idk=True
  while idk:
    print(f'{Green}Mission granted: Go to base!{White}')
    time.sleep(2)
    any_key2()
    rb = input('\nWill you roam around for now or will you go to the base? b/r\n> ').lower()
    clear()

    if rb == 'r':
      print(f'{Green}You decided to roam around!{White}')
      time.sleep(2)
      any_key()
      idk=False
      roaming=True
    elif rb == 'b':
      print(f'{Green}You decided to go to the base!{White}')
      time.sleep(2)
      any_key()
      idk=False
      base=True
      roaming=False
    else:
      print(f'{Red}Invalid Choice, try again!{White}')
      time.sleep(2)
      any_key()
      clear()
  
  clear()
  if roaming==True:
    while roaming:
      poi = input('What part of the island do you want to go? \n[C]oast(where you are)\n[F]orest\n[B]ase\n[R]iver\n> ').lower()
      clear()

      if poi == 'b':
        print(f'{Green}You went back to the base!{White}')
        time.sleep(2)
        any_key()
        clear()
        base=True
        roaming=False
      elif poi == 'f':
        print(f'{Green}You went inside the Forest... Until{White}')
        time.sleep(2)
        any_key()
        sp(f'{italic}Timmy:{reset} {Blue}{username}{White}, don\'t go in there yet! It\'s quite dangerous for now, so let\'s skip that for now!')
        time.sleep(2)
        any_key2()
        clear()
      elif poi == 'c':
        print(f'{Red}You\'re already here right now!{White}')
        time.sleep(2)
        any_key()
        clear()
      elif poi == 'r':
        print(f'{Green}You visited the nearest river and looked in...{White}')
        time.sleep(1)
        sp('You see your own reflection...')
        time.sleep(1)
        any_key2()
        sp('You go back to the coast...')
        time.sleep(2)
        clear()
      else:
        print(f'{Red}Invalid Choice!{White}')
        time.sleep(2)
        any_key()
        clear()
  else:
    if base == True:
      idk2=True
      print(f'{Green}You are now at the base... And see three more people! You have a surprised expression, and Timmy and Tommy notice.{White}')
      time.sleep(2)
      any_key()
      sp(f'\n{italic}Tommy:{reset} Ah {Blue}{username}{White}! I see you\'ve seen our visitors!')
      time.sleep(2)
      any_key2()
      yn = input('\n[Y]es! or [N]o...\n> ').lower()
      #tom_nook_meet=True

      if yn == 'y':
        sp(f'\n{italic}Timmy:{reset} Yep! This is our boss, {Green}Tom Nook!{White}')
        time.sleep(2)
        any_key2()
      elif yn == 'n':
        sp(f'\n{italic}Timmy:{reset} Aww, come one {Blue}{username}{White}! Don\'t lie to us! Anyways, meet {Green}Tom Nook!{White}')
        time.sleep(2)
        any_key2()
      else:
        sp(f'\n{italic}Tommy:{reset} Awww, don\'t say naughty words {Blue}{username}{White}! Anyways, meet {Green}Tom Nook!{White}')
        time.sleep(2)
        any_key2()
    else:
      pass
  if idk2 == True:
    pass
  else:
    if base == True:
      print(f'{Green}You are now at the base... And see three more people! You have a surprised expression, and Timmy and Tommy notice.{White}')
      time.sleep(2)
      any_key()
      sp(f'\n{italic}Tommy:{reset} Ah {Blue}{username}{White}! I see you\'ver seen our visitors!')
      time.sleep(2)
      any_key2()
      yn = input('\n[Y]es! or [N]o...\n> ').lower()
      #tom_nook_meet=True

      if yn == 'y':
        sp(f'\n{italic}Timmy:{reset} Yep! This is our boss, {Green}Tom Nook!{White}')
        time.sleep(2)
        any_key2()
      elif yn == 'n':
        sp(f'\n{italic}Timmy:{reset} Aww, come one {Blue}{username}{White}! Don\'t lie to us! Anyways, meet {Green}Tom Nook!{White}')
        time.sleep(2)
        any_key2()
      else:
        sp(f'\n{italic}Tommy:{reset} Awww, don\'t say naughty words {Blue}{username}{White}! Anyways, meet {Green}Tom Nook!{White}')
        time.sleep(2)
        any_key2()
    else:
      pass

  sp(f'{italic}Tom Nook:{reset} Hello young sir/ma\'am! What is your name?')
  time.sleep(1)
  any_key2()
  name = input('\n> ')

  if name == username:
    sp(f'\n{italic}Tom Nook:{reset} So {Blue}{username}{White}, welcome! Let us start with the basics of your new home! What will be your {Green}new island{White} name? Also-')
    time.sleep(2)
    any_key2()
  else:
    sp(f'\n{italic}Timmy:{reset} Dont lie {Blue}{username}{White}! Anyways-')
    time.sleep(1)
    any_key2()
    sp(f'\n{italic}Tom Nook:{reset} You young rascal! Hahahaha! Lets start with the basics {Blue}{username}{White}! What will be you new island name?')
    time.sleep(2)
    any_key2()

  island_name_choose=True
  island_names=['Nook','Paradise','LOST','Super Blues','Bermuda Triangle','Konoha','Dark','God','The Omnious','Upside Down','Nook Kingdom']
  island_name1 = random.choice(island_names)
  island_name2 = random.choice(island_names)
  island_name3 = random.choice(island_names)
  island_name4 = random.choice(island_names)
  island_name5 = random.choice(island_names)
  thingy54=True
  while thingy54:
    if island_name1 == island_name2:
      island_name2=random.choice(island_names)
    elif island_name1 == island_name3:
      island_name3=random.choice(island_names)
    elif island_name1 == island_name4:
      island_name4=random.choice(island_names)
    elif island_name1 == island_name5:
      island_name5=random.choice(island_names)
    elif island_name2 == island_name3:
      island_name3=random.choice(island_names)
    elif island_name2 == island_name4:
      island_name4=random.choice(island_names)
    elif island_name2 == island_name5:
      island_name5=random.choice(island_names)
    elif island_name3 == island_name4:
      island_name4=random.choice(island_names)
    elif island_name3 == island_name5:
      island_name5=random.choice(island_names)
    elif island_name4 == island_name5:
      island_name5=random.choice
    #this whole blob of if and elif statements check that the names arent the same, a waste of code, right? xd
    else:
      thingy54=False

  while island_name_choose:
    your_name_island = input("What is your island name? \nNote: Dont include the 'island'.\n> ")
    clear()

    sp(f'Is it {Purple}{your_name_island} island{White}? Remember, you cant switch it once you\'ve chosen. y/n')
    yn = input('> ').lower()
    clear()

    if yn == 'y':
      print(f'You personally voted on {Purple}{your_name_island}{White}!')
      time.sleep(2)
      any_key()
      clear()
      island_name_choose=False
    elif yn == 'n':
      print(f'{Green}Ok then, lets choose again!{White}')
      time.sleep(2)
      any_key()
      clear()
    else:
      print(f'{Red}Invalid Choice, try again!{White}')
      time.sleep(2)
      any_key()
      clear()

  villager_names=['Truffles','Spork','Peggy','Hugh','Agnes','Rasher','Maggie','Lucy','Kevin','Gala','Curly','Cobb','Chops','Boris','Del','Sly','Gayle','Drago','Boots','Alli','Alfonso','Apollo','Avery','Amelia','Pierce','Frank','Buzz','Sterling','Keaton','Peewee','Violet','Hans','Boyd','Rocket','Boone','Rilla','Louise','Al','Cesar','Bea','Walker','Shep','Portia','Marcel','Maddie','Mac','Bones','Bones','Cookie','Lucky','Cherry','Daisy','Butch','Biskit','Benjamin','Goldie','Marcie','Walt','Rooney','Kitt','Matilda','Carrie','Sylvia','Astrid','Roald','Tex','Sprinkle','Puck','Iggly','Gwen','Friga','Aurora','Cube','Flo','Hopper','Wade','Boomer','Admiral','Jacob','Piper','Robin','Sparo','Midge','Peck','Lucha','Jitters','Twiggy','Jay','Anchovy','Jacques','Anabelle','Snooty','Pango','Antonio','Olaf','Annalisa','Cyrano','Anicotti','Chadder','Rod','Limberg','Rizzo','Candi','Dora','Brocollo','Penelope','Bella','Bettina','Bree','Mouse','Samson','Greta','Soleil','Rodney','Flurry','Apple','Hamphrey','Hamlet','Graham','Clay']#idk if these are from the correct season
  villager1=random.choice(villager_names)
  villager2=random.choice(villager_names)
  name_pick=True
  while name_pick:
    if villager1==villager2:
      villager2=random.choice(villager_names)
    else:
      name_pick=False
  sp(f'{italic}Timmy:{reset} So, now that we are done, lets vote!')
  time.sleep(2)
  any_key2()
  sp(f'\n{italic}Tom Nook:{reset} Yes, let us vote!')
  time.sleep(1)
  any_key2()
  sp(f'{italic}Tom Nook:{reset} Also, we have two villagers to stay with us, {Blue}{villager1}{White} and {Blue}{villager2}{White}! They will be your starting {Green}neighbors{White}, and remember, later on as you get more advanced, you will get more villagers!')
  time.sleep(2)
  any_key2()
  if guest == True:#checks if youre a guest, because if you are, not progress saves.
    pass#does nothing
  else:
    dataset = f'Number of villagers: 2\nIsland Name: {your_name_island}\nVillager Names: {villager1} and {villager2}'#later on, add more to this
    outputFile = 'stats.env'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()
  
  sp(f'{italic}Tommy:{reset} Lets get started with the poll everyone!')
  time.sleep(2)
  any_key2()
  print(f'\n{italic}Timmy:{reset} {Green}{island_name1} island{White}\n{italic}Tommy:{reset} {Green}{island_name2} island{White}\n{italic}Tom Nook:{reset} {Green}{island_name3} island{White}\n{italic}{villager1}:{reset} {Green}{island_name4} island{White}\n{italic}{villager2}:{reset} {Green}{island_name5} island{White}\n{Blue}{username}:{White} {Green}{your_name_island} island{White}')
  time.sleep(2)
  any_key()
  sp(f'\n\n{italic}Timmy:{reset} Hmmmm... I like {Blue}{username}{White}\'s island name very much... I would like to vote on {Blue}{username}{White}\'s!')
  time.sleep(1)
  any_key2()
  sp(f'{italic}Tom Nook:{reset} Yes, I agree with {Blue}Timmy{White} as well!')
  time.sleep(1)
  any_key2()
  sp(f'{italic}{villager1} and {villager2}:{reset} Same as us too!')
  time.sleep(1)
  any_key2()
  sp(f'{italic}Tommy:{reset} Well, that leaves me! And I agree with everyone else!')
  time.sleep(1)
  any_key2()
  clear()
  print(f'{Green}Island name is {your_name_island} island! Hooray! {White}')
  time.sleep(2)
  any_key()
  clear()
  if guest == True:
    pass
  else:
    dataset = 'Island name decided'
    outputFile = 'thingy.env'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()

  sp(f'{italic}Tom Nook:{reset} Now that we have decided on the island name, lets find set up our home. As of right now though, because we do not have houses...')
  time.sleep(2)
  any_key2()
  sp(f'{italic}Timmy:{reset} We have tents for you! Feel free to set it up where ever you want to! {villager1} and {villager2}, you can set up your tents as well! When you are done-')
  time.sleep(2)
  any_key2()
  sp(f'{italic}Tommy:{reset} -Come back to the {Green}Base{White} for more intructions!')
  time.sleep(1)
  any_key2()
  clear()
  print(f'{Green}Mission granted: Set up tent!{White}')
  time.sleep(1)
  any_key()
  clear()
  setting=True
  while setting:
    print('Setting up tent:\nNote: Because this is a tent, not your permanent home, place it anywhere it feels right')
    print('[1] Near the beach\n[2] Near the base\n[3] Near the river\n[4] Near the forest')
    setup_tent = input('> ')
    clear()

    if setup_tent == '1':
      print(f'{Green}You set it up near the beach!{White}')
      time.sleep(2)
      any_key()
      clear()
      setting=False
      if guest == True:
        pass
      else:
        dataset = 'Tent: Near beach'
        outputFile = 'tent.env'
        fw = open(outputFile, 'wb')
        pickle.dump(dataset, fw)
        fw.close()
    elif setup_tent == '2':
      print(f'{Green}You set it up near the base!{White}')
      time.sleep(2)
      any_key()
      clear()
      setting=False
      if guest == True:
        pass
      else:
        dataset = 'Tent: Near base'
        outputFile = 'tent.env'
        fw = open(outputFile, 'wb')
        pickle.dump(dataset, fw)
        fw.close()
    elif setup_tent == '3':
      print(f'{Green}You set it up near the river!{White}')
      time.sleep(2)
      any_key()
      clear()
      setting=False
      if guest == True:
        pass
      else:
        dataset = 'Tent: Near river'
        outputFile = 'tent.env'
        fw = open(outputFile, 'wb')
        pickle.dump(dataset, fw)
        fw.close()
    elif setup_tent == '4':
      print(f'{Green}You set it up near the forest!{White}')
      time.sleep(2)
      any_key()
      clear()
      setting=False
      if guest == True:
        pass
      else:
        dataset = 'Tent: Near forest'
        outputFile = 'tent.env'
        fw = open(outputFile, 'wb')
        pickle.dump(dataset, fw)
        fw.close()
    else:
      print(f'{Red}Invalid Choice!{White}')
      time.sleep(2)
      any_key()
      clear()
  
  print(f'{Green}Tent Placed!{White}')
  time.sleep(1)
  any_key()
  sp('\nBecause you finished placing your tent, you went back for more instructions...')
  time.sleep(2)
  any_key()
  clear()
  tentplacing=['Near the Beach','Near the Base','Near the River','Near the Forest']
  idk5=True
  while idk5:
    tentplace1=random.choice(tentplacing)
    tentplace2=random.choice(tentplacing)
    if tentplace1 == tentplace2:
      tentplace2=random.choice(tentplacing)
    else:
      idk5=False
  sp(f'{italic}Tom Nook:{reset} Ah {Blue}{username}{White}! I see you\'ve set up your tent! How about you help {villager1} and {villager2} set up their tents? Go {tentplace1} and {tentplace2} to find them!')
  time.sleep(2)
  any_key2()
  clear()
  print(f'{Green}Go Help {villager1} and {villager2} set up their tents!{White}')
  time.sleep(2)
  any_key()
  clear()
  if guest == True:
    pass
  else:
    dataset = 'Helping villagers'
    outputFile = 'thingy.env'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()
  thingy=True
  while thingy:
    go = input(f'Will you go {tentplace1} or {tentplace2}?\nNote: Enter the exact statement\n> ')
    clear()

    if go == tentplace1:
      thingy=False
      print(f'{Green}You went to help {villager1}!{White}')
      time.sleep(2)
      any_key()
      clear()
      sp(f'{italic}{villager1}:{reset} Oh! Hello {Blue}{username}{White}! I need some help setting up my tent... Should I set it up here or somewhere else?')
      time.sleep(2)
      any_key2()
      yn=input('y/n\n> ').lower()

      if yn == 'y':
        sp(f'{italic}{villager1}:{reset} Really? Thanks for helping me {Blue}{username}{White}! I\'m gonna go back to the base now!')
        time.sleep(2)
        any_key()
        clear()
      elif yn == 'n':
        sp(f'{italic}{villager1}:{reset} Hmmm, where should I put it then?')
        time.sleep(1)
        any_key2()
        idk3=True
        while idk3:
          print('NTB(near the beach)/NTF(near the forest)/NTB2(near the base)/NTR(near the river)')
          f = input('> ')
          clear()

          if f == 'NTB':
            sp(f'{italic}{villager1}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTB2':
            sp(f'{italic}{villager1}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTR':
            sp(f'{italic}{villager1}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTF':
            sp(f'{italic}{villager1}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          else:
            print(f'{Red}Invalid Choice!{White}')
            time.sleep(2)
            any_key()
            clear()

      print(f'{Green}You went to help {villager2}!{White}')
      time.sleep(2)
      any_key()
      clear()
      sp(f'{italic}{villager2}:{reset} Oh! Hello {Blue}{username}{White}! I need some help setting up my tent... Should I set it up here or somewhere else?')
      time.sleep(2)
      any_key2()
      yn=input('y/n\n> ').lower()

      if yn == 'y':
        sp(f'{italic}{villager2}:{reset} Really? Thanks for helping me {Blue}{username}{White}! I\'m gonna go back to the base now!')
        time.sleep(2)
        any_key()
        clear()
      elif yn == 'n':
        sp(f'{italic}{villager2}:{reset} Hmmm, where should I put it then?')
        time.sleep(1)
        any_key2()
        idk3=True
        while idk3:
          print('NTB(near the beach)/NTF(near the forest)/NTB2(near the base)/NTR(near the river)')
          f = input('> ')
          clear()

          if f == 'NTB':
            sp(f'{italic}{villager2}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTB2':
            sp(f'{italic}{villager2}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTR':
            sp(f'{italic}{villager2}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTF':
            sp(f'{italic}{villager2}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          else:
            print(f'{Red}Invalid Choice!{White}')
            time.sleep(2)
            any_key()
            clear()    

    elif go == tentplace2:
      thingy=False
      print(f'{Green}You went to help {villager2}!{White}')
      time.sleep(2)
      any_key()
      clear()
      sp(f'{italic}{villager2}:{reset} Oh! Hello {Blue}{username}{White}! I need some help setting up my tent... Should I set it up here or somewhere else?')
      time.sleep(2)
      any_key2()
      yn=input('y/n\n> ').lower()

      if yn == 'y':
        sp(f'{italic}{villager2}:{reset} Really? Thanks for helping me {Blue}{username}{White}! I\'m gonna go back to the base now!')
        time.sleep(2)
        any_key()
        clear()
      elif yn == 'n':
        sp(f'{italic}{villager2}:{reset} Hmmm, where should I put it then?')
        time.sleep(1)
        any_key2()
        idk3=True
        while idk3:
          print('NTB(near the beach)/NTF(near the forest)/NTB2(near the base)/NTR(near the river)')
          f = input('> ')
          clear()

          if f == 'NTB':
            sp(f'{italic}{villager2}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTB2':
            sp(f'{italic}{villager2}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTR':
            sp(f'{italic}{villager2}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTF':
            sp(f'{italic}{villager2}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          else:
            print(f'{Red}Invalid Choice!{White}')
            time.sleep(2)
            any_key()
            clear()
      
      print(f'{Green}You went to help {villager1}!{White}')
      time.sleep(2)
      any_key()
      clear()
      sp(f'{italic}{villager1}:{reset} Oh! Hello {Blue}{username}{White}! I need some help setting up my tent... Should I set it up here or somewhere else?')
      time.sleep(2)
      any_key2()
      yn=input('y/n\n> ').lower()

      if yn == 'y':
        sp(f'{italic}{villager1}:{reset} Really? Thanks for helping me {Blue}{username}{White}! I\'m gonna go back to the base now!')
        time.sleep(2)
        any_key()
        clear()
      elif yn == 'n':
        sp(f'{italic}{villager1}:{reset} Hmmm, where should I put it then?')
        time.sleep(1)
        any_key2()
        idk3=True
        while idk3:
          print('NTB(near the beach)/NTF(near the forest)/NTB2(near the base)/NTR(near the river)')
          f = input('> ')
          clear()

          if f == 'NTB':
            sp(f'{italic}{villager1}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTB2':
            sp(f'{italic}{villager1}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTR':
            sp(f'{italic}{villager1}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          elif f == 'NTF':
            sp(f'{italic}{villager1}:{reset} Ok then! Thanks {Blue}{username}{White}!')
            time.sleep(2)
            any_key()
            clear()
          else:
            print(f'{Red}Invalid Choice!{White}')
            time.sleep(2)
            any_key()
            clear()

    else:
      print(f'{Red}Invalid Choice!{White}')
      time.sleep(2)
      any_key()
      clear()
  
  sp(f'{italic}Tom Nook:{reset} I see you\'ve helped {villager1} and {villager2} with their tents! Nice job! Let\'s move on to the next step -')
  time.sleep(1)
  any_key2()
  sp(f'{italic}Tommy:{reset} -Food! YES!')
  time.sleep(1)
  any_key2()
  sp(f'{italic}Tom Nook:{reset} Yes {Blue}{username}{White}, food! It seems like there are some apple trees as well as tree branches... Would you get {Green}6 apples and 10 branches?{White}')
  time.sleep(2)
  any_key()
  clear()
  print(f'{Green}Mission Granted: Get 6 apples and 10 branches!{White}')
  time.sleep(1)
  any_key()
  clear()

  thingy=True
  while thingy:
    print('What will you do:\n[1] Get apples\n[2] Get branches')
    ot = input('> ')
    clear()

    if ot == '1':
      print(f'{Green}You went to get apples!{White}')
      time.sleep(2)
      any_key()
      clear()
      print('You looked across the small meadow, and looked for apples!')
      time.sleep(1)
      any_key()
      print(f'{Green}You successfully found 6 apples!{White}')
      time.sleep(1)
      any_key()
      clear()
      print(f'{Green}Now you went looking for branches!{White}')
      time.sleep(1)
      any_key()
      clear()
      print('You found a total of 5 branches, but you couldn\'t find anymore...')
      time.sleep(2)
      any_key()
      sp(f'{italic}Timmy:{reset} {Blue}{username}{White}, you can SHAKE the trees to find more branches!')
      time.sleep(2)
      any_key2()
      clear()
      print(f'{Green}You shook the trees and got 2 more branches! You also went to other trees and got a total of 10 branches!{White}')
      time.sleep(2)
      any_key()
      sp(f'As you got all you needed, you headed back to the {Green}base!{White}')
      time.sleep(1)
      any_key()
      clear()
      thingy=False
    
    elif ot == '2':
      print(f'{Green}You went to get branches!{White}')
      time.sleep(2)
      any_key()
      clear()
      print('You looked across the small meadow, and looked for branches!')
      time.sleep(1)
      any_key()
      print(f'{Green}You successfully found 5 branches, however, you couldnt find anymore...')
      time.sleep(1)
      any_key()
      sp(f'{italic}Timmy:{reset} {Blue}{username}{White}, you can SHAKE the trees to find more branches!')
      time.sleep(2)
      any_key2()
      clear()
      print(f'{Green}You shook the trees and got your remaining branches!{White}')
      time.sleep(1)
      any_key()
      clear()
      print(f'{Green}Now you went looking for apples!{White}')
      time.sleep(1)
      any_key()
      clear()
      print('You found a total of 6 apples!')
      time.sleep(2)
      any_key()
      sp(f'As you got all you needed, you headed back to the {Green}base!{White}')
      time.sleep(1)
      any_key()
      clear()
      thingy=False
    
    else:
      print(f'{Red}Invalid Choice!{White}')
      time.sleep(2)
      any_key()
      clear()
  
  #bruh, tom nook is pretty much the boss lmao
  sp(f'{italic}Tom Nook:{reset} Now that we have the branches, lets start a fire!')
  time.sleep(1)
  any_key2()
  print(f'{Green}Your group started a fire!{White}')
  time.sleep(2)
  any_key()
  clear()
  sp(f'{italic}Tom Nook:{reset} Also, ive looked at these apples, and it seems like they are edible! So let us make juice!')
  time.sleep(2)
  any_key2()
  sp(f'{italic}Timmy:{reset} Lets toast to our island!')
  time.sleep(1)
  any_key2()
  clear()
  print(f'{Green}Your group made apple juice!{White}')
  time.sleep(1)
  any_key()
  print(f'{Green}You toasted to your island!{White}')
  time.sleep(1)
  any_key()
  clear()
  sp(f'{italic}Tommy:{reset} {Blue}{username}{White}, if you feel tired, feel free to go into your tent and sleep! Oh, by the way, let me give you this: ')
  time.sleep(1)
  print(f'{Green}You got a sleeping pack bundle!{White}')
  time.sleep(2)
  any_key()
  clear()
  sp(f'{italic}Tommy:{reset} You can put this anywhere you want in your tent, it has your bed, radio, and lamp!')
  time.sleep(2)
  any_key2()
  sp(f'{italic}Tommy:{reset} Ill see you in the morning!')
  time.sleep(1)
  any_key2()
  clear()
  sp(f'{Green}You went in your tent because you were sleepy...\nYou also set up your things the simple way, as you are too tired to do nothing but sleep...\nHowever, as you take out the radio, you here D.J. K.K!{White}')
  time.sleep(1)
  sp(f'{italic}DJ KK:{reset} Cool. Settle back and dig this groove. {italic}Main music theme plays as you fall asleep...{reset}')#idk if these are exact words, but here goes
  time.sleep(2)
  any_key()
  if guest == True:
    pass
  else:
    dataset = 'Meets DJ KK and sleeps'
    outputFile = 'thingy.env'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()
  clear()
  print(f'{Green}You slept!{White}')
  time.sleep(1)
  any_key()
  clear()
  sp(f'{italic}Timmy:{reset} {Blue}{username}{White}! Wake up! Sorry to wake you up so early, but its time to go! We have some things to show you!')
  time.sleep(2)
  any_key2()
  sp(f'{italic}Tommy:{reset} These things are {Green} a NookPhone, connected to Nook Miles and Bells!{White}')
  time.sleep(1)
  any_key2()
  sp(f'{italic}Timmy:{reset} First, we\'ll give you the items, and then explain them to you!')
  time.sleep(1)
  any_key2()
  print(f'{Green}NookPhone recieved!{White}')
  time.sleep(2)
  any_key()
  if guest == True:
    pass
  else:
    dataset = f'Number of villagers: 2\nIsland Name: {your_name_island}\nVillager Names: {villager1} and {villager2}\nItems: NookPhone,'
    outputFile = 'stats.env'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()
  
  sp(f'{italic}Tommy:{reset} So how a NookPhone works is enter NP for NookPhone opening! Nook Miles and Bells are the currency. To ever view your current amount, go into your NookPhone, and then enter CUR.')#maybe change cmd name?
  time.sleep(2)
  any_key2()
  sp(f'{italic}Timmy:{reset} If you ever need more help, you can either enter HELP in your NookPhone, or come to us!')
  time.sleep(2)
  any_key2()
  sp(f'{italic}Tommy:{reset} However, that wasnt the main reason that we came here! Our boss wanted you to come to the base to talk! So meet us up there!')
  time.sleep(2)
  any_key2()
  clear()
  print(f'{Green}Mission Granted: Go to base!{White}')
  time.sleep(1)
  any_key()
  clear()
  idk=True
  while idk:
    print('Will you explore your phone or go back to the base? NP/b')
    npb = input('> ').lower()
    clear()

    if npb == 'np':
      print(f'{Green}You are exploring your phone!{White}')
      time.sleep(2)
      any_key()
      clear()
      phone=True
      idk=False
      while phone:
        hrmm = input('CMDs - NOOKPHONE\n> ').lower()
        clear()

        if hrmm == 'help':
          print('HELP - Assistance\nEXIT - Exit out of phone\nCUR - Your balance\nMAP - Take a look at the map\nMore coming soon!')
          time.sleep(2)
          any_key()
          clear()
        
        elif hrmm == 'exit':
          phone=False
        
        elif hrmm == 'cur':
          print(f'{Green}You have 0 bells and miles!{White}')
          time.sleep(2)
          any_key()
          clear()

        elif hrmm == 'map':
          if A == True:
            print(a)
          else:
            if B == True:
              print(b)
            else:
              if C == True:
                print(c)
              else:
                if D == True:
                  print(d)
                else:
                  pass

    elif npb == 'b':
      idk=False
    
    else:
      print(f'{Red}Invalid Choice!{White}')
      time.sleep(2)
      any_key()
      clear()
  
  clear()
  print(f'{Green}You went back to the base!{White}')
  time.sleep(2)
  any_key()
  clear()
  sp(f'{italic}Tom Nook:{reset} Ah {Blue}{username}{White}! I see you\'re awake! First, {Blue}{username}{White}, I\'ll give you some {Green}customization kits{White}! ')
  time.sleep(2)
  any_key2()
  sp(f'{italic}Tom Nook:{reset} Let\'s work on your first fishing rod! Of course, I havent made a prefected model yet... But it still works! Choose the {Green}Flimsy Fishing Rod{White} Model from the workshop!')
  time.sleep(2)
  any_key2()
  clear()
  print(f'{Green}Go to the workshop and make the FLIMSY FISHING ROD!{White}')
  time.sleep(2)
  any_key()
  clear()
  sp('You went to the workshop!')#the workshop is not a place, its an object/thingy
  time.sleep(1)
  any_key2()
  if guest == True:
    pass
  else:
    dataset = 'Going to workshop for the first time'
    outputFile = 'thingy.env'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()
  workshop=True
  while workshop:
    print('WorkShop:')
    print('[1] Flimsy Fishing Rod\n[2] ???\n[3] ???')
    ws = input('> ')
    clear()

    if ws == '1':
      print('Flimsy Fishing Rod\nMaterials: 5x tree branches OR ??? Miles/Bells')
      time.sleep(1)
      any_key2()
      sp(f'{italic}Tom Nook:{reset} {Blue}{username}{White}! To build in the workshop, you need {Green}5x tree branches!{White} So gather them outside! Once you\'re done, come back to the workshop!')
      time.sleep(2)
      any_key2()
      clear()
      workshop=False
    
    else:
      print(f'{Red}You havent unlocked it or it isnt a choice!{White}')
      time.sleep(2)
      any_key()
      clear()
  
  print(f'{Green}Gather 5x tree branches!{White}')
  time.sleep(1)
  any_key()
  clear()
  idk2=True
  if guest == True:
    pass
  else:
    dataset = 'Gathering flimsy fishing rod materials'
    outputFile = 'thingy.env'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()
  while idk2:
    print('Menu:\n[1] Gather 5x branches\n[2] Exit Game')
    hrmm = input('> ')
    clear()

    if hrmm == '1':
      print(f'{Green}You went to the meadow and gathered 5x tree branches!{White}')
      time.sleep(2)
      any_key()
      clear()
      idk2=False
    
    elif hrmm == '2':
      idk2=False
      menu=True
      while menu:
        print('Exit Menu:\n[1] Exit without saving\n[2] Exit and save\n[3] Resume')
        heh = input('> ')
        clear()

        if heh == '1':
          hehe = True
          while hehe:
            print('Are you sure? y/n')
            yn = input('> ').lower()
            clear()

            if yn == 'y':
              exit('Ok then! Bye!')  
              inputFile = 'thingy.env'
              fd = open(inputFile, 'rb')
              dataset = pickle.clear(fd)
            
            elif yn == 'n':
              hehe=False
            
            else:
              print(f'{Red}Invalid Choice!{White}')
              time.sleep(1)
              any_key()
              clear()
        
        elif heh == '2':
          hehe = True
          while hehe:
            print('Are you sure? y/n')
            yn = input('> ').lower()
            clear()

            if yn == 'y':
              print(f'{Green}Done! Bai!')
              time.sleep(2)
              any_key()
              clear()
              exit()

            elif yn == 'n':
              hehe=False
            
            else:
              print(f'{Red}Invalid Choice{White}')
              time.sleep(2)
              any_key()
              clear()
        
        elif heh == '3':
          menu=False
          idk=True
        
        else:
          print(f'{Red}Invalid Choice!{White}')
          time.sleep(1)
          any_key()
          clear()
    
    else:
      print(f'{Red}Invalid Choice!{White}')
      time.sleep(2)
      any_key()
      clear()

  sp(f'{italic}Tom Nook:{reset} I see you\'ve gathered the materials {Blue}{username}{White}! Lets get started at the workshop!')
  time.sleep(2)
  any_key()
  clear()
  sp(f'You went to the {Green}Workshop!{White}')
  time.sleep(1)
  any_key()
  clear()
  sp(f'{italic}Tom Nook:{reset} Lets start up the workshop again!')
  time.sleep(1)
  any_key()
  clear()
  workshop=True
  while workshop:
    print('Workshop:')
    print('[1] Flimsy Fishing Rod\n[2] ???\n[3] ???')
    ws = input('> ')
    clear()

    if ws == '1':
      workshop=False
      idk98=True
      while idk98:
        print(f'Flimsy Fishing Rod:\nMaterials: 5x tree branches\nNote: Enter build\n{Green}<Build>{White}')
        buildffr = input('> ').lower()
        clear()

        if buildffr == 'build':
          idk98=False
          print(f'{Green}You built the {Orange}Flimsy Fishing Rod!{White}')
          time.sleep(1)
          any_key()
          clear()
          sp(f'{italic}Tom Nook:{reset} You\'ve built it {Blue}{username}{White}! Just remember, it breaks when you catch 10 things! Go try it out now!')
          time.sleep(2)
          any_key()
          clear()
        
        else:
          print(f'{Red}Invalid Choice!{White}')
          time.sleep(2)
          any_key()
          clear()

      else:
        print(f'{Red}Invalid Choice or locked!{White}')
        time.sleep(2)
        any_key()
        clear()
  
  print(f'{Green}You got a Flimsy Fishing Rod!{White}')
  time.sleep(2)
  any_key()
  clear()
  if guest == True:
    pass
  else:
    dataset = f'Number of villagers: 2\nIsland Name: {your_name_island}\nVillager Names: {villager1} and {villager2}\nItems: NookPhone, Flimsy Fishing Rod,'
    outputFile = 'stats.env'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()
  
  idk43=True
  while idk43:
    print('Fishing Menu:')
    print('[1] Ocean\n[2] River\n[3] Lake')
    fisht = input('> ')

    if fisht == '1':
      idk43=False
      print(f'{Green}You decided to fish in the Ocean!{White}')
      time.sleep(1)
      any_key()
      clear()
      ofish = ['Sea Butterfly','Sea Horse','Clown Fish','Butterfly Fish','Surgeonfish','Zebra Turkeyfish','Napoleonfish','Blowfish','Puffer Fish','Anchovy','Horse Mackerel','Sea Bass','Barred Knifejaw','Red Snapper','Dab','Olive Flounder','Squid','Moray Eel','Ribbon Eel','Ocean Sunfish','Ray','Saw Shark','Hammerhead Shark','Great White Shark','Whale Shark','Suckerfish','Football Fish','Oarfish','Barreleye','Coelacanth']#ocean fish
      fishing=True
      while fishing:
        OFISH=random.choice(ofish)
        print('Ocean Fishing:')
        print('Press ENTER to fish and enter BACK to exit out of fishing')
        p = input('> ').lower()

        if p == '':
          pass
        
        elif p == 'back':
          fishing=False
        
        else:
          pass#same as fishing(pressing enter)

    elif fisht == '2':
      idk43 = False
      print(f'{Green}You decided to fish in the River!{White}')
      time.sleep(1)
      any_key()
      clear()
      rfish = ['Bitterling','Pale Chub','Crucian Carp','Dace','Soft-shelled Turtle','Snapping Turtle','Freshwater Goby','Loach','Bluegill','Yellow Perch','Black Bass','Tilapia','Pike','Sweetfish','Cherry Salmon','Char','Golden Trout','String Fish','Salmon','King Salmon','Mitten Crab','Guppy','Nibble Fish','Angel Fish','Betta','Neon Tetra','Rainbowfish','Piranha','Arowana','Dorado','Arapaima','Saddled Bichir','Sturgeon']#river fish

    elif fisht == '3':
      idk43 = False
      print(f'{Green}You decided to fish in the Lake!{White}')
      time.sleep(1)
      any_key()
      clear()
      lfish = ['']#lake fish
    
    else:
      print(f'{Red}Invalid Choice!{White}')
      time.sleep(2)
      any_key()
      clear()
  
else:
  inputFile = 'thingy.env'
  fd = open(inputFile, 'rb')
  dataset = pickle.load(fd)
  #add more data things-done
  idk=True
  while idk:#not in order btw

    if dataset == 'Meets DJ KK and sleeps':
      pass
    
    elif dataset == 'Gathering flimsy fishing rod materials':
      pass

    elif dataset == 'Going to workshop for the first time':
      pass
    
    elif dataset == 'Island name decided':
      pass
    
    elif dataset == 'Helping villagers':
      pass

    elif dataset == 'Fishing for first time':
      pass

    else:
      continue