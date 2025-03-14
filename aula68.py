"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""

x = 1

def scope():
  x = 10
  def other_function():
    x = 11
    y = 2
    print(x, y) # Aqui x é 11 e y é 2, pois este escopo está acima do global_x
    def global_x():
      global x
      x = 50
      print(x) # Aqui x é 50, se comentar o x = 50 acima, o x será 1, pois está pegando o x global
    
    global_x()

  other_function()
  print(x) # Aqui x é 10, pois está no escopo da funcao scope

print(x) # Aqui x é 1, porque esta sendo colocado antes da funcao ser executada
scope()
print(x) # E aqui x é 50, pois esta sendo executado o global dentro da função global_x, mas é uma má prática