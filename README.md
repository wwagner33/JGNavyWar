# JG Navy War
Homenagem de seus tios para o João Gabriel CAminha Pequeno, com a certeza que ele se tornará um grande jogador e um excelente programador. :-D 

## Visão Geral do Jogo

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



## Requisitos Funcionais

| ID  | Descrição                                                                                          |
|-----|----------------------------------------------------------------------------------------------------|
| 0   | O nome do jogo deve ser "JGNavyWar" e na sua página inicial deve aparecer um texto de homenagem.   |
| 1   | O jogo deve ter licença GPLv3, um arquivo .gitignore para node e um README.md explicativo.         |
| 2   | O tabuleiro do jogo deve ser uma grid de 20x20.                                                    |
| 3   | Os navios devem ser em número de 5 para cada jogador.                                              |
| 4   | Cada navio deve ocupar uma posição aleatória dentro da sub-grid de 1/4 da área do tabuleiro.       |
| 5   | Navios ocupam diferentes números de células contínuas na grid, compondo uma reta.                  |
| 6   | Cada jogador só pode visualizar sua área de jogo.                                                  |
| 7   | As categorias de navios são: Porta-aviões, Couraçado, Cruzador, Destróier, Fragata, Lancha, Submarino.|
| 8   | Cada navio tem uma quantidade de células correspondente à sua categoria.                           |
| 9   | Cada embarcação corresponde a uma quantidade de scores.                                            |
| 10  | Jogador sabe qual navio foi atingido após acertar todas as células.                                |
| 11  | Pontos computados após destruição completa do navio.                                               |
| 12  | Aviso de acerto ao atingir célula do oponente.                                                     |
| 13  | Movimentos no chat indicados por letras e números.                                                 |
| 14  | Jogador pode atacar um oponente por vez, escolhendo célula.                                         |
| 15  | Ordem de movimentos decidida pelo sistema e seguida até o final da partida.                        |
| 16  | Vence a partida quem destruir cinco embarcações primeiro.                                          |
| 17  | O jogo deve ter um ranking de scores ordenado do maior para o menor.                               |
| 18  | Só participa do ranking quem vence uma partida.                                                    |
| 19  | Partida iniciada com pelo menos 2 jogadores, após 1 minuto de espera ou com 4 jogadores.           |
| 20  | Jogador pode iniciar uma nova partida e esperar que outros se conectem.                            |
| 21  | Jogador pode participar de uma partida existente se houver menos de 4 jogadores.                   |
| 22  | Cadastro de jogador com Nome, email, nome de jogador (máximo 10 caracteres) e senha.               |
| 23  | Autenticação por email e senha para acessar o espaço de jogo.                                      |
| 24  | Timer de 1 minuto para iniciar a partida quando dois jogadores conectarem.                         |
| 25  | Desconexão: navios não destruídos de jogador desconectado removidos.                               |
| 26  | Partida interrompida se restar apenas um jogador.                                                  |
| 27  | Jogador desconectado após 60 minutos de inatividade.                                               |
| 28  | Tela inicial mostra ranking e permite acesso ao jogo.                                              |
| 29  | Chat para jogadores conversarem na tela de Home.                                                   |
| 30  | Informação de status (ocupado) para jogadores em partida.                                          |
| 31  | Botões de logout na tela de Home e na tela de jogo.                                                |
| 32  | Página de instruções sobre o jogo.                                                                 |
| 33  | Token de sessão para autenticação.                                                                 |
| 34  | Jogador pode alterar cadastro e remover conta.                                                     |
| 35  | Rodapé com nomes dos criadores e símbolo de copyleft.                                              |

## Requisitos Não Funcionais

| ID  | Descrição                                                                                       |
|-----|-------------------------------------------------------------------------------------------------|
| 1   | Utilizar websockets ou sockets para comunicação peer-to-peer.                                   |
| 2   | O servidor deve armazenar informações e iniciar o jogo, mas o processamento da partida é feito pelos peers.|
| 3   | Usar PostgreSQL para armazenamento das informações.                                             |
| 4   | Interface web desenvolvida com Flask.                                                           |
| 5   | O sistema deve ser seguro, garantindo que apenas usuários autenticados possam acessar as partidas.|
| 6   | O desempenho do sistema deve permitir partidas fluidas e sem atrasos perceptíveis.              |
| 7   | A interface deve ser intuitiva e responsiva, facilitando a interação do jogador.                |
| 8   | A comunicação entre os jogadores deve ser rápida e confiável.                                   |
| 9   | O sistema deve suportar até 4 jogadores por partida.                                            |
| 10  | O servidor deve estar preparado para escalabilidade, suportando um número crescente de jogadores e partidas.|

### Atores do Sistema

1. **Jogador:**
   - Cadastra-se no sistema.
   - Faz login e autentica-se.
   - Participa de partidas.
   - Inicia novas partidas.
   - Realiza movimentos e ataques.
   - Interage com outros jogadores via chat.
   - Consulta ranking e seu status de jogo.
   - Visualiza e gerencia suas informações de cadastro.
   - Realiza logout.

2. **Servidor:**
   - Armazena informações dos jogadores e partidas.
   - Inicia partidas e gerencia autenticação.
   - Armazena e mantém o ranking.
   - Garante segurança e integridade dos dados.

3. **Peer (Jogador em Partida):**
   - Processa a lógica da partida.
   - Comunica-se com outros jogadores na mesma partida.
   - Atualiza status da partida e informa ao servidor.
