#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from pytube import Playlist
from colorama import Fore
import random
import subprocess
import platform
import os
import re

#------------------------------------------------------------
#clear the screen
def clr():
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate()
    else:
        print("\033c", end="")
clr()

#-------------------------------------------------------------
#colors
white = Fore.WHITE
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
cyan = Fore.CYAN
magenta = Fore.MAGENTA
colors = (white, green, magenta, yellow, cyan)
color = random.choice(colors)

#---------------------------------------------------------------
#banner

banner = """
██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗      ██████╗ ██╗   ██╗      █████╗ ███████╗███████╗██╗███████╗████████╗
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║      ██╔══██╗╚██╗ ██╔╝     ██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗██████╔╝ ╚████╔╝█████╗███████║███████╗███████╗██║███████╗   ██║   
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██╔═══╝   ╚██╔╝ ╚════╝██╔══██║╚════██║╚════██║██║╚════██║   ██║   
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ██║        ██║        ██║  ██║███████║███████║██║███████║   ██║   
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚═╝        ╚═╝        ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   


"""
author = 'Venom 🐍 (Gaurav Chaudhary)'
team = 'From Team Venom 🐍'
facebook = 'https://facebook.com/venomgrills'
insta = 'https://instagram.com/i.m.gauravchaudhary'
github = 'https://github.com/venomsec-Dev/'
def bnPrint():
    print(color + banner + color)
    print(color + '   Author: ' + color + green + author + green)
    print(color + '   Team: ' + color + red + team + red)
    print(color + '   Facebook: ' + color + yellow + facebook + yellow)
    print(color + '   Insta: ' + color + cyan + insta + cyan)
    print(color + '   Github: ' + color + white + github + white)
    print('\n')
bnPrint()
#---------------------------------------------------------------
#Menu
print(white + '     [1] ' + color + "Tutorials from Popular blogging and Tutorial Sites")
print(white + '     [2] ' + color + "Download Full Playlist of famous python tutorials from youtube")
print(white + '     [3] ' + color + "Get Sample python project ideas and mindmap")
print(white + '     [4] ' + color + "Get Idea of syntax of any library from pypi.org")
print(white + '     [5] ' + color + "Python Error Resolver")
print(white + '     [6] ' + color + "Message me your problems and queries regarding python")
print(white + '     [X] ' + color + "Exit")
print('\n')
choose = input(white + '     [+] ' + color + "Enter a choice: ")
#---------------------------------------------------------------
#blogs
x = 0
if choose == '1':
    #----------------------------
    clr()
    bnPrint()
    print(white + '     [1] ' + color + "Tutorialspoint.com")
    print(white + '     [2] ' + color + "Learnpython.org")
    print(white + '     [3] ' + color + "Programiz.com")
    print(white + '     [4] ' + color + "Guru99.com")
    print(white + '     [5] ' + color + "Diveintopython3.net")
    print(white + '     [6] ' + color + "Studytonight.com")
    print(white + '     [7] ' + color + "Thepythonguru.com")
    print(white + '     [B] ' + color + "Back to Main Menu")
    print(white + '     [X] ' + color + "Exit")
    print('\n')
    blog_choice = input(white + '    [+] ' + color + "Enter your choice: ")
    clr()
    bnPrint()
    if blog_choice == '1':
        tutorialpoint = 'https://www.tutorialspoint.com/python/index.htm'
        tutpointitles = []
        tutpointlinks = []
        response = requests.get(tutorialpoint)
        soup = BeautifulSoup(response.content,'html.parser')
        content = soup.find('ul', class_="toc chapters")
        for i in content.findAll('li'):
            titles = i.text
            tutpointitles.append(titles)
        for i in content.findAll('a'):
            links = i.get('href')
            new_links = 'https://www.tutorialspoint.com'+links
            tutpointlinks.append(new_links)
        for i in tutpointitles:
            print(white + '    [' + color + str(x)  + '] ' + color + i)
            x += 1
        print(' ')
        tutchoice = int(input(white + '    [+] ' + color + 'Enter your choice: '))
        def mukul(hello):
    	    url = tutpointlinks[hello]
    	    response = requests.get(url)
    	    soup = BeautifulSoup(response.content, 'html.parser')
    	    for i in soup.findAll('p'):
       	    	print(color + i.text)
        mukul(tutchoice)
    elif blog_choice == '2':
        #----------------------------
        learnpython = 'https://www.learnpython.org/'
        learnpythonLinks = []
        learnpythonTitles = []
        response = requests.get(learnpython)
        soup = BeautifulSoup(response.content, 'html.parser')
        for i in soup.findAll('li'):
            links = i.find('a')
            titles = links.text
            learnpythonTitles.append(titles)
            link = links.get('href')
            if link.startswith('/') is True:
                if len(link) > 1:
                    learnpythonLinks.append(link)
                else:
                    pass
            else:
                pass
        junk = ["Home (current)","About","Certify","More Languages","Star","Python","Java","HTML","Go","C","C++","JavaScript","PHP","Shell","C#","Perl","Ruby","Scala","SQL","","","",                    "More Languages"]
        learnpythonLinks.remove('/about')
        for i in junk:
            try:
                learnpythonTitles.remove(i)
            except:
                pass
        bigJunk = learnpythonTitles[0]
        bigJunk1 = learnpythonTitles[1]
        bigjunk = [bigJunk, bigJunk1]
        for i in bigjunk:
            learnpythonTitles.remove(i)
        for i in learnpythonTitles:
            print(white + '     [' + color + str(x) + '] ' + color + i)
            x += 1
        print(' ')
        learnpythonChoice = int(input(white + '     [x] ' + color + 'Enter a number to continue: '))
        def manasvi(gaurav):
            url = 'https://learnpython.org' + learnpythonLinks[gaurav]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            article = soup.find('div', id="inner-text")
            print(color + article.text)
        manasvi(learnpythonChoice)
#-------------------------------
    elif blog_choice == '3':
        programiz = "https://www.programiz.com/python-programming"
        programizLinks = []
        programizTitles = []
        response = requests.get(programiz)
        soup = BeautifulSoup(response.content, 'html.parser')
        article = soup.find('div', class_="contents contents--neg")
        for i in article.findAll('a'):
            links = i.get('href')
            titles = i.get('title')
            programizTitles.append(titles)
            if links.startswith('/') is True:
                programizLinks.append(links)
            else:
                pass
        junk = ["/python-programming/first-program","/learn-python","/python-programming/examples","/python-programming/methods","/python-programming/online-compiler/","/python-programming/guide","Introduction","Python Flow Control","Python Functions","Python Datatype","Python Files","Python Object and Class","Python Advanced Tutorials","Python Date and Time","About Python Programming","Why learn Python?","How to learn Python?","Python Resources","Python First Program","Python official documentation","Get Learn Python App","Python Examples","Python methods","Python Online Compiler","Python Guide","None","None","None"]
        for i in junk:
            try:
                programizLinks.remove(i)
            except:
                pass
        for i in junk:
            try:
                programizTitles.remove(i)
            except:
                pass
        programizJunk = programizTitles[-1]
        programizJunk1 = programizTitles[-2]
        programizJunk2 = programizTitles[-3]
        newjunkList = [programizJunk, programizJunk1, programizJunk2]
        for i in newjunkList:
            programizTitles.remove(i)
        for i in programizTitles:
            print(white + '    [' + color + str(x) + '] ' + color + i)
            x += 1
        programizChoice = int(input('Enter a number: '))
        def mannu(guru):
            url = 'https://www.programiz.com'+programizLinks[guru]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            article = soup.find('div', class_="editor-contents")
            print(color + article.text + color)
        mannu(programizChoice)
#----------------------------------
    elif blog_choice == '4':
        guru99 = "https://www.guru99.com/python-tutorials.html"
        guruLinks = []
        guruTitles = []
        guruArticles = []
        response = requests.get(guru99)
        soup = BeautifulSoup(response.content, 'html.parser')
        for i in soup.findAll('td', class_="responsivetable"):
            links = i.find('a')
            link = links.get('href')
            guruLinks.append(link)
            titles = links.get('title')
            guruTitles.append(titles)
        for i in guruTitles:
            print(white + '     [' + color + str(x) + white + '] ' + color + i)
            x += 1
        guruChoice = int(input(white + '     [+] ' + color + 'Enter your choice: '))
        print(' ')
        def tejas(val):
            url = 'https://www.guru99.com'+guruLinks[val]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            for i in soup.findAll('p'):
                txt = i.text
                guruArticles.append(txt)
        tejas(guruChoice)
        guruJunk = guruArticles[-1]
        guruJunk1 = guruArticles[-2]
        guruJunk2 = guruArticles[-3]
        guruJunk3 = guruArticles[-4]
        guruJunk4 = guruArticles[-5]
        guruJunk5 = guruArticles[-6]
        gurujunkList = [guruJunk, guruJunk1, guruJunk2, guruJunk3, guruJunk4, guruJunk5]
        for i in gurujunkList:
            guruArticles.remove(i)
        for i in guruArticles:
            print(color + i + color)
        #-------------------------------------
    elif blog_choice == '5':
        diveintopython = "https://diveintopython3.net/"
        diveLinks = []
        diveTitle = []
        response = requests.get(divetopython)
        soup = BeautifulSoup(response.content, 'html.parser')
        for i in soup.findAll('li'):
            links = i.find('a')
            link = links.get('href')
            diveLinks.append(link)
            titles = links.text
            diveTitle.append(titles)
        for i in diveTitle:
            print(white + '     [ ' + color + str(x) + white + '] ' + color + i)
            x += 1
        print(" ")
        diveChoice = int(input(white + '     [+] ' + color + 'Enter a choice: '))
        def gautam(single):
            url = 'https://diveintopython3.net/' + diveLinks[diveChoice]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            for i in soup.findAll('p'):
                print(color + i.text + color)
        gautam(diveChoice)
        #--------------------------------------------
    elif blog_choice == '6':
        studytonight = "https://www.studytonight.com/python/"
        studyLinks = []
        studyTitles = []
        response = requests.get(studytonight)
        soup = BeautifulSoup(response.content, 'html.parser')
        for i in soup.findAll("ul", class_="counter-list"):
            for l in i.findAll('a'):
                link = l.get('href')
                title = l.text
                studyTitles.append(title)
                if link.startswith('/') is False:
                    new_link = '/' + link
                    studyLinks.append(new_link)
                else:
                    studyLinks.append(link)
        studyLinks.remove('/')
        junkplace = studyTitles[-1]
        junkplace1 = studyTitles[-2]
        junkplaceVal = [junkplace, junkplace1]
        for i in junkplaceVal:
            try:
                studyLinks.remove(i)
            except:
                pass
        for i in studyTitles:
            print(white + '     [' + color + str(x) + white + '] ' + color + i)
            x += 1
        print(' ')
        studyChoice = int(input(white + '     [+] ' + color +"Enter a choice: "))
        def study(tonight):
            url = 'https://www.studytonight.com/'+studyLinks[tonight]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            article = soup.find('div', id="body-content")
            print(color + article.text + color)
        study(studyChoice)

        #--------------------------------------
    elif blog_choice == '7':
        pythonguru = "https://thepythonguru.com/"
        pythonguruLinks = []
        pythonguruTitles = []
        response = requests.get(pythonguru)
        soup = BeautifulSoup(response.content, 'html.parser')
        for i in soup.findAll('li'):
            links = i.find('a')
            link = links.get('href')
            pythonguruLinks.append(link)
            title = links.text
            pythonguruTitles.append(title)
        pythonguruJunk = ["/","/blog/","/contact-us/","/write-for-us/","#","/tools/pygments-demo/","/comparing-python-and-nodejs-which-is-best-for-your-project/","/windows-10-for-a-python-user-tips-for-optimizing-performance/","/what-skills-do-you-need-to-succeed-as-a-python-dev-in-2020/","/9-reasons-why-you-should-use-cicd/","/how-to-make-money-if-you-have-python-skills/","/about/","/terms-of-use/","/privacy-policy/","/contact-us/","Start Here","Blog","Contact","Write For Us","Tools","Pygments Demo","# Comparing Python and Node.Js: Which Is Best for Your Project?","Windows 10 for a Python User: Tips for Optimizing Performance","What Skills Do You Need to Succeed as a Python Dev in 2020?","9 Reasons Why You Should Use CICD","How To Make Money If You Have Python Skills","About","Terms","Privacy Policy","Contact"]
        for i in pythonguruJunk:
            try:
                pythonguruLinks.remove(i)
            except:
                pass
            try:
                pythonguruTitles.remove(i)
            except:
                pass
        pgJunk = pythonguruTitles[0]
        pythonguruTitles.remove(pgJunk)
        for i in pythonguruTitles:
            print(white + '     [' + color + str(x) + white + '] ' + color + i)
            x += 1
        print('\n')
        pgChoice = int(input(white + '     [+] ' + color + 'Enter your choice: '))
        def mind8(hunter):
            url = 'https://thepythonguru.com' + pythonguruLinks[hunter]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            for i in soup.findAll('p'):
                print(color + i.text + color)
        mind8(pgChoice)
    elif blog_choice == 'B' or blog_choice == 'b':
        os.system("python3 venom.py")
    else:
        exit()
#--------------------------------------------------------------------------
#ytDownload
elif choose == '2':
    clr()
    bnPrint()
    print(white + '     [1] ' + color + "Code with Harry")
    print(white + '     [2] ' + color + "Harshit Vashisth's Python Playlist")
    print(white + '     [3] ' + color + "Telusko's Python Playlist")
    print(white + '     [4] ' + color + "Csdojo's Python Playlist")
    print(white + '     [5] ' + color + "Programming Knowledge")
    print(white + '     [6] ' + color + "Krishna Naik's Python Playlist")
    print(white + '     [7] ' + color + "Edureka")
    print(white + '     [8] ' + color + "FreeCodeCamp.org")
    print(' ')
    ytDownChoice = int(input(white + '     [+] ' + color + "Enter the choice: "))
    print(' ')
    #youtube channels
    codewithharry = "https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME"
    harshitvashisth = "https://www.youtube.com/playlist?list=PLwgFb6VsUj_lQTpQKDtLXKXElQychT_2j"
    telusko = "https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"
    csdojo = "https://www.youtube.com/playlist?list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg"
    programmingKnowledge  = "https://www.youtube.com/playlist?list=PLS1QulWo1RIYt4e0WnBp-ZjCNq8X0FX0J"
    krishNaik = "https://www.youtube.com/playlist?list=PLZoTAELRMXVNUL99R4bDlVYsncUNvwUBB"
    edureka = "https://www.youtube.com/playlist?list=PL9ooVrP1hQOHY-BeYrKHDrHKphsJOyRyu"
    freeCodeCamp = "https://www.youtube.com/playlist?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB"
    ytChannels = [codewithharry, harshitvashisth, telusko, csdojo, programmingKnowledge, krishNaik, edureka, freeCodeCamp]
    output = ['Code With harry', 'Harshit Vashisth', 'Telusko', 'Csdojo', 'Programming Knowledge', 'Krish Naik', 'Edureka', 'FreeCodeCamp']
    try:
        os.mkdir('YTPlaylist')
    except:
        pass
    def downyt(channel):
        link = channel - 1
        os.chdir('YTPlaylist')
        os.mkdir(output[link])
        os.chdir(output[link])
        playlist = Playlist(ytChannels[link])
        for video in playlist.videos:
            print("Downloading: " + video.title)
            video.streams.first().download()
    downyt(ytDownChoice)
#--------------------------------------------------------------------------
elif choose == '3':
    clr()
    bnPrint()
    #samplecodes
    realpython = "https://realpython.com"
    titles = []
    links = []
    response = requests.get(realpython)
    soup = BeautifulSoup(response.content, 'html.parser')
    row = soup.find('div', class_='row')
    for i in row.findAll('div', class_="card-body m-0 p-0 mt-2"):
        title = i.find('h2').text
        titles.append(title)
        link = i.find('a').get('href')
        new_link = realpython+link
        links.append(new_link)
    print(' ')
    for i in titles:
        print(white + '     [' + color + str(x) + white + '] ' + color + i)
        x += 1
    print(' ')
    choose = int(input('Enter a number: '))
    def venom(number):
        url = links[number]
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        article = soup.find('div', class_="article-body")
        print(' ')
        print('[+]' + '-------------------------' + titles[number] + '-----------------------------' + '[+]')
        print(' ')
        for i in article.findAll('p'):
            p = i.text
            new = p.replace('Table of Contents', ' ')
            print(new)
    venom(choose)
#-----------------------------------------------------------------------
#library info
elif choose == '4':
    clr()
    bnPrint()
    library = input(white + '     [+] ' + color + 'Enter the library name: ')
    url = "https://pypi.org/project/"+library
    new_url = url + library
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        for i in soup.findAll('pre'):
            print(color + i.text)
    except:
        print("Maybe library name is wrong or else we don't have any info!!")
#-------------------------------------------------------------------------
elif choose == '5':
    clr()
    bnPrint()
    error = input(white + '    [+] ' + color + 'Enter your error: ' + color)
    url = 'https://www.google.com/search?q=' + error
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ok = soup.find_all('div', class_='kCrYT')
    ok = str(ok)
    new = re.findall('<a href="(.*?)"', ok)
    new_link = len(new)
    answer = []
    solutions = []
    x = 0
    if new_link > 1:
        for i in new:
            i = str(i)
            if i.startswith('/url?q=') is True:
                i = i[7:-100]
                if i.startswith('https://stackoverflow.com/') is True:
                    _response = requests.get(i)
                    _soup = BeautifulSoup(_response.content, 'html.parser')
                    solution = _soup.find('div', id="answers")
                    try:
                        for answers in solution.find_all('div', class_="s-prose js-post-body"):
                            print(white + '<----------------' + color + green + ' Answer ' + str(x) + green + white + '------------------->')
                            print(color + answers.get_text() + color)
                            x += 1
                    except TypeError as e:
                        pass
                else:
                    pass
            else:
                pass
#-----------------------------------------------------------------
#message
elif choose == '6':
    clr()
    bnPrint()
    print(white + '   [+] ' + color + "Whatsapp Me: " + color + green + "+91 9910332273" + green)
    print(white + '   [+] ' + color + "Call Me: " + color + red + "+91 8595869214" + red)
    print(white + '   [+] ' + color + "Mail Me: " + yellow + "babesurdevil@gmail.com" + yellow)
    print(white + '   [+] ' + color + "Mail Me: " + cyan + "teamvenom@protonmail.com" + cyan)

#-------------------------------------------------------------------

elif choose == 'X' or choose == 'x':
    print(' ')
    print(white + '     [-] ' + color + 'Bye Bye Exiting')
    exit()
else:
    print(' ')
    print(white + '     [+] ' + red + "I don't understand you!!!")
    os.system("python3 venom.py")
