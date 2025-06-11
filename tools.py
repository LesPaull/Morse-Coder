

def ana_menu_veya_cikis():
    secim = input("Çıkmak için 'q' tuşuna, ana menüye dönmek için herhangi bir tuşa basın: ")
    if secim.strip().lower() == "q":
        print("Hoşçakalın!")
        exit()
    else:
        menu_goster()



def menu_goster():
    print("Çevirici Uygulamasına Hoşgeldiniz!")
    print("İşlemler")
    print("1. Mors Kodu")
    print("2. İşaret Dili")
    print("3. Braille Alfabesi")
    print("4. Morse Quotes")
    print("5. Çıkış")
    while True:
                soru = input("Lütfen yapmak istediğiniz işlemin numarasını girin: ")
                if soru == "1":
                    print("Mors Alfabesine Yönlendiriliyorsunuz!")
                    preter.ask_whether()
                elif soru == "2":
                    print("Bu işlem şu anda geliştirme aşamasındadır, daha sonra tekrar deneyebilirsiniz...")
                    ana_menu_veya_cikis()
                elif soru == "3":
                    print("Bu işlem şu anda geliştirme aşamasındadır, daha sonra tekrar deneyebilirsiniz...")
                    ana_menu_veya_cikis()
                elif soru == "4":
                    preter.morse_quotes()
                elif soru == "5":
                    exit()


class morse_code_preter:

    def __init__(self):
        self.Morse_quotes = { "Qui prodest, scelus is fecit.- Senaca": "--.- ..- ../.--. .-. --- -.. . ... -/... -.-. . .-.. ..- .../.. .../..-. . -.-. .. -"
}
        self.Morse_Codes_Dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-","L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "X": "-..-", "Y": "-.--", "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0":"-----", " ": "/"}
        self.reverse_dict = {v: k for k, v in self.Morse_Codes_Dict.items()}

    def ask_whether(self):
        askwhether = input("Mors >> Yazı için '1', Yazı >> Mors için '2' tuşuna basınız: ")
        if askwhether == "1":
            self.morse_to_lang()
        elif askwhether == "2":
            self.lang_to_morse()
        else:
            print("Yanlış bir tuşlama yaptınız, Lütfen tekrar deneyin!")
            preter.ask_whether()

    def morse_to_lang(self):
        print("UYARI! Harfler arası birer boşluk, kelimeler arası / kullanın.")
        metinmtl = input("Morse Kodunu Girin: ")

        words = metinmtl.strip().split("/")
        output = []

        for word in words:
            letters = word.strip().split()
            decoded = ''.join(self.reverse_dict.get(h.strip(), '?') for h in letters)
            output.append(decoded)

        print("Metin Çevirildi:", ' '.join(output))
        cikis2 = input("çıkmak için q tuşuna, ana menü için herhangi bir tuşa basın: ")
        if cikis2 == "q".lower().strip():
            exit()
        else:
            menu_goster()

    def lang_to_morse(self):
        print("UYARI! LUTFEN INGILIZCE KARAKTER KULLANIN.")
        metinltm = input("Metin Girin: ").upper()
        kelimeler = metinltm.split()
        morse_kelimeler = []
        for kelime in kelimeler:
            harfler = [self.Morse_Codes_Dict.get(h, "?") for h in kelime]
            morse_kelimeler.append(' '.join(harfler))
        print('Metin çevirildi:', '/'.join(morse_kelimeler))
        ana_menu_veya_cikis()

            
    
    def morse_quotes(self):
        for quote, morse in self.Morse_quotes.items():
            print(f"\n{quote}\n{morse}")
        ana_menu_veya_cikis()
        
preter = morse_code_preter()

menu_goster()









