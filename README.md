1. **Informações Gerais:**
   - Nome do jogo: JGNavyWar.
   - Homenagem a João Gabriel Caminha Pequeno.
   - Licença GPLv3.
   - Autores: Wellington Sarmento e Patrícia de Sousa

2. **Tabuleiro:**
   - Grid de 20x20 (colunas identificadas por letras, linhas por números).

3. **Navios:**
   - 5 navios por jogador.
   - Posição aleatória dentro de uma sub-grid de 1/4 da área do tabuleiro.
   - Navios ocupam células contínuas compondo uma reta.
   - Categorias e células ocupadas: 
     - Porta-aviões: 8 células.
     - Couraçado: 7 células.
     - Cruzador: 6 células.
     - Destróier: 5 células.
     - Fragata: 4 células.
     - Submarino: 4 células.
     - Lancha: 2 células.

4. **Visualização:**
   - Cada jogador só pode visualizar sua área de jogo.

5. **Pontuação:**
   - Cada embarcação corresponde a uma quantidade de scores:
     - Porta-aviões: 100.
     - Couraçado: 70.
     - Cruzador: 60.
     - Destróier: 50.
     - Fragata: 40.
     - Submarino: 80.
     - Lancha: 20.
   - Pontos computados após destruição completa do navio.

6. **Regras de Ataque:**
   - Jogador sabe qual navio foi atingido após acertar todas as células.
   - Aviso de acerto ao atingir célula do oponente.
   - Movimentos no chat indicados por letras e números (e.g., C1 - Alvo destruído).
   - Um jogador ataca um oponente por vez, escolhendo célula (e.g., jogador1(c2)).
   - Ordem de movimentos decidida pelo sistema e seguida até o final da partida.

7. **Informações de Jogo:**
   - Áreas indicativas de navios destruídos (e.g., 1. Fragata (C1, D1, E1, F1)).
   - Tempo máximo de 1 minuto para realizar lance.
   - Ranking de scores dos jogadores, apenas para vencedores de partidas.

8. **Partida:**
   - Iniciada com pelo menos 2 jogadores, após 1 minuto de espera ou com 4 jogadores.
   - Desconexão: Navios não destruídos de jogador desconectado removidos.
   - Partida interrompida se restar apenas um jogador.
   - Jogador pode iniciar ou participar de uma partida visível na tela inicial.

9. **Cadastro e Autenticação:**
   - Nome, email, nome de jogador (máximo 10 caracteres) e senha.
   - Acesso ao espaço de jogo com autenticação por email e senha.

10. **Interface e Funcionalidades:**
    - Tela inicial mostra ranking e permite acesso ao jogo.
    - Chat para jogadores conversarem na tela de Home.
    - Informação de status (ocupado) para jogadores em partida.
    - Botões de logout na tela de Home e na tela de jogo.
    - Página de instruções sobre o jogo.
    - Token de sessão para autenticação.
    - Desconexão após 60 minutos de inatividade.
    - Possibilidade de alterar cadastro e remover conta.
    - Rodapé com nomes dos criadores e símbolo de copyleft.

A partir desses requisitos, vamos estruturar a lógica do jogo. Podemos começar pela criação das classes e métodos necessários para gerenciar o tabuleiro, os navios, e as interações entre jogadores. O que acha?
