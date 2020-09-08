import nltk


sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']

tagged_sent = nltk.pos_tag(sent)
print(tagged_sent[sent.index("raced")][1])
