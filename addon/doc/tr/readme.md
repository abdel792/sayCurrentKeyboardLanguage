# mevcutKlavyeDİliniSöyle #

* Yazarlar: Abdel, Noelia;
* [Kararlı sürümü
  indir](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)
* [Geliştirme sürümünü
  indir](https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage)

# Sunum #

Bu eklenti, nvda-addons posta listesindeki bir üyenin isteği üzerine
oluşturuldu.

Mevcut klavyenin dilini almayı ve duyurmayı sağlayan hareket tanımlanmamış
bir komut sağlar.

İki kez basılırsa, varsayılan sistem dilini bildirir.

Bu modülün ilk versiyonunda, NVDA'nın konfigürasyon dizinine yapıştırmak
için basit küreselEklenti olarak önerilmiş, daha sonra Eklentiye
dönüştürülmüştür.

## Notlar ##

Klavye dilini duyuran komut dosyasına bir hareket ayarlamak için aşağıdaki
adımları izleyin:

* NVDA menüsünü açın, "NVDA + N" ile;
* NVDA'nın tercihler menüsüne gidin, T ile;
* Ardından "Girdi hareketleri" iletişim kutusuna gidin.
* Daha sonra "Girdi" kategorisini seçin ve sağ ok ile açın.
* Etiketli öğeye gittiğinizde "Kullanılan klavyenin dilini duyurur, iki kez
  basılırsa sistemin varsayılan dilini duyurur" ;
* İşiniz bittiğinde, bir hareket eklemek için Alt + E tuşlarına basın ve
  "NVDA + F4" veya seçtiğiniz başka bir hareketi yazın;
* Bu yapılırsa, yukarı oka bir kez basın, "seçtiğiniz hareket, tüm düzenler"
  ifadesini duyarsınız;
* Sırasıyla, Enter  ile doğrulayın ve ardından sekme tuşuyla Tamam'a giderek
  tekrar Enter'e  basın;
* Seçtiğiniz hareket, klavye dilini duyuran komutu çağırmalıdır.

## Uyumluluk ##

* Bu eklenti, NVDA'nın 2019.3 ve sonrası sürümleriyle uyumludur.

## 20230729.0.0 için değişiklikler ##

* Flake8 ve mypy kuralları koda uygulandı;
* Python 3'te tanıtılan ek açıklamaları desteklemek için desteklenen minimum
  NVDA sürümü 2019.3 olarak değiştirildi.
* Kullanıcıların tercih ettikleri hareketi seçmelerine izin vermek için
  klavye dilini duyuran komutu çağıran "NVDA + F4" hareketi kaldırıldı.

## 20230426.0.0 ve sonraki sürümler için değişiklikler##

* Mağaza kurallarına/gereksinimlerine göre sürüm numarası, minimum NVDA
  sürümü ve indirme bağlantısı değiştirildi.

## 19.02 sürümü için değişiklikler ##

* Sürüm numaralandırılması YY.AA olarak değiştirildi. (Yıl 2 haneli,
  ardından nokta ve 2 haneli ay);
* Nvda 2019.1'den bu yana ortaya çıkan eklentinin yeni sürüm oluşturma
  biçimiyle uyumluluk eklendi.

## 1.1 sürümü için değişiklikler ##

* Eklentinin adı getCurKeyboardLanguage iken sayCurrentKeyboardLanguage
  olarak değiştirildi;
* Eklentiye GPL lisansı eklendi;
* "Sistem durumu" kategorisine getCurKeyboardLanguage komutu eklendi;
* Koddaki bazı hatalar düzeltildi.

## 1.0 sürümü için değişiklikler ##

* İlk Sürüm.

[[!tag dev stable]]
