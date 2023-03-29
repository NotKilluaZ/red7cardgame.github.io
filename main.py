from cardgame_functions import *
import random

#Main game function will be called if user wants to restart
def main_game_function():

  #Builds new deck in deck var in order like taking it out of the box
  deck = build_deck()

  #Intro to game
  print("Welcome back to the Diamond Casino! At this table you will be playing Red 7!")
  print(" ")
  print("Before we start, if you do not know how to play Red 7, press x to read over the rules of the game, and to continue, press c: ")
  print(" ")
  #Allows user to read over the rules
  red7_rules("(x to see the rules, c to continue) ")
  print(" ")
  
  print("To begin, the dealer has already opened a new deck of cards, and it's up to you how many times you wish to shuffle it! Press s to shuffle that deck as many times as you want and c to continue with the game: ")
  #Allows user to shuffle deck as much as they want
  user_shuffle("(s to shuffle, c to continue)", deck)
  print(" ")

  #User picks a number between 1 and 3
  num_players = check_int("Next, input how many opponents you want to face off against (up to a maximum of 3): ", 1, 3)
  print(" ")

  #Deals cards to the player and how ever many bots they chose. Deals them each 5??? cards I believe to their hand then one card to each palette then returns a list of all players which is a longer list of lists with their hand palette and "tag".
  players = deal_cards(deck, 7, num_players)

  #Finds lowest card of all players and makes them the starting player since the winning player with the highest card should never be starting
  starting_player = lowest_card_palette(players)
  #Rearranges order of players so that the lowest card player starts by removing them from their current index spot then inserting them in the zero position (first spot)
  players.remove(starting_player)
  players.insert(0, starting_player)

  #Canvas always starts as Red at start of the game but is a list as the canvas will be added and removed from throughout the game
  canvas = ["Red"]

  #As long as there are more than one player int he game (Enough people to go against) the game will keep looping through each players turn until only one player stands or another condition such as no more cards in a players hand is met in which the game will then end.
  while len(players) > 1:

    #Goes through each player in list of players to let them have their turn
    for x in players:

      #Print some information such as all the players palettes, the canvas, and their hand --> Information that they may want when deciding what move to take
      print("\033[0m The canvas is currently:")
      color_text_canvas(canvas)
      canvas_rule_print(canvas)
      #These ANSI codes allow text of cards to match their colors. The functions above match the color text int he string to match the actual code of colored text that it will print that card with.
      print("\033[0m ")
      print("Here are all of the player's palettes:")
      print(" ")

      #Prints all palettes, canvas, and that rule it matches with.
      for p in players:
        display_palette = get_palette(p)
        if p[2] == "player":
          print("Your palette is:")
          for i in display_palette:
            color_text(i)
          print("\033[0m ")
        else:
          print("One of the bot's palettes is:")
          for i in display_palette:
            color_text(i)
          print("\033[0m ")

      #For each player, palette will be that current player's buy calling the function that indexes their palette from their list of hand palette and tag.
      palette = get_palette(x)
      #Sorts palette so that it looks better and is required for later functions that rely on the decedning order of the palette
      sort_palette(palette)

      #Gets hand of current player and sorts it from color first then by number decending with each color
      hand = sort_palette(get_hand(x))

      #Finds winning player that mathces the canvas rule before each turn
      winning_player = check_winning_player(canvas, players)

      #Checks of winning player before turn is the real person and if so it will tell them but of not it will say that they are not winning
      if winning_player[2] == "player":
        print("Wow, it appears you are currently the winning player!")
        print(" ")
      else:
        print("Looks like the current winning player is one of the bots!")
        print(" ")

      #If the tag of the current player is "player" (AKA the real person/human) then this will run as they need more front end interface to interact with on their turn.
      if x[2] == "player":
        #Checks if their hand has any cards in it as if it does not, they cannot play any cards and will be forced to lose.
        if len(hand) == 0:
          #Asks if they want to play again and runs if statement if the returned value is True vs False. Then based on the boolean either the main game function is called again to restart or it quit().
          if play_again("Looks like you don't have anymore cards in your hand to continue playing!"):
            main_game_function()
          else:
            #Quits if they do not want to play again
            quit()

        #Else if they do have mroe than 0 cards in hand, they will go through with their turn
        else:
          #Tells them what they can do and gives them information on what cards they have and where
          print("Now, it's your turn to make a move! You can either play a card from your hand into your palette, discard a card from your hand into the canvas to change the rules of the game to the color of that card, play a card into your palette and then a card into the canvas pile, or do nothing. If you do nothing, you automatically forfeit the game!")
          print(" ")
          print("\033[0m This is your hand right now:")
          for i in hand:
            color_text(i)
          print(" ")
          print("\033[0m This is your palette right now:")
          for i in palette:
            color_text(i)
          print(" ")
          print("\033[0m And lastly, this is the canvas currently:")
          color_text_canvas(canvas)
          print("\033[0m The winning rule is:")
          canvas_rule_print(canvas)
          print("\033[0m ")
          #Shows all canvas rules helpful for choosing what color to add to canvas
          print("Here are all of the different canvas rules:")
          all_canvas_rules = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
          all_canvas_rules_print(all_canvas_rules)
          print("\033[0m ")

          not_enough_cards = True
          while not_enough_cards:
            #Makes sure they input a valid input to make a valid turn
            player_input = check_int("To play a card to your palette press 1, to discard a card to the canvas press 2, to play a card to your palette and then a card to the canvas press 3, and lastly, to do nothing press 4: ", 1, 4)
            print(" ")

            #If the person only has one card left in hand but they want to play a card to canvas and their palette, this will prevent them from being trapped in an unescapable loop since they will not be able to play a second card.
            if player_input == 3 and len(hand) == 1:
              print("Sorry, you don't have enough cards to do that! You can only do actions 1, 2, or 4.")
            else:
              not_enough_cards = False

          #Main player function that allows them to make their move and will modify the canvas, palette, and hand accordingly
          player_turn(player_input, hand, palette, canvas)

        #Sorts palette in case it was modified in the turn before finding the new winner
        sort_palette(palette)
        #Finds new winning player after turn (It better be the current player)
        winning_player_after_turn = check_winning_player(canvas, players)

        #If winning player is the current player, the game continues
        if winning_player_after_turn[2] == "player":
          print("Good, looks like you're winning after your turn!")
          print(" ")
        #Else, they lose as they must be winning after their turn
        elif winning_player_after_turn != x:
          if play_again("Looks like you aren't winning after your turn! You lose."):
            main_game_function()
          else:
            quit()

      #This is the bot turn as if the tag of x is not player it must be a bot
      else:
        #Same as player, checks if their hand has a card to play
        if len(hand) == 0:
          if play_again("Looks like the bot doesn't have anymore cards in their hand to continue playing!"):
            print(" ")
          else:
            quit()

        #Turns runs as supposed to be if the bot has more than 0 cards
        else:
          #Will run 100 times until condition met breaks from this loop
          for i in range(100):
            #If only 1 card in hand, they can only do moves 1 or 2 so the number generated will be reduced to 1 or 2
            if len(hand) == 1:
              random_input = random.randint(1, 2)
            #Else they can generate a number including action 3
            else:
              #Generates random int from 1 and 3 both included using random module
              random_input = random.randint(1, 3)
            #Checks if the two random cards chosen for the bot turn are the same and if they are, this will keep running until they are different cards
            two_same_card = True
            while two_same_card:
              #Generates a random card from their hand using index number from 0 (first card)
              winning_card1 = hand[random.randint(0, len(hand) - 1)]
              winning_card2 = hand[random.randint(0, len(hand) - 1)]
              if winning_card1 != winning_card2:
                two_same_card = False

            #Will take the two generated cards and run them through this function to see if these cards and move is actually played, if they will be winnnig after their turn. This for i in range will keep running to ensure most of the time, the bot will make a move that will allow the game to keep going.
            if bot_move_check_if_winning(hand, palette, canvas, players, winning_card1, winning_card2, random_input, x):

              #Once a winning move is found, this will actually apply it to the bots real hand canvas and palette
              make_bot_winning(random_input, hand, palette, canvas, winning_card1, winning_card2)

              #Breaks out of for i in range 
              break

        #Sorts palette
        palette = sort_palette(palette)
        #Checks if new winning player is bot which it will be most times
        winning_player_after_turn = check_winning_player(canvas, players)

        #Prints whether the bot is winning after their turn and if not it will say so then remove them from the list of players which is basically disqualifying them.
        if winning_player_after_turn == x:
          print("It appears the bot is winning after it's turn... The game will continue.")
          print(" ")
        else:
          print("Looks like the bot was not winning after it's turn! They are now out of the game.")
          print(" ")
          players.remove(x)

  #Once there is only one player left standing, it will always be the real player if this if statement is reached so it will congradulate them then ask if they want to play again.
  if len(players) == 1:
    print("Congratulations! You are the last player standing and win Red 7!")

    #If user wants to play again, the main while True will run again and restart but if not, it breaks and the code ends
    if play_again("You are the winner!"):
      main_game_function()
    else:
      quit()



#Auto starts game by calling the entire game above
main_game_function()