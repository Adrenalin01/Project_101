#| USER |   PASSWORD  |
#-----------------------
#| bob  |     123     |
#| ann  |    pass123  |
#| mike | password123 |
#| liz  |    pass123  |

# our dictionary with data
data = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
            }

# we want to ask user for username and password
Username    = str(input('Please enter the username: '))
Password    = str(input('Please enter the password: '))

# two conditions for evaluating the inputs
if data.get(Username) != Password:
    print('Password or username is wrong')

elif data.get(Username) == Password:
    print('Permission granted')



#'''
#author = 
#'''

# definice textu

texts = ['''
situated about 10 miles west of kemmerer, 
fossil butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above twin creek valley 
to an elevation of more than 7500 feet 
above sea level. the butte is located just 
north of us 30n and the union pacific railroad, 
which traverse the valley.''',
'''at the base of fossil butte are the bright 
red, purple, yellow and gray beds of the wasatch 
formation. eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the green river formation, 
which are about 300 feet thick.''',
'''the monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. the richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. the fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. other fish such as paddlefish, 
garpike and stingray are also present.''']

text_choose = int(input('Choose the text you want to analyze [1,2 or 3]: '))

text = texts[text_choose - 1]

#final_text = text.replace(',',' ')
text_array = text.split(' ')
words_count = len(text_array)
print(text_array)
# Oznameni analyzy
print("I'm analyzing the text")
results = [words_count,0,0,0,0]
current_word = 0
while (current_word < words_count):
    analyze_word = text_array[current_word]
    if (analyze_word[0].isupper()):
        results[1] += 1
    if (analyze_word.isupper()):
        results[2] += 1
    if (analyze_word.islower()):
        results[3] += 1
    if (analyze_word.isdigit()):
        results[4] += 1
    current_word += 1
print('-' * 50)
print('There are ' + str(words_count) +  ' words in the selected text.')
print('There are ' + str(results[1]) + ' titlecase words')
print('There are ' + str(results[2]) + ' uppercase words')
print('There are ' + str(results[3]) + ' lowercase words')
print('There are ' + str(results[4]) + ' numeric strings')
print('-' * 50)
bar_index = 0
while (bar_index < len(results)):
    graph_results = results[bar_index]
    graph_text = str(bar_index + 1) + ' ' + str('*' * graph_results) + ' ' + str(graph_results)
    print(graph_text)
    bar_index += 1
