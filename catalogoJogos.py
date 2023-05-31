class CatalogoJogos:
  
  def __init__(self):
    self.jogos = []

  def add(self, jogo):
    self.jogos.append(jogo)

  def contains(self, jogo):
    return jogo in self.jogos