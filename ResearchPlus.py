import requests #Python library that retrieves urls
from bs4 import BeautifulSoup #Python Library that parses html
import re

def web(page,WebUrl):
    if(page>0): # page is the length of a list of urls
        url = WebUrl
        using = True
        code = requests.get(url) #html code for url page
        plain = code.text #text html code
        s = BeautifulSoup(plain, "html.parser") #takes html code and parses it
        for link in s.findAll('a', attrs={'href': re.compile("^http://")}):
            #print(link.get('href'))
            listOfUrls.append(link.get('href'))
        while (using):
            #print(len(listOfUrls))
            WebUrl = listOfUrls.pop(0)
            texts = s.findAll(text=True)
            PartialWord = input("What to you want to search for: ")
            allText = [word for word in texts]
            need = []
            #keywords = [word for word in texts if PartialWord in word]
            for word in texts:
                if (PartialWord in word):
                    if (texts.index(word) > 0):
                        Num = allText.index(word) #Num is equal to word
                        subNum = Num - 2 
                        addPrev = allText[(Num-1)]
                        if addPrev.startswith('\n'):
                            addPrev = allText[subNum]
                            while addPrev.startswith('\n'):
                                subNum-=1
                                addPrev = allText[(subNum)]
                        subNum = Num - 2
                        if addPrev.startswith('['):
                            addPrev = allText[subNum]
                            while addPrev.startswith('['):
                                subNum-=1
                                addPrev = allText[subNum]
                        subNum = Num - 2
                        if addPrev.endswith('('):
                            addPrev = allText[subNum]
                            while addPrev.endswith('('):
                                subNum+=1
                                addPrev = allText[subNum]
                            
                        need.append(addPrev)
                        need.append(word)
                        
                        addNum = Num + 2
                        addNext = allText[(Num+1)]
                        if addNext.startswith('\n'):
                            addNext = allText[addNum]
                            while addNext.startswith('\n'):
                                addNum+=1
                                addNext = allText[addNum]
                        addNum = Num + 2
                        if addNext.startswith('['):
                            addNext = allText[addNum]
                            while addNext.startswith('['):
                                addNum+=1
                                addNext = allText[addNum] 
                        addNum = Num + 2
                        if addNext.endswith('('):
                            addNext = allText[addNum]
                            while addNext.endswith('('):
                                addNum+=1
                                addNext = allText[addNum]
                        
                        need.append(addNext)
                        
                    elif (texts.index(word) == 0):
                        need.append(word)
                        addNum = Num + 2
                        addNext = allText[Num+1]
                        if addNext.startswith('\n'):
                            addNext = allText[addNum]
                            while addNext.startswith('\n'):
                                addNum+=1
                                addNext = allText[addNum]
                        if addNext.startswith('['):
                            addNext = allText[addNum]
                            while addNext.startswith('['):
                                addNum+=1
                                addNext = allText[addNum] 
                        if addNext.endswith('('):
                            addNext = allText[addNum]
                            while addNext.endswith('('):
                                addNum+=1
                                addNext = allText[addNum]
                        
                        need.append(addNext)
                        
                    
            for i in need:
                print(i)
            keepPlaying = input("Do you want to continue researching? ")
            if keepPlaying == "n" or keepPlaying == "N":
                using = False
                
           

startUrl = input("What url do you want to search: ")
listOfUrls = [startUrl]
WebUrl = startUrl
web(1,WebUrl)
