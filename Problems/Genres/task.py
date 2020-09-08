from nltk.corpus import brown

# import nltk
#
# nltk.download('brown')

# print(brown.categories())
print(brown.fileids(categories=input())[:3])