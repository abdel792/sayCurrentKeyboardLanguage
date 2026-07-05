# sayCurrentKeyboardLanguage

* Yazar(lar): Abdel, Noelia.

# Sunum #

Bu eklenti, nvda-addons e-posta listesindeki bir üyenin talebi üzerine oluşturulmuştur.

Geçerli klavyenin dilini almayı ve seslendirmeyi sağlayan, kısayol tuşu atanmamış bir komut dosyası sunar.

İki kez basıldığında, sistemin varsayılan dilini bildirir.

Bu modülün ilk sürümünde, NVDA'nın yapılandırma dizinine yapıştırılacak basit bir globalPlugin olarak önerilmiş, daha sonra eklentiye dönüştürülmüştür.

## Notlar ##

Klavye dilini bildiren komut dosyasına bir kısayol tuşu atamak için aşağıdaki adımları izleyin:

* "NVDA + N" tuşlarına basarak NVDA menüsünü açın;
* NVDA tercihler menüsüne gidin;
* Ardından "Girdi tuşları" alt menüsüne gidin.
* Daha sonra "Giriş" kategorisini seçin ve sağ ok tuşuyla açın.
* "Kullanılan klavyenin dilini verir, iki kez basıldığında sistemin varsayılan dilini verir" etiketli öğeye gidin;
* Bu işlem tamamlandığında, bir kısayol tuşu eklemek için Alt + A tuşlarına basın ve "NVDA + F4" veya seçtiğiniz başka bir kısayol tuşunu yazın;
* Bunu yaptıktan sonra, yukarı ok tuşuna bir kez basın, "seçtiğiniz kısayol tuşu, tüm düzenler" ifadesini duyacaksınız;
* Enter tuşu ile onaylayın, ardından Tab tuşu ile Tamam seçeneğine gelip Enter tuşuna basın;
* Seçtiğiniz kısayol tuşu artık klavye dilini bildiren komut dosyasını çağıracaktır.

## Uyumluluk ##

* Bu eklenti, 2019.3 ve sonraki NVDA sürümleriyle uyumludur.

## 20240326.0.0 İçin Değişiklikler

* nvda-2024.1 için uyumluluk güncellendi;
* İndirme bağlantısı readme dosyasından kaldırıldı, gelecekteki güncellemeler için indirme bağlantısı artık yalnızca eklenti mağazasından erişilebilir olacaktır.

## 20231229.0.0 İçin Değişiklikler ##

* Yakında nvda-2024.1 ile sunulacak olan talep üzerine konuşma modunu desteklemek için geriye dönük uyumlu bir uygulama eklendi.

## 20230729.0.0 İçin Değişiklikler ##

* Koda flake8 ve mypy kuralları uygulandı;
* Python 3 ile gelen ek açıklamaları desteklemek için desteklenen en düşük NVDA sürümü 2019.3 olarak değiştirildi.
* Kullanıcıların kendi tercih ettikleri kısayol tuşunu seçebilmeleri için klavye dilini bildiren komut dosyasını çağıran "NVDA + F4" kısayol tuşu kaldırıldı.

## 20230607.0.0 İçin Değişiklikler ##

* Aşağıdaki iş akışları eklendi:
 * auto-update-translations - NVDA'nın çeviri sisteminden çevirileri otomatik olarak güncellemek için.
 * release-on-tag..yaml: yeni bir etiket gönderilir gönderilmez eklentiyi derlemek ve yayınlamak için;
 * manual-release.yaml: eklentinin yeni sürümlerini manuel olarak derlemek ve yayınlamak için.
* Çeviriler güncellendi.

## 20230426.0.0 ve Sonraki Sürümler İçin Değişiklikler ##

* • Sürüm numarası, minimum NVDA sürümü ve indirme bağlantısı mağaza kurallarına/gereksinimlerine göre değiştirildi.

## 19.02 Sürümü İçin Değişiklikler ##

* Sürüm numaralandırması YY.AA formatı kullanılarak değiştirildi (2 haneli yıl, ardından bir nokta, ardından 2 haneli ay);
* nvda 2019.1 sürümünden beri mevcut olan yeni eklenti sürüm numaralandırma formatıyla uyumluluk eklendi.

## 1.1 Sürümü İçin Değişiklikler ##

* Eklentinin adı getCurKeyboardLanguage yerine sayCurrentKeyboardLanguage olarak değiştirildi;
* Eklentiye GPL lisansı eklendi;
* getCurKeyboardLanguage komut dosyası "Sistem durumu" kategorisine eklendi;
* Koddaki bazı hatalar düzeltildi.

## 1.0 Sürümü İçin Değişiklikler ##

* İlk sürüm.
