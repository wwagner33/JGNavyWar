from .player import Player

class Chat:
    """
    Classe que representa o chat do jogo JGNavyWar.

    Atributos:
    - messages: Lista de mensagens no chat.
    """
    def __init__(self):
        self.messages = []

    def send_message(self, player: Player, message: str):
        """
        Envia uma mensagem no chat.

        :param player: Instância da classe Player que está enviando a mensagem.
        :param message: Mensagem a ser enviada.
        """
        self.messages.append(f"{player.username}: {message}")

    def __repr__(self):
        return f"Chat(messages={self.messages})"
