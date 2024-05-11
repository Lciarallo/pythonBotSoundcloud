#language: pt
Funcionalidade: Eu como usuario Baixar musicas do soundclound
    '''
    Eu como usuario quero abrir o soundclound
    fazer uma consulta do nome da música que eu quero
    fazer download da música em arquivo .mp3.
    '''
    Cenario: Baixar música do soundclound
     Dado acesso a pagina inicial do soundcloud
     Quando realizar a busca do nome da musica
     Quando clicar na primeira música
     Quando obter a URL da música
     Entao devo baixar o a musica em formato .mp3

