import unittest
from catalogoJogos import CatalogoJogos

class TestCatalogoJogos(unittest.TestCase):

  def test_adicionar_jogo(self):
    catalogoJogos = CatalogoJogos()
    catalogoJogos.add("Pac Man")
    self.assertTrue("Pac Man" in catalogoJogos.jogos)

  def test_contains_retorna_true_quando_contem_jogo(self):
    catalogoJogos = CatalogoJogos()
    catalogoJogos.add("Pac Man")
    self.assertTrue(catalogoJogos.contains("Pac Man"))

  def test_contains_retorna_false_quando_nao_contem_jogo(self):
    catalogoJogos = CatalogoJogos()
    self.assertFalse(catalogoJogos.contains("Pac Man"))