# Osama Rahman 1304349 Open Domain QA System - TonAI
# Why can't I get birthYear for Adolf Hitler?
# DBpedia note: If answer returns link, get end of URL for answer.
# IE: "Who was the cinematographer the Westworld TV show?"
# Would return a link to Paul Cameron's page
# Instead, get "/Paul_Cameron_" from URL

from SPARQLWrapper import SPARQLWrapper, JSON
import sys
import nltk

# start = ok

print '\n', "Hi, I'm TonAI. What would you like to know about? "

inp = raw_input()
response = inp.replace(" ", "_")


print '\n', "Enter a prefix (rdfs, dbo)"
prefix_input = raw_input()
prefix = prefix_input

print '\n', "Enter a property input (comment, birthYear)"
property_input = raw_input()
label = property_input

# Use for quick test - when you don't want to use other inputs
# prefix = "rdfs"
# label = "comment"

# inp_tokens = nltk.word_tokenize(inp)
# print inp_tokens

# label stands for property, the type of data that is retrieved
# Given it's own variable as it might change depending on question
# The label for name would be different to birthday
# Need to fill with other property types


# SPARQL connection to DBPedia
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""

    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dbo: <http://dbpedia.org/ontology/>


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
