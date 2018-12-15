#'''
#author = 
#'''
#TEXTS = ['''
#Situated about 10 miles west of Kemmerer, 
#Fossil Butte is a ruggedly impressive 
#topographic feature that rises sharply 
#some 1000 feet above Twin Creek Valley 
#to an elevation of more than 7500 feet 
#above sea level. The butte is located just 
#north of US 30N and the Union Pacific Railroad, 
#which traverse the valley. ''',

#'''At the base of Fossil Butte are the bright 
#red, purple, yellow and gray beds of the Wasatch 
#Formation. Eroded portions of these horizontal 
#beds slope gradually upward from the valley floor 
#and steepen abruptly. Overlying them and extending 
#to the top of the butte are the much steeper 
#buff-to-white beds of the Green River Formation, 
#which are about 300 feet thick.''',

#'''The monument contains 8198 acres and protects 
#a portion of the largest deposit of freshwater fish 
#fossils in the world. The richest fossil fish deposits 
#are found in multiple limestone layers, which lie some 
#100 feet below the top of the butte. The fossils 
#represent several varieties of perch, as well as 
#other freshwater genera and herring similar to those 
#in modern oceans. Other fish such as paddlefish, 
#garpike and stingray are also present.'''
#]


# definice textu
text = "Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley."
text_array = text.split('')
words_count = len(text_array)

# Oznameni analyzy
print("I'm analyzing the text")
results = [words_count,0,0,0,0]
current_word = 0
while (current_word < words_count):
    analyze_word = text_array[current_word]
    if (analyze_word[0].isupper()):
        results[1] += 1
    if (analyze_word.isupper()):
        resuts[2] += 1
    if (analyze_word.islower()):
        resuts[3] += 1
    if (analyze_word.isdigit()):
        results[4] += 1
    current_word += 1
print('There are ' + word_count +  ' words in the selected text.')
print('There are ' + results[1] + ' titlecase words')
print('There are ' + results[2] + ' uppercase words')
print('There are ' + results[3] + ' lowercase words')
print('There are ' + results[4] + ' numeric strings')

bar_index = 0
while (bar_index < len(results)):
    graph_results = results[bar_index]
    graph_text = str(bar_index + 1) + '' + str('*' * graph_results) + '' + str(graph_results)
    print(graph_text)
    bar_index += 1