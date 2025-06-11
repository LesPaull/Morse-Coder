# Morse, Braille, Sign Language Coder

Basit seviyede Latin Alfabesi ve Mors Alfabesi arasında çeviri işlemleri yapar.

## Özellikler

Mors'tan Latin'e Çeviri.
Latin'den Mors'a Çeviri.
Braille Alfabesi Çevirisi. (Geliştirme Aşamasında)(!)
İşaret Dili Çevirisi. (Geliştir Aşamasında)(!)
Kendine Ait Morse ve Latin Harfleriyle tanımlanan bir "quotes" Kütüphanesi.(Geliştir Aşamasında)(!)

## Dosya Yapısı

morsepy/
├── run.py          # Uygulama ana dosyası
├── tools.py        # Çeviri fonksiyonlarını içerir
└── pycache/    # Python tarafından otomatik oluşturulan önbellek

## ⚙️ Kullanım

1. Bu repoyu klonla:
   ```bash
   git clone https://github.com/enesakyazi/morsepy.git
   cd morsepy
   python3 run.py

    Girdi: ENES
    Çıktı: . -. . ... 

    Girdi: .... . .-.. .-.. --- 
    Çıktı: HELLO

## Örnek Kullanım

Seçiminizi yapınız:
1. Metni Morse koduna çevir
2. Morse kodunu metne çevir
3. Çıkış

1
Çevirmek istediğiniz metni girin: ENES
Çıktı: . -. . ...

2
Çevirmek istediğiniz Morse kodunu girin: .... . .-.. .-.. ---
Çıktı: HELLO

## Planlanan Geliştirmeler

	•	GUI (grafik arayüz) desteği (Tkinter / PyQt5)
	•	Web sürümü (Flask / Django)
	•	Sesli Morse sinyali çalma
	•	Çoklu dil desteği ve hata kontrol sistemi

## Projeye katkı sağlamak istersen:
	•	Fork’la ve kendi geliştirmelerini yap
	•	Pull Request gönder
	•	Issue oluştur (hata bildirimi veya öneri)

# Lisans

MIT Lisansı ile lisanslanmıştır. Dilediğin gibi kullanabilir, paylaşabilir ve geliştirebilirsin.