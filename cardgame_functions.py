import random
from copy import *

#Prints all of the rules for the user to read if needed or continue once they have read them
def red7_rules(prompt):
  while True:
    user_input = input(prompt)
    try:
      if user_input.strip().lower() == "x":
        print("""
The rules of Red 7 are simple! 
There are 4 components:
  - 49 cards, numbered 1 to 7 in seven colors
  - 4 icon/color reference guide cards
  - 2 turn option guide cards
  - 1 canvas (pile) card

Gameplay:
  The rule for winning at Red is straight forward: Have the best card! But will you still be playing the same game when your turn ends? If you're not winning by the current game's rule at the end of your turn, you're out, and the last person standing wins the round.
  The deck consists of 49 cards numbered 1-7, in each of the seven rainbow colors. A 7 is always higher than a 6, but a Red 6 is higher than an Orange 6, and so on down the color spectrum (Red, Orange, Yellow, Green, Blue, Indigo, Violet). When comparing two cards, compare value first, then color.
  
  
  To begin a game of Red7, deal out a seven-card hand to each player, and then deal one more card faceup in front of each player to start their Palette.
  Start the Canvas (discard pile) with the Red card. The top card of the Canvas pile determines what the rules are. The player with the lowest card on their Palette is currently the worst at Red, so that player will go first.

Game Turn:
  On your turn, you must take one of the following actions:
  Play a card faceup from your hand to your Palette.
  Discard a card from your hand to the Canvas to change the game to the rule of the discarded card's color. You must be winning the new game after you do this.
  Play a card from your hand to your Palette AND THEN discard a card to the Canvas. You must be winning the game after you do this.
  Do nothing, and lose. If your hand is empty, you must do this.
  If you are not winning the game at the end of your turn, you lose and are out of the round. If you are ever the last player in the game, you win the round!
  You are currently winning a game if your Palette contains more cards that meet the current game's rule than any other player. To break a tie, look at each tied player's highest card that follows the rule, checking its value, then its color if necessary.
  If you have no cards (for Green or Violet) that follow the rule, you are not winning. Examples are to the right for each rule. If you have no cards in your hand at the start of your turn, you lose since you are unable to do anything to win by the end of your turn.

End Game:
  Finally, if you do not have any cards left in your hand during your turn, you lose. If you are not winning at the end of your turn, you lose. If you do not play a card during your turn, you will lose. But, if you are the last player standing, you win!!! Best of luck...
""")
      elif user_input.strip().lower() == "c":
        return True
      else:
        raise Exception
    except:
      print("Make sure to enter either s or c!")

#Builds deck
def build_deck():
  deck = []

  #List of all colors and possible numbers
  colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
  numbers = ["1", "2", "3", "4", "5", "6", "7"]

  #For each color, each number is ran and matched together then appended to the deck list. This allows for all possible combonations of cards to be created
  for i in colors:
    for num in numbers:
      card = i + " " + num
      deck.append(card)

  return deck

#Deals the starting cards to all players
def deal_cards(deck, num_cards, num_players):

  #All empty lists of possible lists that will be added to
  players = []
  
  player_hand = []
  bot_hand1 = []
  bot_hand2 = []
  bot_hand3 = []
  player_palette = []
  bot1_palette = []
  bot2_palette = []
  bot3_palette = []

  #If user only wants one bot this will run --> Not going to repeat so basically this if statement checks to see hwo many bots the user wants and then will run that respective code so that the right amount of cards are dealt to the right amount of players
  if num_players == 1:
    #Pops last item of the deck which removes it then appends that card to the current player palette. Runs for both palettes of players
    player_palette.append(deck.pop())
    bot1_palette.append(deck.pop())

    #Until there are 7 cards in the hand, this will keep popping a card from the deck into each players hand until they all have 7
    while len(player_hand) < 7:
      player_hand.append(deck.pop())
      bot_hand1.append(deck.pop())
    #Creates each player which is a list of lists with their palette hand and tag
    player = [player_hand, player_palette, "player"]
    bot1 = [bot_hand1, bot1_palette, "bot1"]
    #Players is a list players which is a list of lists
    players = [player, bot1]

  #Rest of this is the same as before but just for more bots
  elif num_players == 2:
    player_palette.append(deck.pop())
    bot1_palette.append(deck.pop())
    bot2_palette.append(deck.pop())
    while len(player_hand) < 7:
      player_hand.append(deck.pop())
      bot_hand1.append(deck.pop())
      bot_hand2.append(deck.pop())
    player = [player_hand, player_palette, "player"]
    bot1 = [bot_hand1, bot1_palette, "bot1"]
    bot2 = [bot_hand2, bot2_palette, "bot2"]
    players = [player, bot1, bot2]
  else:
    player_palette.append(deck.pop())
    bot1_palette.append(deck.pop())
    bot2_palette.append(deck.pop())
    bot3_palette.append(deck.pop())
    while len(player_hand) < 7:
      player_hand.append(deck.pop())
      bot_hand1.append(deck.pop())
      bot_hand2.append(deck.pop())
      bot_hand3.append(deck.pop())
    player = [player_hand, player_palette, "player"]
    bot1 = [bot_hand1, bot1_palette, "bot1"]
    bot2 = [bot_hand2, bot2_palette, "bot2"]
    bot3 = [bot_hand3, bot3_palette, "bot3"]
    players = [player, bot1, bot2, bot3]

  #Returns the final list of players
  return players

"""
Define all other functions that you will rely on in your game below. Since we will be importing these into the main Python script, each function should be well defined with appropriate parameters and return values.
"""

#Shuffles deck of cards
def shuffle_deck(deck):
  
  #Finds length of the deck of cards minus 1 (returns 51)
  last_card = len(deck) - 1

  #Starts from 1 until it reaches 1000 going up by 1 by default, this for loop will randomly pick 2 cards and swap their position 1000 times.
  for i in range(1, 1000):
    # a and b are random cards chosen between 0 (first card in list) and last_card (51 or last card in list)
    a = random.randint(0, last_card)
    b = random.randint(0, last_card)
    #If a and b are the same card, card b will be regenerated until it is not the same as a
    while a == b:
      b = random.randint(0, last_card)

    #Replaces order of deck (list) of card a and card b by swapping their positions in the list.
    deck[a], deck[b] = deck[b], deck[a]

  #Returns shuffled deck
  return deck

#Allows user to keep shuffling deck until they want to continue and makes sure they input only an s to shuffle or c to continue
def user_shuffle(prompt, deck):
  while True:
    user_input = input(prompt)
    try:
      if user_input.strip().lower() == "s":
        deck = shuffle_deck(deck)
        print("Nice! Now you can choose to shuffle again or continue!")
      elif user_input.strip().lower() == "c":
        return deck
      else:
        raise Exception
    except:
      print("Make sure to enter either s or c!")

#Checks if the inputed number is wiithin the min and max numbers accepted. If not, the loop will run until a valid int is entered
def check_int(prompt, min, max):
  while True:
    try:
      #Asks for input using prompt
      user_input = int(input(prompt))
      #If input is not within parameters then error is raised to keep loop running
      if user_input < min or user_input > max:
        raise ValueError
      else: 
        #If user inputs valid number it is returned
        return user_input
    except ValueError:
      print(f"Ensure to enter an integer between {min} and {max}!")

#Indexes one card to retrieve the number value from it then int() it to make it an integer data type
def get_card_value(card):
  card_value = int(card[-1:])
  #Returns the number
  return card_value

#Same as above function but gets the string of the color instead of int number of the card.
def get_card_color(card):
  card_color = card[:-2]
  #Returns the color and strips any negative space after the strong like spaces
  return card_color.strip()

#Takes a card and gives it a number value based on what color it is (red is highest value)
def card_color_rank(card):
  #Uses dictionary with color strings as keys and integers as values assigned to each
  colors = {
    'Red': 7,
    'Orange': 6,
    'Yellow': 5,
    'Green': 4,
    'Blue': 3,
    'Indigo': 2,
    'Violet': 1
  }

  #Returns a number
  return colors[get_card_color(card)]

#Finds lowest card of all players from their palettes to determine which player will start the game
def lowest_card_palette(players):
  lowest_value = 8
  lowest_color = 8

  #Goes through all palettes of all playres in players list
  for p in players:
    #Indexes the palette (second element)
    palette = p[1]
    #Only runs with palette having one card so this index will get the card
    palette_card = palette[0]
    #Gets num value of card
    value_card = int(palette_card[-1:])
    #Gets color of card
    palette_color = palette_card[:-2]

    #Assigns card value based on color (basically card color function)
    if palette_color == 'Red':
      palette_color = 7
    elif palette_color == 'Orange':
      palette_color = 6
    elif palette_color == 'Yellow':
      palette_color = 5
    elif palette_color == 'Green':
      palette_color = 4
    elif palette_color == 'Blue':
      palette_color = 3
    elif palette_color == 'Indigo':
      palette_color = 2
    else:
      palette_color = 1

    #If values of two cards are equal, it compares color and the lower color will remain lowest card
    if lowest_value == value_card:
      if palette_color < lowest_color:
        lowest_color = palette_color
        lowest_player = p

    #Compares values of card and lowest will be new lowest card
    else:
      if value_card < lowest_value:
        lowest_value = value_card
        lowest_player = p
        lowest_color = palette_color

  #Returns lowest card by the code above comapring all cards from each palette
  return lowest_player

#Gets highest card of all players from all cards in their palettes. Used for red canvas rule. Works the same way as lowest card all players but indtead find the highest card meaning it uses different comparisons.
def highest_card_all_players(players):
  highest_value = 0
  highest_color = 0

  for player in players:
    
    palette = player[1]
  
    for p in palette:
  
      value_card = int(p[-1:])
      palette_color = p[:-2]
      
      if palette_color == 'Red':
        palette_color = 7
      elif palette_color == 'Orange':
        palette_color = 6
      elif palette_color == 'Yellow':
        palette_color = 5
      elif palette_color == 'Green':
        palette_color = 4
      elif palette_color == 'Blue':
        palette_color = 3
      elif palette_color == 'Indigo':
        palette_color = 2
      else:
        palette_color = 1
        
      if highest_value == value_card:
        if palette_color > highest_color:
          highest_color = palette_color
          highest_player = player
  
      else:
        if value_card > highest_value:
          highest_value = value_card
          highest_player = player
          highest_color = palette_color

  #Returns highest card all players
  return highest_player

#Only gets highest card of one player. Same as highest card all players function but only takes one list which is the player, not the whole player list. This only compares the cards in a players palette
def get_player_highest_card(palette):

  highest_value = 0
  highest_color = 0
  highest_card = ""
  
  for p in palette:
    palette_value = int(p[-1:])
    palette_color = palette[:-2]

    if palette_color == 'Red':
      palette_color = 7
    elif palette_color == 'Orange':
      palette_color = 6
    elif palette_color == 'Yellow':
      palette_color = 5
    elif palette_color == 'Green':
      palette_color = 4
    elif palette_color == 'Blue':
      palette_color = 3
    elif palette_color == 'Indigo':
      palette_color = 2
    else:
      palette_color = 1

    if palette_value > highest_value:
      highest_value = palette_value
      highest_card = p
      
    if palette_value == highest_value and palette_color > highest_color:
      highest_color = palette_color
      highest_card = p

  #Returns highest card of one player from their palette
  return highest_card

#Indexes the hand of a player from the player's list of hand palette and tag
def get_hand(player):
  hand = player[0]
  return hand

#Gets palette by indexing a different number than get_hand to return the palette from player's list
def get_palette(player):
  
  palette = player[1]

  return palette

#Same as check_int not sure why I made this -_-
"""def player_check(prompt, min, max):
  while True:
    try:
      player_input = int(input(prompt))
      if player_input < min or player_input > max:
        raise ValueError
      else:
        return player_input
    except ValueError:
      print(f"Make sure to input an integer between {min} and {max}!")"""

#Makes sure user inputs a card that is within their hand
def check_card(hand):

  while True:

    print("Which card from your hand would you like to play? Here is your hand right now:")

    #Sorts hand
    sort_palette(hand)
    for x in hand:
      #Prints all cards in player hand using colored text
      color_text(x)

    card_input = input("\033[0m ").strip()

    #Checks if card is in the players hand else it will loop using True loop until a valid card is entered
    if card_input in hand:
      return card_input
  
    else:
      print("That is not one of your cards!")

#Main player turn function
def player_turn(input, player_hand, player_palette, canvas):
  
   #Player adds card to palette
  if input == 1:
    #Checks if inputed card is in their hand
    action1_card = check_card(player_hand)
    if action1_card:
      #If it is, runs action1 function
      player_palette = action1(player_palette, action1_card)
      #Removes the card from their hand
      player_hand.remove(action1_card)
      return True
  #Player adds card to canvas
  elif input == 2:
    action2_card = check_card(player_hand)
    if action2_card:
      #Adds card color using index -2 to remove number and appends to canvas
      canvas.append(action2_card[:-2])
      #Removes card from hand
      player_hand.remove(action2_card)
      return True
  #User adds card to palette then discards card to canvas. Basically just action 1 and 2 in one turn
  elif input == 3:
    action1_card = check_card(player_hand)
    if action1_card:
      player_palette = action1(player_palette, action1_card)
      player_hand.remove(action1_card)

    action2_card = check_card(player_hand)
    if action2_card:
      canvas.append(action2_card[:-2])
      player_hand.remove(action2_card)
    
      return True
  #User does nothing
  else:
    return True

#Action 1 appends the card from hand to the palette
def action1(palette, card):
  palette.append(card)
  return palette

def play_again(prompt):
  #Same structure as check_input function but fitted to check if user enters not either a y or n.
  while True:
    #Input prompts user then stores in variable
    user_restart = input(f"{prompt}... Do you want to restart?: (y/n)")
    try:
      #Checks if user inputs anything other than a y or n
      if user_restart.strip().lower() != "y" and user_restart.strip().lower() != "n":
        #If input is not a y or n, expetion is raised which prompts user to input a valid value then loops back to start of while true loop
        raise Exception
      #If excpetion is not raised, user_restart value is returned where it will be compared in an if statement in next part of code.
      elif user_restart.strip() == "y":
        return True
      else:
        return False
    except:
      print("Ensure you input something! If you did, make sure it is either y or n")

#Checks the winning player based on canvas rule
def check_winning_player(canvas, players):
  #Takes the last element in list of canvas whihc is the current canvas rule card to find what function to call
  if canvas[-1] == "Red":
    #All returns will return the player (which is a list of 3 items) who best meets the canvas rule (winning)
    return canvas_red(players)
    
  elif canvas[-1] == "Orange":
    return canvas_orange(players)
    
  elif canvas[-1] == "Yellow":
    return canvas_yellow(players)
    
  elif canvas[-1] == "Green":
    return canvas_green(players)
    
  elif canvas[-1] == "Blue":
    return canvas_blue(players)
    
  elif canvas[-1] == "Indigo":
    return canvas_indigo(players)
    
  else:
    return canvas_violet(players) 

#Red rule: Highest Card
def canvas_red(players):

  #Finds highest card of all players then returns that player with the highest card
  highest_player = highest_card_all_players(players)
  
  return highest_player

#Orange rule: Most Of One Number
def canvas_orange(players):

  most_one_number_each_player = []

  #Runs through each player to get the most amount of cards that meet the card rule
  for p in players:

    #Gets palette for p (current player)
    each_palette = get_palette(p)

    #Appends to a final list a different list of all the cards that meet the canvas rule
    most_one_number_each_player.append(get_most_one_number(each_palette))

  #Returns the player that is winning which is determined in find_winning_player function which compares all the lists of the final list. Each list in the final list is the cards for that player that meets the canvas rule.
  return find_winning_player(most_one_number_each_player, players)
    
#Yellow rule: Cards Of One Color  
def canvas_yellow(players):

  #!!! Follows same procces as orange rule but calls a different function to match the canvas rule !!!
  most_one_color_each_player = []
  
  for p in players:

    each_palette = get_palette(p)
    
    most_one_color_each_player.append(get_most_one_color(each_palette))

  return find_winning_player(most_one_color_each_player, players)

#Green rule: Most Even Cards
def canvas_green(players):

  #!!! Follows same procces as orange rule but calls a different function to match the canvas rule !!!
  most_even_each_player = []
  
  for p in players:

    each_palette = get_palette(p)
    
    most_even_each_player.append(get_most_even(each_palette))

  #But, will check if the length of both lists are empty (have no cards that meet the rule) in which the highest card of all players will instead be returned as the find_winning_player function doesnt work with 2 empty lists
  if len(most_even_each_player[0]) == 0 and len(most_even_each_player[1]) == 0:
    return canvas_red(players)

  return find_winning_player(most_even_each_player, players)

#Blue rule: Most Of Different Colors
def canvas_blue(players):

  #!!! Follows same procces as orange rule but calls a different function to match the canvas rule !!!
  most_different_color_each_player = []
  
  for p in players:

    each_palette = get_palette(p)

    most_different_color_each_player.append(get_most_different_color(each_palette))

  return find_winning_player(most_different_color_each_player, players)

#Indigo rule: Most Cards In A Row
def canvas_indigo(players):

  #!!! Follows same procces as orange rule but calls a different function to match the canvas rule !!!
  most_in_row_each_player = []
  
  for p in players:

    each_palette = get_palette(p)
    
    most_in_row_each_player.append(get_most_in_row(each_palette))

  return find_winning_player(most_in_row_each_player, players)

#Violet rule: Cards below 4
def canvas_violet(players):

  most_below_4_each_player = []
  
  for p in players:

    each_palette = get_palette(p)

    most_below_4_each_player.append(get_below_4(each_palette))

  #But, will check if the length of both lists are empty (have no cards that meet the rule) in which the highest card of all players will instead be returned as the find_winning_player function doesnt work with 2 empty lists
  if len(most_below_4_each_player[0]) == 0 and len(most_below_4_each_player[1]) == 0:
    return canvas_red(players)
  
  return find_winning_player(most_below_4_each_player, players)

#Not sure where this is used?
"""def find_card_in_players(card, players):
  for p in players:
    if card in p[1]:
      return p[2]"""

#Orange rule finds most of one number for each palette
def get_most_one_number(palette):
  value_dictionary = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
  }

  #Runs through each card in palette and adds 1 value to the dictionary by accessing the key mathcing that card's int value
  for p in palette:
    value_dictionary[get_card_value(p)] += 1

  #Grabs highest value from each of the keys in the dictionary where the key is then stored in the most_number var
  most_number = max(value_dictionary, key = value_dictionary.get)

  #Goes through all palette cards again but finds any that match the dictionary key (rule cards) then appends them to the final rule cards list
  rule_cards = []
  for card in palette:
    if int(card[-1]) == most_number:
      rule_cards.append(card)

  #Returns rule cards
  return rule_cards

#Same as most one number but different dictionary keys to match the color not card value
def get_most_one_color(palette):
  color_dictionary = {
    'Red': 0,
    'Orange': 0,
    'Yellow': 0,
    'Green': 0,
    'Blue': 0,
    'Indigo': 0,
    'Violet': 0
  }

  for p in palette:
    color_dictionary[get_card_color(p)] += 1

  most_color = max(color_dictionary, key = color_dictionary.get)
  
  rule_cards = []
  for card in palette:
    if card[:-2].strip() == most_color:
      rule_cards.append(card)

  return rule_cards

#Gets most even cards for each palette
def get_most_even(palette):

  even_cards = []

  #For every card in palette, each cards is checked to see if divisable by 2 and remainder of 0 (meaning it is even)
  for p in palette:
    palette_card = get_card_value(p)
    if int(palette_card) % 2 == 0:
      #If even, added to rule cards list
      even_cards.append(p)

  return even_cards

#Gets list of different colors in palette
def get_most_different_color(palette):
  """color_dictionary = {
    'Red': 0,
    'Orange': 0,
    'Yellow': 0,
    'Green': 0,
    'Blue': 0,
    'Indigo': 0,
    'Violet': 0
  }

  for p in palette:
    color_dictionary[get_card_color(p)] += 1"""

  #Starts list by adding the first card in the palette as there cannot already be that color in the list
  list_of_different_colors = [palette[0]]

  #Goes through each card in palette and gets the card color then checks if that color is already in the rule card list. If it is, the next card is checked, but if not, that card is added to the list meaning any other card in palette with that color cannot be added again
  for card in palette:
    current_card_color = get_card_color(card)
    for x in list_of_different_colors:
      card_in_list_color = get_card_color(x)
      if current_card_color != card_in_list_color:
        list_of_different_colors.append(card)

  #Returns all cards of different colors
  return list_of_different_colors

#Gets most cards in a row --> This is so clapped to explain (T-T)
def get_most_in_row(palette):

  #Only runs if there is at least 2 cards in palette
  if len(palette) >= 2:
    in_run = False
    #Creates a palette where only one of each value is in the palette (ex. There cannot be Red 7 Orange 7 as this will ruin the code so this function removes the second card with the same value in this case Orange 7)
    palette = one_each_num_value(palette)
    #Gets value of card that will be comapred to by current card
    before_card_value = get_card_value(palette[0])
    #Keeps track of first card value for when the palette is indexed to find the most cards in row
    first_card_value = palette.index(palette[0])
    #Keeps track of how long the hgihest run is
    highest_run_len = 1

    #Starting from 1, going through the number of cards in the palette...
    for i in range(1, len(palette)):
      #The current card that will be comparing is the index[i(number of index postion of current card)]
      current_card = palette[i]
      #Gets the value of current card
      current_card_value = get_card_value(current_card)
      #If the run is False...
      if not in_run:
        #Checks if the current card value is exaclty one below the previous card
        if current_card_value == before_card_value - 1:
          #The new previous card becomes current card
          before_card_value = current_card_value
          #In run is True as the run is 2 now
          in_run = True
          run_len = 2
          #Only runs on first instance as the run length will always be larger than 1
          if run_len > highest_run_len:
            highest_run_len = run_len
            #Keeps track of the index of the first card of the new run
            first_card_value = palette.index(palette[i - 1])
        #Else if the current card is not only 1 lower...
        else:
          #Current card becomes new previous one
          before_card_value = current_card_value
      #Else if already in run...
      elif in_run:
        #Checks if current card is only 1 lower than previous card
        if current_card_value == before_card_value - 1:
          #If so, the run length adds one
          run_len += 1
          #New previous card is the current card
          before_card_value = current_card_value
        #If run length is larger than the other longest run, the new highest run is this one and the first card of the run is indexed using current card index minus the highest run length + 1 as the index starts counting at 0
        if run_len > highest_run_len:
          highest_run_len = run_len
          first_card_value = palette.index(palette[i - highest_run_len + 1])
        #But if not only 1 lower, the run stops and becomes False
        else:
          in_run = False

    #Indexes the original palette from the first card of the largest run to the last card of it by adding the run length to the first card
    palette = palette[first_card_value : first_card_value + highest_run_len]
    return palette

  #If only 1 card in palette, the palette is returned
  else:
    return palette

#Gets most cards below 4
def get_below_4(palette):

  below_4_cards = []

  #Each card in palette is gone through and checks if the value of that card + 4 is at max 8 meaning that hgihest a card can be is 4 (4 + 4 is 8) or lower.
  for p in palette:
    palette_card = get_card_value(p)
    if int(palette_card) + 4 <= 8:
      #Appends card if lower or == to 4
      below_4_cards.append(p)

  #Returns all rule cards list
  return below_4_cards

#Sorts palette using .sort() and reversing it so the order decends in value using the key function that assigns value to each color and just gets the num value of each card. 
def sort_palette(palette):
  palette.sort(reverse = True, key = get_card_value)
  palette.sort(reverse = True, key = card_color_rank)
  #Returned palette decends in order of color highest to lowest then decending number value for each of the colors
  return palette

#Finds winning player using all the lists of each players rule cards. Basically, the list with the longest length will be the winning player as they have more cards meeting the winning rule.
def find_winning_player(list_of_palettes, players):
  current_winner = players[0]
  current_longest_palette = list_of_palettes[0]
  len_current_winning_palette = len(current_longest_palette)
  high_card_of_winner = get_player_highest_card(current_longest_palette)
  
  for x in list_of_palettes:
    palette_len = len(x)

    #If current len of list is larger than current longest list, it replaces the longest list
    if palette_len > len_current_winning_palette:
      current_longest_palette = x
      current_winner = list_of_palettes.index(x)
      len_current_winning_palette = palette_len
      high_card_of_winner = get_player_highest_card(current_longest_palette)

    #But if the lengths are the same, the two highest cards wihtin those lists are comapred and whoever has the highest card in the list that meets the canvas rule will be the winning player
    elif palette_len == len_current_winning_palette:
      high_card_of_winner = highest_card_of_two(high_card_of_winner, get_player_highest_card(x))
      if high_card_of_winner in x:
        current_longest_palette = x
        current_winner = list_of_palettes.index(x)
        len_current_winning_palette = palette_len
        high_card_of_winner = get_player_highest_card(current_longest_palette)

  #Returns the winning player be indexing the current player number from all players list
  return players[current_winner]

#Finds the highest card of two given cards
def highest_card_of_two(card1, card2):
  card1_value = get_card_value(card1)
  card1_color = card_color_rank(card1)
  card2_value = get_card_value(card2)
  card2_color = card_color_rank(card2)

  #Comapres card values first but if they are equal, it goes to color rankings
  if card1_value > card2_value:
    return card1
  elif card2_value > card1_value:
    return card2
  elif card1_value == card2_value:
    if card1_color > card2_color:
      return card1
    else:
      return card2

#Creates a list with no duplicates of same card values. There can be duplicate colors, but for example, no Red7 and Orange7 (same values)
def one_each_num_value(palette):
  list_of_values = []
  list_of_cards = []
  #For each card in palette, checks value of the card then checks if it is NOT in the list of values then appends it if it is not but if it is, thent he next card is checked (loops)
  for p in palette:
    card_value = get_card_value(p)
    if card_value not in list_of_values:
      list_of_values.append(card_value)
      list_of_cards.append(p)
  #Sorts the new palette
  list_of_cards.sort(reverse = True, key = get_card_value)
  return list_of_cards

#This was the prototype of bot turn before the system that checked if it would be winning after turn
"""def bot_turn(input, hand, palette, canvas):

  for i in range(100):
    #Bot adds card to palette
    if input == 1:
      action1_card = hand[random.randint(0, len(hand) - 1)]
      palette = action1(palette, action1_card)
      hand.remove(action1_card)
      print(f"The current bot played the card {action1_card} to their palette!")
      print(" ")
      return True
    #Bot adds card to canvas
    elif input == 2:
      action2_card = hand[random.randint(0, len(hand) - 1)]
      canvas.append(action2_card[:-2])
      hand.remove(action2_card)
      print(f"The current bot played the card {action2_card} to the canvas!")
      print(" ")
      return True
    #Bot adds card to palette then discards card to canvas. Basically just action 1 and 2 in one turn
    elif input == 3:
      action1_card = hand[random.randint(0, len(hand) - 1)]
      palette = action1(palette, action1_card)
      hand.remove(action1_card)
      action2_card = hand[random.randint(0, len(hand) - 1)]
      canvas.append(action2_card[:-2])
      hand.remove(action2_card)
      print(f"The current bot played the card {action1_card} to their palette! Then they added {action2_card} to the canvas!")
      print(" ")
      return True
    #Bot does nothing
    else:
      return True"""

#Prints a given card by checking what it's color is then printing the color and number (whole card) using that card's color in text
def color_text(card):
  card_color = card[:-2]
  if card_color == "Red":
    print(f"\033[0;31m {card}")
  elif card_color == "Orange":
    print(f"\033[0;37m {card}")
  elif card_color == "Yellow":
    print(f"\033[0;33m {card}")
  elif card_color == "Green":
    print(f"\033[0;32m {card}")
  elif card_color == "Blue":
    print(f"\033[0;36m {card}")
  elif card_color == "Indigo":
    print(f"\033[0;34m {card}")
  elif card_color == "Violet":
    print(f"\u001b[35m {card}")

#Same as above but takes the last card in canvas instead
def color_text_canvas(list):
  card = list[-1]
  if card == "Red":
    print(f"\033[0;31m {card}")
  elif card == "Orange":
    print(f"\033[0;37m {card}")
  elif card == "Yellow":
    print(f"\033[0;33m {card}")
  elif card == "Green":
    print(f"\033[0;32m {card}")
  elif card == "Blue":
    print(f"\033[0;36m {card}")
  elif card == "Indigo":
    print(f"\033[0;34m {card}")
  elif card == "Violet":
    print(f"\u001b[35m {card}")

#Prints in matching color text, the rule for the given card color
def canvas_rule_print(list):
  canvas = list[-1]
  
  if canvas == "Red":
    print("\033[0;31m The single highest card.")
  elif canvas == "Orange":
    print("\033[0;37m Most cards of one number.")
  elif canvas == "Yellow":
    print("\033[0;33m Most cards of one color.")
  elif canvas == "Green":
    print("\033[0;32m Most even cards.")
  elif canvas == "Blue":
    print("\033[0;36m Most cards of all different colors.")
  elif canvas == "Indigo":
    print("\033[0;34m Highest amount of cards in a row.")
  else:
    print("\u001b[35m The most cards below 4.")

#This is the system that checks if the bot will be winning after making it's turn. It mimicks the player turn function and then checks the winning player to see if it will be the bot
def bot_move_check_if_winning(hand, palette, canvas, players, winning_card1, winning_card2, bot_move_random, x):

  #Creates a copy of players so that the actual player's list and all palettes hands within it are not affected
  players_copy = deepcopy(players)
  bot_copy = players_copy[players_copy.index(x)]
  bot_hand_copy = bot_copy[0]
  bot_palette_copy = bot_copy[1]
  #Deep copies canvas meaning a whole new set of data instead of a shallow copy
  canvas_copy = deepcopy(canvas)

  #Takes the random card1 and random input value if it is 1 and appends the card1 to the palette copy then removes that card from the bot hand copy
  if bot_move_random == 1:
    bot_palette_copy.append(winning_card1)
    bot_hand_copy.remove(winning_card1)

  #Takes card2 and appends the color only to the canvas copy then removes the card from hand copy
  elif bot_move_random == 2:
    bot_hand_copy.remove(winning_card2)
    canvas_copy.append(winning_card2[:-2])

  #Does both things in one move from above
  else:
    bot_palette_copy.append(winning_card1)
    bot_hand_copy.remove(winning_card1)
    bot_hand_copy.remove(winning_card2)
    canvas_copy.append(winning_card2[:-2])

  #Sorts palette
  sort_palette(bot_palette_copy)
  #Checks who will be the winning player. If it is the bot copy, it returns true so that the next function in main file can do this move for real!
  if check_winning_player(canvas_copy, players_copy) == bot_copy:
    return True
  #Else, if the winning player is not the bot, depending on what move they made, it will revert these cahnges to the copy so that it resets back and the for i in range loop will run again until a winning move is found and the bot will be winning
  elif check_winning_player(canvas_copy, players_copy) != bot_copy and bot_move_random == 1:
    bot_hand_copy.append(winning_card1)
    bot_palette_copy.remove(winning_card1)
  elif check_winning_player(canvas_copy, players_copy) != bot_copy and bot_move_random == 2:
    bot_hand_copy.append(winning_card2)
    #Popping will take the last value of the list (basically just removing the latest added card to it)
    canvas_copy.pop()
  elif check_winning_player(canvas_copy, players_copy) != bot_copy and bot_move_random == 3:
    bot_hand_copy.append(winning_card1)
    bot_palette_copy.remove(winning_card1)
    bot_hand_copy.append(winning_card2)
    canvas_copy.pop()
  
#This comes after the above function to take the cards that made sure the bot would win as well as the move the mimick system used to make this move for real and allow the bot to be winning. 
def make_bot_winning(input, hand, palette, canvas, winning_card1, winning_card2):
  #Bot adds card to palette
  if input == 1:
    palette = action1(palette, winning_card1)
    hand.remove(winning_card1)
    #Tells user in console what the bot played to their palette
    print(f"The current bot played the card {winning_card1} to their palette!")
    print(" ")
    return True
  #Bot adds card to canvas
  elif input == 2:
    canvas.append(winning_card2[:-2])
    hand.remove(winning_card2)
    #Tells user in console what the bot played to the canvas
    print(f"The current bot played the card {winning_card2} to the canvas!")
    print(" ")
    return True
  #Bot adds card to palette then discards card to canvas. Basically just action 1 and 2 in one turn
  elif input == 3:
    palette = action1(palette, winning_card1)
    hand.remove(winning_card1)
    canvas.append(winning_card2[:-2])
    hand.remove(winning_card2)
    print(f"The current bot played the card {winning_card1} to their palette! Then they added {winning_card2} to the canvas!")
    print(" ")

#Prints all canvas color rules by taking a list of all colors and matching them to print that rule in it's color
def all_canvas_rules_print(list_colors):
  for i in list_colors:
    #Red rule
    if i == "Red":
      print("\033[0;31m The single highest card.")
      #Orange rule
    elif i == "Orange":
      print("\033[0;37m Most cards of one number.")
      #Yellow rule
    elif i == "Yellow":
      print("\033[0;33m Most cards of one color.")
      #Green rule
    elif i == "Green":
      print("\033[0;32m Most even cards.")
      #Blue rule
    elif i == "Blue":
      print("\033[0;36m Most cards of all different colors.")
      #Indigo rule
    elif i == "Indigo":
      print("\033[0;34m Highest amount of cards in a row.")
      #Violet rule
    else:
      print("\u001b[35m The most cards below 4.")