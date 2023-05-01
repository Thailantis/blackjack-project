import random

class BlackJack:
    def __init__(self, cards, player, dealer):
        self.cards = cards
        self.player = player
        self.dealer = dealer
        
    def driver(self, player):
        dealer = True
        while dealer is input("Welcome to Blackjack. Please enter your 'name': "):
            if player == 'name':
                print("Welcome! are you ready? type 'yes' to start or 'no' to quit")
                self.driver()
            elif player == 'yes':
                print("Welcome to Blackjack! Let the game begin")
                self.driver()
            elif player == 'no':
                print("Thanks, come again!")
                self.driver()
            else:
                print("The casino is closed due to covid-19.")
                print("The casino is closed due to the fire.")
                print("The casino is closed due to being sold out by the another company.")
                self.driver()
                
    def cards(self):
        cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        red_card_type = ['Hearts', 'Diamonds']
        black_card_type = ['Clubs', 'Spades']
        shuffle_card = random.choice(cards, red_card_type, black_card_type)
        return shuffle_card
      
    def calculate_score(self, cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
      
    def compare(self, player_score, cpu_score):
        if player_score > 21 and cpu_score > 21:
            print("You bust. You lose.")
        if player_score == cpu_score:
            return "Draw"
        elif cpu_score == 0:
            return "You lose, the opponent won"
        elif player_score == 0:
            return "You win. Victory is yours!"
        elif player_score > 21:
            return "You lost dumb dumb cause you went over numb"
        elif cpu_score > 21:
            return "The villain lost. You win! congratulations!"
        elif player_score > cpu_score:
            return "You Win blackjack!"
        else:
            return "You lose"
          
    def play_game(self):
        player_cards = []
        cpu_cards = []
        game_over = False
        for card in range(2):
            player_cards.append(card())
            cpu_cards.append(card())
        while not game_over:
            player_score = self.calculate_score(player_cards)
            computer_score = self.calculate_score(cpu_cards)
            print(f"Your cards: {player_cards}")
            print(f"Your opponet's cards: {cpu_cards}")
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            deal_the_card = input("Would you like to get another card? type 'yes' to get another card or 'no' to pass: ")
        if deal_the_card == "yes":
            player_cards.append(card())
        elif deal_the_card == input("Would you like to add a double?"):
            player_cards.append(card(2))
        else:
            game_over = True
        while computer_score != 0 and computer_score < 17:
            cpu_cards.append(card())
            computer_score = self.calculate_score(cpu_cards)
        print(f" Your final hand: {player_cards}, final score: {player_score}")
        print(f" Computer's final hand: {cpu_cards}, final score: {computer_score}")
        stand = input("Would you like to use stand to not deal anymore?")
        score = self.compare(player_score, computer_score)
        return self.compare(stand, score)
    
test = BlackJack
test.driver('self', 'player')
print(test)
