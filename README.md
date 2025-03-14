# Discord Task Bot

Bu proje, Discord sunucularında görev yönetimini kolaylaştıran bir bottur. Kullanıcılar, bot aracılığıyla görev ekleyebilir, tamamlayabilir, silebilir ve mevcut görevleri listeleyebilir.

## Özellikler
- Yeni görev ekleme
- Mevcut görevleri görüntüleme
- Görevleri tamamlama
- Görevleri silme

## Gereksinimler
- Python 3.8 veya daha yeni bir sürüm
- `discord.py` kütüphanesi
- SQLite (veya belirtilen başka bir veritabanı)

## Kurulum

1. **Depoyu Klonla**  
   ```sh
   git clone https://github.com/resulpeker/Kodland.git
   cd Kodland
   ```

2. **Gerekli Kütüphaneleri Yükle**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Bot Token'ını Ayarla**  
   - `bot.py` dosyasındaki `bot.run("anahtar")` kısmına kendi Discord bot token'ınızı ekleyin.

4. **Botu Çalıştır**  
   ```sh
   python bot.py
   ```

## Kullanım

### **Komutlar**
- `!add_task <açıklama>` → Yeni bir görev ekler.
- `!show_tasks` → Mevcut görevleri listeler.
- `!complete_task <görev_id>` → Görevi tamamlandı olarak işaretler.
- `!delete_task <görev_id>` → Belirtilen görevi siler.

## Katkıda Bulunma
Katkıda bulunmak için **pull request** gönderebilir veya hata bildiriminde bulunabilirsin.


