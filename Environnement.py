"""
Environnement Splendor en python

"""
import random as rd

class Card:
    def __init__(self, id, price, color, stars, points):
        self.id = id
        self.price = price                                                  # price is a list, [BLACK, BLUE, GREEN, RED, WHITE] 
        self.color = color                                                  # color is an integer representing the color in this order : [BLACK, BLUE, GREEN, RED, WHITE] 
        self.stars = stars                                                  
        self.points = points
        self.bought = 0                                                     # bought is a number representing the id of the player who bought the card (0 if not bought)
        self.reserved = 0                                                   # same as bought but with reservation
    
    def buyable(self, player):
        if self.id == 0:
            print("Erreur: La carte n'est pas sur le plateau")
            return False
        if self.bought != 0 or (self.reserved != player.id and self.reserved != 0):
            print("Erreur: La carte est déjà achetée ou réservée")
            return False
        else:
            if self.price[0] > player.chips[0] + player.card_chips[0] + player.chips[5] or self.price[1] > player.chips[1] + player.card_chips[1] + player.chips[5] or self.price[2] > player.chips[2] + player.card_chips[2] + player.chips[5] or self.price[3] > player.chips[3] + player.card_chips[3] + player.chips[5] or self.price[4] > player.chips[4] + player.card_chips[4] + player.chips[5]:
                print("Erreur: Vous n'avez pas assez de jetons pour pouvoir acheter cette carte")
                return False
            elif self.price[0] <= player.chips[0] + player.card_chips[0] and self.price[1] <= player.chips[1] + player.card_chips[1] and self.price[2] <= player.chips[2] + player.card_chips[2] and self.price[3] <= player.chips[3] + player.card_chips[3] and self.price[4] <= player.chips[4] + player.card_chips[4]:
                return True
            else:
                sum == 0
                for i in range(0,5):
                    sum += max[self.price[i] - player.chips[i],0]
                if sum <= player.chips[5]:
                    return True
                else:
                    print("Erreur: Vous n'avez pas assez de jetons pour pouvoir acheter cette carte")
                    return False



    def generate_card_rd(self, id):
        stars = rd.randint(1,3)
        if stars == 1:
            points = rd.randint(0,1)
            prices = [[1,1,1,1,0], [0,1,1,1,1], [1,0,1,1,1], [1,1,0,1,1], [1,1,1,0,1], [0,0,2,2,0], [0,2,2,0,0], [0,0,0,2,2], [2,0,0,0,2], [2,2,0,0,0]]
            price = prices[rd.randint(0,4)]
            color = rd.randint(0,4)
        if stars == 2:
            points = rd.randint(1,3)
            prices = [[0,0,0,0,5], [5,0,0,0,0], [0,5,0,0,0], [0,0,5,0,0], [0,0,0,5,0], [2,1,4,0,0], [0,2,1,4,0], [0,0,2,1,4],[4,0,0,2,1], [1,4,0,0,2], [3,3,2,0,0], [0,3,3,2,0], [0,0,3,3,2], [2,0,0,3,3], [3,2,0,0,3]]
            price = prices[rd.randint(0,11)]
            color = rd.randint(0,4)
        if stars == 3:
            points = rd.randint(3,5)
            prices = [[7,0,0,0,0], [0,7,0,0,0], [0,0,7,0,0], [0,0,0,7,0],[0,0,0,0,7], [4,6,3,0,0], [0,4,6,3,0], [0,0,4,6,3], [3,0,0,4,6], [6,3,0,0,4], [0,7,3,0,0], [0,0,7,3,0], [0,0,0,7,3],[3,0,0,0,7], [3,3,3,5,0], [0,5,3,3,3], [3,0,5,3,3], [3,3,0,5,3],[3,3,3,0,5]]
            price = prices[rd.randint(0,15)]
            color = rd.randint(0,4)
        new_card = Card(id, price, color, stars, points)
        return new_card

class Deck:
    def __init__(self, star, star2, star3):               # star is the list of the id of the one star cards in the deck | star2 is for the 2 stars cards | star3 for 3 stars cards
        self.star = star
        self.star2 = star2
        self.star3 = star3
    
    def update(self, card, turned):
        if card.bought != 0 or card.reserved != 0:
            if card.stars == 1:
                for i in self.star:
                    if i == card.id:
                        i = turned.star[0]
                        turned.star.pop(0)
            if card.stars == 2:
                for i in self.star2:
                    if i == card.id:
                        i = turned.star2[0]
                        turned.star2.pop(0)
            if card.stars == 3:
                for i in self.star3:
                    if i == card.id:
                        i = turned.star3[0]
                        turned.star3.pop(0)               
            return True
        print("Erreur: La carte ",card.id," n'a pas été achetée, inutile de repiocher dans le deck")
        return False
    
    def generate_deck(self, nbcards):                    # nbcards is the number of cards in the deck    
        cards = []
        for i in range(0,nbcards):
            card = Card(0, [], 0, 0, 0)
            rd_card = card.generate_card_rd(i)
            cards.append(rd_card)
            if rd_card.stars == 1:
                self.star.append(rd_card.id)
            elif rd_card.stars == 2:
                self.star2.append(rd_card.id)
            else:
                self.star3.append(rd_card.id)
        new_deck = Deck(self.star, self.star2, self.star3)
        return new_deck, cards

class Chips:
    def __init__(self, color):
        self.color = color

class Player:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.points = 0
        self.chips = [0,0,0,0,0,0]
        self.card_chips = [0,0,0,0,0]
        self.reserve = 0

    def reservable(self, card):
        if card.id == 0:
            print("Carte pas sur le plateau ou n'existe pas")
            return False
        if self.reserve < 3 and card.reserved == 0 and card.bought == 0:
            return True
        else:
            print("Erreur: Vous avez soit déjà plus de 3 cartes réservées soit la carte que vous voulez réserver est déjà achetée")
            return False

    def buy_card(self, card, visible, deck):             # visible is a list containing the id of the cards that are possible to buy, deck is the list of the id of the cards that will be used to replace the visible cards that have been bought/reserved
        if card.buyable(self):
            self.points += card.points
            self.card_chips[card.color] += 1
            card.bought = self.id
            for i in range(0,5):
                chips_needed = card.price[i] - self.card_chips[i]
                joker_needed = min([chips_needed - self.chips[i], 0])
                self.chips[i] -= min(self.chips[i], chips_needed)
                self.chips[5] -= joker_needed[i]
                visible.update(card, deck)
                print("La carte", card.id, " a bien été achetée par le joueur", self.id)
            return True
        else :
            print("Erreur: La carte", card.id, " n'est pas achetable par le joueur", self.id)
            return False
        
    def reserve_card(self, card, visible, deck):         # visible is a list containing the id of the cards that are possible to buy, deck is the list of the id of the cards that will be used to replace the visible cards that have been bought/reserved
        if self.reservable(card):
            self.chips[5] += 1
            card.reserved = self.id
            self.reserve += 1
            visible.update(card, deck)
            return True
        else:
            print("Erreur: La carte", card.id, " n'est pas réservable par le joueur", self.id)
            return False
        

    def receive_square_card(self, square_card):
        if self.card_chips[0] >= square_card.price[0] and self.card_chips[1] >= square_card.price[1] and self.card_chips[2] >= square_card.price[2] and self.card_chips[3] >= square_card.price[3] and self.card_chips[4] >= square_card.price[4]:
            self.points += square_card.points
            print("Le joueur", self.id, "reçoit le carton", square_card.id)
            return True
        else:
            print("Le carton",square_card.id," n'est pas recevable pour le joueur", self.id)
            return False
        
    def pick_2_same_chips(self, bank, color):              # color is an integer associated to the color the player wants to pick, in this order: [BLACK, BLUE, GREEN, RED, WHITE]
        if color < 5 and color >= 0:
            tot_chips = 0
            for i in self.chips:
                tot_chips += i
            if bank.nBchips[color] > 4 and tot_chips <= 8:
                bank.nBchips[color] -= 2
                self.chips[color] += 2
                print("Le joueur", self.id, "a bien reçu ses 2 jetons de couleur", color)
                return True
            else:
                print("Erreur: Vous avez soit plus de 8 jetons en main, soit la couleur demandée n'a pas assez de jetons")
                return False
        else:
            print("Erreur: La couleur demandée n'existe pas (color < 5 et positif)")
            return False
    
    def pick_3chips(self, bank, color1, color2, color3):            # same, color1,2,3 are integers representing the colors the player wants to pick
            tot_chips = 0
            for i in self.chips:
                tot_chips += i
            if tot_chips <= 7:
                if color1 != color2 and color1 != color3 and color2 != color3 and color1 < 5 and color2 < 5 and color3 < 5 and color1 >= 0 and color2 >= 0 and color3 >= 0:
                    bank.nBchips[color1] -= 1
                    bank.nBchips[color2] -= 1
                    bank.nBchips[color3] -= 1
                    self.chips[color1] += 1
                    self.chips[color2] += 1
                    self.chips[color3] += 1
                    return True
                else:
                    print("Erreur: vous avez soit demandé des jetons de la même couleur, soit la couleur demandée n'existe pas (color < 5 et positif)")
                    return False
            elif tot_chips == 8:
                if color1 != color2 and color1 < 5 and color2 < 5 and color1 >= 0 and color2 >= 0:
                    bank.nBchips[color1] -= 1
                    bank.nBchips[color2] -= 1
                    self.chips[color1] += 1
                    self.chips[color2] += 1
                    return True
                else:
                    print("Erreur: vous avez soit demandé des jetons de la même couleur, soit la couleur demandée n'existe pas (color < 5 et positif)")
                    return False
            elif tot_chips == 9:
                if color1 < 5 and color1 >= 0:
                    bank.nBchips[color1] -= 1
                    self.chips[color1] += 1
                    return True
                else:
                    print("Erreur: la couleur demandée n'existe pas (color < 5 et positif)")
                    return False
            else:
                print("Erreur: Vous avez déjà 10 jetons.")
                return False
        
class Bank:
    def __init__(self, nBjoueurs):
        if nBjoueurs == 2:
            self.nBchips = [4,4,4,4,5]                              # nBchips is a list of the numbers of chips, each number is linked to a color [BLACK, BLUE, GREEN, RED, WHITE] 
        if nBjoueurs == 3:
            self.nBchips = [5,5,5,5,5]
        else :
            self.nBchips = [7,7,7,7,5]

                             
class Game:
    def __init__(self, players, deck, bank, square_cards):
        self.players = players
        self.deck = deck
        self.bank = bank
        self.square_cards = square_cards
        



    def end_game(self):
        for player in self.players:
            if player.points >= 15:
                return player.id
            else:
                return 0
            
    def play(self):
        cards = self.deck.generate_deck(120)[1]
        visible = Deck(self.deck.star[:4], self.deck.star2[:4], self.deck.star3[:4])
        del self.deck.star[:3]
        del self.deck.star2[:3]
        del self.deck.star3[:3]
        tour = 0
        while self.end_game() == 0 or tour % len(self.players) != 0:
            for player in self.players:
                while (player.id - tour) % len(self.players) != 0:
                    print("Joueur: ", player.id,"à toi de jouer")
                    print("1. Piocher 3 jetons")
                    print("2. Piocher 2 jetons de la même couleur")
                    print("3. Réserver une carte")
                    print("4. Acheter une carte")
                    print("5. Afficher les cartes achetables/réservables")
                    choice = int(input("Entrez le numéro de votre choix : "))
                    if choice == 1:
                        tot_chips = 0
                        for chips in player.chips:
                            tot_chips += chips
                        if tot_chips < 8:
                            print("Choisissez 3 couleurs différentes")
                            print("0 = noir, 1 = bleu, 2 = vert, 3 = rouge, 4 = blanc")
                            choice_color1 = int(input("Entrez le  numéro correspondant à la première couleur: "))
                            choice_color2 = int(input("Entrez le  numéro correspondant à la deuxième couleur: "))
                            choice_color3 = int(input("Entrez le  numéro correspondant à la troisième couleur: "))
                            if player.pick_3chips(self.bank, choice_color1, choice_color2, choice_color3):
                                tour += 1
                        elif tot_chips == 8:
                            print("Vous avez déjà 8 jetons: choisissez 2 couleurs différentes ou revenez au menu principal")
                            print("0 = noir, 1 = bleu, 2 = vert, 3 = rouge, 4 = blanc, 5 = menu principal")
                            choice_color1 = int(input("Entrez le  numéro correspondant à votre choix: "))
                            if choice_color1 == 5:
                                break
                            choice_color2 = int(input("Entrez le  numéro correspondant à la deuxième couleur: "))
                            if player.pick_3chips(self.bank, choice_color1, choice_color2, 0):
                                tour += 1
                        elif tot_chips == 9:
                            print("Vous avez déjà 9 jetons: choisissez 1 couleur ou revenez au menu principal")
                            print("0 = noir, 1 = bleu, 2 = vert, 3 = rouge, 4 = blanc, 5 = menu principal")
                            choice_color1 = int(input("Entrez le  numéro correspondant à votre choix: "))
                            if choice_color1 == 5:
                                break
                            else:
                                if player.pick_3chips(self.bank, choice_color1, 0, 0):
                                    tour += 1
                    if choice == 2:
                        print("Choisissez 1 couleur:")
                        print("0 = noir, 1 = bleu, 2 = vert, 3 = rouge, 4 = blanc")
                        choice_color = int(input("Entrez le  numéro correspondant à la couleur: "))
                        if player.pick_2_same_chips(self.bank, choice_color):
                            tour += 1
                    if choice == 3:
                        id_to_reserve = int(input("Entrez l'id de la carte que vous voulez réserver: "))
                        card_to_reserve = Card(0,[],0,0,0)
                        for card in cards:
                            if card.id == id_to_reserve and card.id in (visible.star or visible.star2 or visible.star3):
                                card_to_reserve = card
                        if player.reserve_card(card_to_reserve, visible, self.deck):
                            tour += 1
                    if choice == 4:
                        id_to_buy = int(input("Entrez l'id de la carte que vous voulez acheter: "))
                        card_to_buy = 0
                        for card in cards:
                            if card.id == id_to_buy and card.id in (visible.star or visible.star2 or visible.star3):
                                card_to_buy = card
                        if player.buy_card(card_to_buy, visible, self.deck):
                            tour += 1
                    if choice == 5:
                        for visible_id in visible.star:
                            for card_to_print in cards:
                                if card_to_print.id == visible_id:
                                    print("Carte:", card_to_print.id)
                                    print("Points:", card_to_print.points)
                                    print("Couleur:", card_to_print.color)
                                    print("Prix:", card_to_print.price[0], "noir", card_to_print.price[1], "bleus", card_to_print.price[2], "verts", card_to_print.price[3], "rouges", card_to_print.price[4], "blancs")
                        for visible_id in visible.star2:
                            for card_to_print in cards:
                                if card_to_print.id == visible_id:
                                    print("Carte:", card_to_print.id)
                                    print("Points:", card_to_print.points)
                                    print("Couleur:", card_to_print.color)
                                    print("Prix:", card_to_print.price[0], "noir", card_to_print.price[1], "bleus", card_to_print.price[2], "verts", card_to_print.price[3], "rouges", card_to_print.price[4], "blancs")
                        for visible_id in visible.star3:
                            for card_to_print in cards:
                                if card_to_print.id == visible_id:
                                    print("Carte:", card_to_print.id)
                                    print("Points:", card_to_print.points)
                                    print("Couleur:", card_to_print.color)
                                    print("Prix:", card_to_print.price[0], "noir", card_to_print.price[1], "bleus", card_to_print.price[2], "verts", card_to_print.price[3], "rouges", card_to_print.price[4], "blancs")
                print(tour)
                #print("Le joueur ",player.id,"a ", player.points,"points, ", player.chips[0]+player.card_chips[0], "jetons noirs, ", player.chips[1]+player.card_chips[1], "jetons bleus, ", player.chips[2]+player.card_chips[2], "jetons verts, ", player.chips[3]+player.card_chips[3], "jetons rouges, ", player.chips[4]+player.card_chips[4], "jetons blancs et", player.chips[5], "jetons joker")
                for square_card in self.square_cards:
                    player.receive_square_card(square_card)
        exaequo = []
        last_exaequo = []
        nbpoints = 14
        winner = -1
        for player in self.players:
            if player.points > nbpoints:
                nbpoints = player.points
                winner = player.id
                exaequo = [player]
            elif player.points == nbpoints:
                exaequo.append(player)
        if len(exaequo) > 1:
            nbcards = 0
            winner = -1
            for player in exaequo:
                tot_cards = 0
                for i in player.card_chips:
                    tot_cards += i
                if tot_cards > nbcards:
                    nbcards = tot_cards
                    winner = player.id
                    last_exaequo = [player]
                if tot_cards == nbcards:
                    last_exaequo.append(player)
        if len(last_exaequo) > 1:
            print("Félicitations aux vainqueurs exaequo:")
            for player in last_exaequo:
                print(player.id)
        else:
            print("Le vainqueur est le joueur:", winner)

class Square_card:

    def __init__(self, id, price, points):
        self.id = id
        self.price = price
        self.points = points

    def generate_square_card_rd(self,id):
        prices = [[3,3,3,0,0], [0,3,3,3,0], [0,0,3,3,3], [3,0,0,3,3],[3,3,0,0,3], [4,4,0,0,0], [0,4,4,0,0], [0,0,4,4,0], [0,0,0,4,4],[4,0,0,0,4]]
        price = prices[rd.randint(0,7)]
        self.id = id
        self.price = price
        self.points = 3
        return self



"""
Tests scenarios
"""

"""Players"""
Alizee = Player(1, "Alizee")
Pierre = Player(2, "Pierre")

"""Deck"""
deck = Deck([],[],[])

"""Square cards"""

square_card1 = Square_card(0,[],0)
square_card2 = Square_card(0,[],0)
square_card3 = Square_card(0,[],0)
square_cards = [
square_card1.generate_square_card_rd(1),
square_card2.generate_square_card_rd(2),
square_card3.generate_square_card_rd(3),
]

"""Bank"""
bank = Bank(2)

"""Game"""
game = Game([Alizee, Pierre], deck, bank, square_cards)
game.play()


