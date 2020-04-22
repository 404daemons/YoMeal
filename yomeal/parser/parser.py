# import re


def parseMsg(msg):
    foodSet = set(line.strip() for line in open(
        '/Users/bittu/Downloads/gito/YoMeal/yomeal/parser/food.txt'
        ))
    # TODO: use regex
    for word in msg.split():
        if word in foodSet:
            print(word)


test = "this is banana"
parseMsg(test)

'''
# # Simple example using spaCy
import spacy
nlp = spacy.load("en_core_web_sm") 
    # Loading English tokenizer, tagger, parser, NER and word vectors
# # ## OR ##
# import en_core_web_sm
# nlp = en_core_web_sm.load()

# Process whole documents
text = ("this is made from banana, 1gm eggs.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)
'''
