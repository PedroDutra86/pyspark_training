# Exercício -> Sistema de perguntas e respostas

questions = [
  {
    'Question': 'Quanto é 2 + 2?',
    'Options': ['1', '3', '4', '5'],
    'Answer': '4',
  },
  {
    'Question': 'Quanto é 5 * 5?',
    'Options': ['25', '55', '10', '51'],
    'Answer': '25',
  },
  {
    'Question': 'Quanto é 10 / 2?',
    'Options': ['4', '5', '2', '1'],
    'Answer': '5',
  },
]

accumulator = 0

for question in questions:
  print(f'Pergunta: {question["Question"]}')
  print()

  for index, option in enumerate (question['Options']):
    print(f'{index}) {option}')
  print()

  answer = input('Digite uma das opções acima (digite o índex e não o número): ')

  try:
    answer = int(answer)
  except ValueError:
    print(f'"{answer}" não é um número')
    continue

  if answer < 0 or answer > len(question["Options"]):
    print('Opção inválida! Tente novamente')

  if question['Options'][answer] == question['Answer']:
    print('Você acertou! ✅')
    accumulator += 1
  else:
    print('Você errou ❌')

print(f'Você acertou {accumulator} de {len(questions)} perguntas')