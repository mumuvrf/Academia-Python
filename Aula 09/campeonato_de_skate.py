def limpa_texto(texto):
    pontuacoes = set(['!', '?', ',', ';', '.', ':', ')', '}', ']', '(', '[', '{'])
    texto_limpo = ''

    for caractere in texto:
        if caractere not in pontuacoes:
            texto_limpo += caractere
        
    return texto_limpo

def pontos_no_skate(manobras, performances):
    manobras_format = {}
    for manobra in manobras.keys():
        manobras_format[manobra.lower()] = manobras[manobra]

    atletas = {}
    for atleta in performances:
        atletas[atleta] = {
            'qtde manobras': 0,
            'total pontos': 0
        }
        for frase in performances[atleta]['frases']:
            palavras = limpa_texto(frase).split()
            for palavra in palavras:
                if palavra.lower() in manobras_format:
                    pontos, unidade = manobras_format[palavra.lower()].split()
                    atletas[atleta]['qtde manobras'] += 1
                    atletas[atleta]['total pontos'] += int(pontos)

    return atletas

manobras = {
    'ollie': '1 ponto',
    'nollie': '01 ponto',
    'Heelflip': '02 pontos',
    'Varialflip': '3 pontos',
    'casperflip': '003 pontos',
    'Impossible': '6 pontos'
}
performance = {
    'Tony Hawk': {
    'narrador': 'galvão bueno',
    'frases': [
      'Bem amigos da rrrrede globo',
      'vem aí Tony Hawk',
      'Ele manda um Ollie, agora um Nollie,',
      'haaaaja coração,'
      'vai com tuUuUUuudo Tony Hawk'
    ]
  },
  'Fadinha': {
    'narrador': 'Karen Jonz',
    'frases': [
      'vem logo de Varialflip',
      'um Casperflip, outro varialflip',
      'olha aí, mandou um Impossible.',
      'Mano, ficou parecendo',
      'um peixe morto ali de propósito',
      'pra matar todo mundo do coração',
      'aí depois, era pegadinha'
    ]
  },
  'Guilherme da Academia': {
    'narrador': 'jô soares',
    'frases': [
      'Hoje a noite teremos uma performance',
      'de um skatista muito especial'
      'o Guilherme da Academia.',
      'Lá vem ele... xiii... caiu!!!',
      'skate não é a especialidade dele.',
      'Bira, o que você achou disso?'
    ]
  }
}
print(pontos_no_skate(manobras, performance))