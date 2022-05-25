import urllib.request
from bs4 import BeautifulSoup

def dict():
    word = input("Enter your word:")

    originalUrl = 'https://www.merriam-webster.com/dictionary/'+ word

    #parsing the webpage
    request = urllib.request.Request(originalUrl)
    content = urllib.request.urlopen(request)
    parse = BeautifulSoup(content, 'html.parser')

    #store all definitions in a variable
    definitions = parse.find_all('span', attrs={'class': 'dtText'})

    n = 1

    #function get rid of tags (<span> </span> in this case.)
    def parseDefinition(text):
        parsedDefinition = text.get_text()
        print(str(n) + parsedDefinition)
        print("")

    #find_all returns list, therefore 'for x in variable' is necessary.
    for definition in definitions:
        parseDefinition(definition)
        n += 1

while True:
    answer = input("Search words?(y/n): ")
    if answer not in ('y', 'n'):
        input("Invalid input. Goodbye.")
        break
    if answer == 'y':
        dict()
    else:
        input("Goodbye.")
        break
