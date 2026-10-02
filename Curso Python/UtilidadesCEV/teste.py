from UtilidadesCEV import Moeda
from UtilidadesCEV import Dado
p = Dado.leiaDinheiro("Digite o preço: R$")
moeda = Moeda.moeda(p)
Moeda.resumo(p, 80, 35)