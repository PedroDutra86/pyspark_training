"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
        <- Contagem de complexidade (ruim)
"""

speed = 59 # velocidade atual do carro
car_location = 101 # local em que o carro está na estrada

FIRST_RADAR = 60 # velocidade máxima do radar 1
FIRST_RADAR_LOCATION = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega
#--------------------------------------------------------------------------------
radar_negative_range = FIRST_RADAR_LOCATION - RADAR_RANGE
radar_positive_range = FIRST_RADAR_LOCATION + RADAR_RANGE
car_speed_exceeded = speed > FIRST_RADAR
car_in_radar_range = car_location >= radar_negative_range and car_location <= radar_positive_range 
did_car_pass_radar = car_in_radar_range
#--------------------------------------------------------------------------------
car_fined = did_car_pass_radar and car_speed_exceeded


if car_speed_exceeded:
  print('Limite excedido')
if did_car_pass_radar:
  print('Carro passou no radar')
if car_fined:
  print('Carro multado no radar')