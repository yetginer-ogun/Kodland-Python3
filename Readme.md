# Discord Görev Yönetim Botu

Bu proje, küçük ekipler için görevleri yönetmeye yardımcı olan bir Discord botudur. Bot, görev ekleme, silme, görüntüleme ve tamamlama işlevlerini sağlar. Veriler SQLite veritabanında saklanır.

## Özellikler

- Görev ekleme: `!add_task <açıklama>`
- Görev silme: `!delete_task <görev_id>`
- Görevleri gösterme: `!show_tasks`
- Görev tamamlamayı işaretleme: `!complete_task <görev_id>`

## Gereksinimler

- Python 3.9 veya üstü
- `discord` kütüphanesi
- `SQLAlchemy` kütüphanesi
- `sqlite` veritabanı

## Kurulum

1. **Depoyu Klonlayın**

   Projeyi indirmek için aşağıdaki komutu çalıştırın:
   git clone <depo-url>
   cd <depo-adı>

2. **Gereksinimleri Yükleyin**
    Projede ihtiyaç duyulan kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:
    pip install -r requirements.txt

3. **Bot Token'ınızı Ayarlayın**
    Botunuzu çalıştırmak için bir Discord bot token'ına ihtiyacınız var. Botunuzu Discord Developer Portal üzerinden oluşturun ve token'ınızı alın. Token'ınızı boy.py dosyasının sonundaki bot.run() içine ekleyin.

4. **Botu Çalıştırın**
    Aşağıdaki komutu çalıştırarak botu başlatın:
    python bot.py

## Kullanım

1. **Görev Ekleme**
    Yeni bir görev eklemek için:
    !add_task <açıklama>

2. **Görev Silme**
    Bir görevi silmek için görev ID'sini kullanın:
    !delete_task <görev_id>

3. **Görevleri Gösterme**
    Tüm görevleri görüntülemek için:
    !show_tasks

4. **Görev Tamamlama**
    Bir görevi tamamlanmış olarak işaretlemek için:
    !complete_task <görev_id>
