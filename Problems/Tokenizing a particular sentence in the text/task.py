from nltk.tokenize import sent_tokenize
from nltk.tokenize import regexp_tokenize

sentences = sent_tokenize(input())

print(regexp_tokenize((sentences[int(input())]), "[A-z']+"))
