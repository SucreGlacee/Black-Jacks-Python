import random as r

# Code de Black Jack codé par SucreGlace_               Discord : SucreGlace_#8758
# Note du développeur : Le code n'est pas optimal mais il marche. Celui ci contient toute les règles du black jack : 6 jeu de cartes, comportement du croupier ectttt. 
# Vous pouvez l'utiliser dans des bots ou vos projets. Il est open source. 
# A rajouter : Gains de jetons : x1 pour une win normal x1.5 pour un blackjack (main de 21)
#              Mise : Sur le black jack dont je me suis inspiré : 5 euros minimum 300 euros max
# gros kiss les reufs

def hands():
    card = []
    r.shuffle(total_cards)
    print("Le paquet est mélangé")
    for i in range(2):
        card_choose = r.choice(total_cards)
        card.append(card_choose)
        total_cards.remove(card_choose)
    return card

def croupier():
    card_croupier = []
    for i in range(2):
        card_choose_croupier = r.choice(total_cards)
        card_croupier.append(card_choose_croupier)
        total_cards.remove(card_choose_croupier)
    return card_croupier

def hit(hand):
    new_card = []
    new_card_choose = r.choice(total_cards)
    new_card.append(new_card_choose)
    total_cards.remove(new_card_choose)
    hand_hit = hand + new_card
    return hand_hit

def pass_(hand_croupier):
    return finisher(hand_croupier)

def finisher(hand_croupier):
    hand_c = hand_croupier.copy()
    while sum(cartes[card] for card in hand_c) < 17:
        new_card_croupier = r.choice(total_cards)
        hand_c.append(new_card_croupier)
        total_cards.remove(new_card_croupier)
    return hand_c

def verif_partie(hand, hand_croupier):
    cartes = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    player_score = sum(cartes[card] for card in hand)
    croupier_score = sum(cartes[card] for card in hand_croupier)
    print(player_score)
    print(croupier_score)
    if player_score > 21:
        print("Bust ! Vous avez perdu !")
    elif croupier_score > 21:
        print("Bust ! Le croupier a perdu ! Vous avez gagné !")
    else:
        if player_score > croupier_score:
            print("Vous avez une main plus élevée que le croupier. Vous avez gagné !")
        elif player_score < croupier_score:
            print("Le croupier a une main plus élevée que vous. Vous avez perdu !")
        else:
            print("Égalité !")

def verif_bust(hand):
    cartes = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    player_score = sum(cartes[card] for card in hand)
    if player_score > 21:
        print("Bust ! Vous avez perdu !")
        return False
    return True

def has_as(hand):
    for card in hand:
        if card == "1":
            return True
    return False

cartes = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
total_cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
total_cards = total_cards*4
total_cards = total_cards*6
hand = hands()
print(hand)
a = sum(cartes[card] for card in hand)
print("Vous avez :", a, "points !")
hand_c = croupier()
print("Le croupier a un", hand_c[0])
while True:
    choice = input("Souhaitez-vous hit ou pass ? (H pour hit, P pour pass)")
    if choice.lower() == "h":
        hand = hit(hand)
        b = sum(cartes[card] for card in hand)
        print("Vous avez maintenant", b, "points !")
        if not verif_bust(hand):
            break
        if has_as(hand) and sum([cartes[card] for card in hand]) + 10 <= 21:
            total_value = sum([cartes[card] for card in hand]) + 10
        else:
            total_value = sum([cartes[card] for card in hand])
    elif choice.lower() == "p":
        hand_croupier = pass_(hand_c)
        verif_partie(hand, hand_croupier)
        break
