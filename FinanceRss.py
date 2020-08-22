from tkinter import*
import feedparser #tuodaan feedparser kirjasto ohjelmaan.
from tkinter.font import Font #tuodaan fonttikirjasto.


#luodaan funktio, jolla haetaan Rss-syötteet.
def getNews():
    #jos arvopaperi rss checkbox on valittu, tallennetaan news muuttujaan
    #syötteet, jotka feedparser hakee sille parametrina annetusta osoitteesta.
    if arvopaperirss.get() == 1:
        news = feedparser.parse('https://www.arvopaperi.fi/api/feed/v2/rss/ap')
        #käydään syötteet sisältävä muuttuja läpi for-silmukassa ja tulostetaan
         #syötteet insert komennolla tekstilaatikkoon.
        for post in news.entries:
            post.title + ': ' + post.description
            textbox.insert(INSERT,'\n',END)
            textbox.insert(INSERT,post.title,END)
            textbox.insert(INSERT,post.description,END)
            textbox.insert(INSERT,'\n',END)

#jos taloussanomat checkbox on valittu, hakee feedparser sille parametrina
#annetusta osoitteesta rss-syötteet.
    
    elif talousrss.get() == 1:
        news = feedparser.parse('https://www.is.fi/rss/taloussanomat.xml')
        for post in news.entries:
            post.title + ': ' + post.description
            textbox.insert(INSERT,'\n',END)
            textbox.insert(INSERT,post.title,END)
            textbox.insert(INSERT,post.description,END)
            textbox.insert(INSERT,'\n',END)
            
#luodaan funktio, jolla tyhjennetään tekstilaatikko.
def clearText():
    textbox.delete(1.0,END)

#luodaan pohjakomponentti.            
root = Tk()
#lisätään otsikko ohjelmaikkunaan.
root.title('Rss reader')

#tallennetaan titlefont muuttujaan system-fontti.
titlefont = Font (family = 'System')

#lisätään pohjakomponentin taustaväri
root.configure( background = 'cadet blue')

#luodaan rullauspalkki, sijoitetaan se oikealle sivulle ja annetaan rullaussuunnaksi
#y-akseli eli pystysuuntainen rullaus.
scrollingbar = Scrollbar(root)
scrollingbar.pack(side = RIGHT, fill = Y)

#label komennolla luodaan tekstikomponentti, font komennolla käytetään tekstissä
#titlefont muuttujaan tallennettua fonttia.
name = Label(root, text = 'Financial Rss reader',bg = 'cadet blue', font = titlefont)

#luodaan tekstilaatikko, laatikoon koko annetaan width ja height komennoilla.
textbox = Text(root, width = 90, height = 20, yscrollcommand = scrollingbar.set)
scrollingbar.config (command = textbox.yview)

#button komenolla luodaan painikkeet, command komennolla kerrotaan funktio
#joka suoritetaan kun nappia on painettu.
newsbutton = Button(root, text = 'Get RSS', command = getNews, relief = 'solid')
clearbutton = Button(root, text = 'Clear textbox',command = clearText)

#luodaan checkboxit checkbutton komennolla ja niiden tarvitsemat muuttujat
#IntVar komennolla.
arvopaperirss = IntVar()
apvalinta = Checkbutton(root, text = 'Arvopaperi Rss feed', bg = 'cadet blue', variable = arvopaperirss)
talousrss = IntVar()
tsvalinta = Checkbutton(root, text = 'Taloussanomat Rss feed', bg = 'cadet blue', variable = talousrss)

#pakataan komponentit, että ne näkyvät ohjelmassa. side komennolla asemoidaan
#komponentteja. Pady komennolla lisätään tyhjää tilaa komponenttien ympärille.
name.pack()
apvalinta.pack(side=TOP)
tsvalinta.pack(side=TOP)
textbox.pack()
newsbutton.pack(pady=4)
clearbutton.pack(pady=4)
mainloop()
