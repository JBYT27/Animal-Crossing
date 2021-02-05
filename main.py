import os, time, sys, random
#from replit import db
from fish import *
from map import *

def clear():
  os.system('clear')

def any_key():
      print('\n\n<NEXT>\t[Press any KEY to continue]')
      input()

def any_key2():
  print('\n<NEXT>\t[Press any KEY to continue]')
  input()

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
    print('Login Menu:')
    username = input('Username\n> ')
    clear()

    with open('username.env','r') as user_read:
      reead = user_read.read()
      
      if username in reead:
        user_read.close()
        print(f'{Green}Valid Username!{White}')
        time.sleep(2)
        any_key()
        clear()
        login_signup=False
      else:
        user_read.close()
        print(f'{Red}Invalid Username!{White}')
        time.sleep(2)
        any_key()
        clear()

  elif ls_menu == '2':
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
        with open('username.env','a') as user:
          user.write(f'{username}\n')
          user.close()
        time.sleep(2)
        any_key()
        login_signup=False
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
      with open('username.env','a') as user:
        user.write(f'{username}\n')
        user.close()
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
        island_shape=False
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
        island_shape=False
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
        island_shape=False
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
  for i in range(3):
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
  thingy=True
  while thingy:
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
      thingy=False

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
    with open('stats.env','a') as stats:
      stats.write('Number of Villagers: 2\n')
      stats.write(f'Island Name: {your_name_island}\n')
      stats.close()
  
  sp(f'{italic}Tommy:{reset} Lets get started with the poll everyone!')
  time.sleep(2)
  any_key2()
  print(f'\n{italic}Timmy:{reset} {Green}{island_name1} island{White}\n{italic}Tommy:{reset} {Green}{island_name2} island{White}\n{italic}Tom Nook:{reset} {Green}{island_name3} island{White}\n{italic}{villager1}:{reset} {Green}{island_name4} island{White}\n{italic}{villager2}:{reset} {Green}{island_name5} island{White}\n{Blue}{username}:{White} {Green}{your_name_island} island{White}')


else:
  pass