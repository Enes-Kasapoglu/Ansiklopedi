from tkinter import *
from gtts import gTTS
import wikipedia
from playsound import playsound

# Normal Ansiklopedi Penceresi

def main():

    window = Tk()
    window.title("Ansiklopedi")
    window.geometry("650x400")
    window.resizable(False,False)
    window.config(bg="#21232E")
    
    # Fonksiyonlar

    def search():
        word = search_input.get()
        wikipedia.set_lang("tr")
        wikiresult = wikipedia.summary(word,sentences=5)

        resultArea["text"] = (wikiresult)

        print(wikiresult)

    def voice_search():
        wordv = search_input.get()
        wikipedia.set_lang("tr")
        wikiresult = wikipedia.summary(wordv, sentences=3)
        resultArea["text"] = (wikiresult)
        print(wikiresult)
        sesverisi = gTTS(text=wikiresult,lang="tr")
        sesverisi.save("audiodata.mp3")
        playsound("audiodata.mp3")
    
    # Renkler

    background = "#21232E" # Different tone black | Farklı tonda siyah
    font_color = "#fff" # Beyaz | White
    border_color = "#723CC2" # Mor | Purple

    #Tasarım

    # Arama Yazısı
    search_brand = Label(text="Arama Yap", fg=font_color, bg = background)
    search_brand.pack()
    search_brand.place(x = 15, y = 20)
    
    # Yazı Alanı
    search_input = Entry()
    search_input.pack()
    search_input.place(width=400,height=30,x=15,y=46)

    # Arama Butonu

    search_button = Button(text="Ara!",bg="#488bff",fg=font_color,relief=SUNKEN,highlightbackground=background,highlightthicknes=1,command=search)
    search_button.pack()
    search_button.place(width=90,x=425, y = 45)
    
    # Ses Butonu | Voice Button

    voiceButton = Button(text = "Ses", bg = "#488bff",fg=font_color,relief=SUNKEN,command=voice_search,highlightbackground=background,highlightthicknes=1)
    voiceButton.pack()
    voiceButton.place(width=90,x=530,y=45)

    # Sonuç Alanı | Result Area

    resultArea = Label(text="",background="#282a32",fg=font_color,wraplength=600)
    resultArea.pack(expand=YES, fill=BOTH)
    resultArea.place(width=600,height=230,x = 25,y=100)

    mainloop()


main()
