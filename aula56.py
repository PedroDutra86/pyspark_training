"""
split e join com list e str
split -> divide uma string (list)
join -> une uma string
"""

sentence = '   Olha só que   , coisa interessante   '

sentence_list = sentence.split(',')
formatted_sentence_list = []
for index, word in enumerate(sentence_list):
  formatted_sentence_list.append(sentence_list[index].strip())

print(formatted_sentence_list)
print(sentence_list)

joined_sentences = ', '.join(formatted_sentence_list)
print(joined_sentences)
