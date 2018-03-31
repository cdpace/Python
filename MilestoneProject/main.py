import card_pack
import game_service
import player

client = player.Player('test',100)

service = game_service.GameService(client)

service.start()






