# ERROS DE SINTAXE
#pimt("OI") #erro de sintaxe pq esta mal escrito

# EXCEÇAO name error
# EXCEÇAO = Exception
# exceçao é quando a logica de algo nao funciona como um numero que deveria ser so int ou uma variavel q n existe
#print(x) # quando a variavel n existe por exemplo

# EXCEÇAO value error
#n = int(input("Numero: ")) # se n nao for inteiro da o erro value error
#print(n)

# Exceçao ZeroDivisionError
# nao da pra dividir algo por 0
"""
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(f"o resultado é {r}")
"""
from logging import exception

#TRY = tenta
try: # tentar pra ver se da problema
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): # se algo der errado ele, faz o que esta no codigo
    #pode haver varios except para varios tipos de erros
    print(f"Tivemos um problema com os tipos de dados")
except ZeroDivisionError:
    print("nao é possivel dividir por 0 burro")
except KeyboardInterrupt:
    print("O usuario preferiu nao informar os dados")
except Exception as erro:
    print(f"O erro encontrado foi {str(erro)}")
else: # deu certo, ele faz o que esta no codigo (opcional)
    print(f"o resultado é {r}")
finally: # o finally faz o codigo independente se estiver certo ou nao (opcional)
    print("Adeus")

