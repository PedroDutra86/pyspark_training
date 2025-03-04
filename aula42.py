phrase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum'.lower()

count = 0
letter_occurrences = 0
most_frequent_letter = ''

while count < len(phrase):
  current_letter = phrase[count]

  if current_letter == ' ':
    count += 1
    continue

  letter_count = phrase.count(current_letter)

  if letter_occurrences < letter_count:
    letter_occurrences = letter_count
    most_frequent_letter = current_letter

  count += 1

print(most_frequent_letter, letter_occurrences)