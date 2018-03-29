import card_pack

pack = card_pack.CardPack()

for card in pack.get_all_cards():
    print(card)


print(len(pack.get_all_cards()))