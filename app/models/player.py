class Player:
    """
    Classe que representa um jogador no jogo JGNavyWar.

    Atributos:
    - id: Identificador único do jogador.
    - name: Nome do jogador.
    - email: Email do jogador.
    - username: Nome de usuário do jogador.
    - password: Senha do jogador.
    - score: Pontuação do jogador.
    """
    def __init__(self, id: int, name: str, email: str, username: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.score = 0

    def update_score(self, points: int):
        """
        Atualiza a pontuação do jogador.

        :param points: Pontos a serem adicionados à pontuação do jogador.
        """
        self.score += points
