# Osama Rahman 1304349 Open Domain QA System - TonAI
# If there is no English translation, system won't return anything
# TODO Make use of other prefixes to get more information - Need more than just comment

from SPARQLWrapper import SPARQLWrapper, JSON
import nltk

print '\n', "Hi, I'm TonAI. What would you like to know about? "

inp = raw_input()
inp_string = inp

# Use for quick test - when you don't want to use other inputs
# response = inp.replace(" ", "_")
# print '\n', "Enter a prefix (rdfs, dbo)"
# prefix_input = raw_input()
# prefix = prefix_input
# print '\n', "Enter a property input (comment, birthYear)"
# property_input = raw_input()
# label = property_input

inp_tokens = nltk.word_tokenize(inp)
tagger = nltk.pos_tag
tagged_input = tagger(inp_tokens)
print tagged_input

# Tags to be used to identify keywords for response
# Change as you go along, testing different URLs
# TODO if 'IN' comes before NNP(and maybe others) add to response
response_tags = ['NNP', 'NN', 'JJ', 'NNS', 'IN']


prefix = ""
label = "comment"
response = ""

# Will give rdfs if 'Who' is in the question
for i in tagged_input:
    if 'WP' in i:
        prefix = "rdfs"
        label = "comment"

temp = []
for i in tagged_input:
    if i[1] in response_tags:
        temp.append(i[0])

response = "_".join(temp)

if "?" not in inp:
    response.replace(" ", "_")
    prefix = "rdfs"


print "response:", response
print "temp: ", temp


print '\n', "http://dbpedia.org/resource/"+response+">"+prefix+":"+label+"?"+label


# SPARQL connection to DBPedia
def info_retrieval():

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX dct: <http://purl.org/dc/terms/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>

        SELECT ?"""+label+"""
        WHERE { <http://dbpedia.org/resource/"""+response+""">"""+prefix+""":"""+label+""" ?"""+label+"""

    # Will not work if property is not text - IE won't work with birthYear
    FILTER (langMatches(lang(?"""+label+"""),"en"))
        }
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        print '\n' + (result[label]["value"])


info_retrieval()
