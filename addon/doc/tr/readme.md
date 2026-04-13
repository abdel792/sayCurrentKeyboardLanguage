# geçerli Klavye Dilini Söyle

* Yazarlar: Abdel, Noelia;
* [Kararlı Sürümü İndir][1];
* [Geliştirici sürümünü indir][2].

# Sunum #

Bu eklenti, nvda-addons posta listesindeki bir üyenin isteği üzerine oluşturuldu.

Mevcut klavyenin dilini almaya ve vermeye izin veren atanmamış bir komut dosyası sağlar.

İki kez basılırsa, varsayılan sistem dilini bildirir.

Bu modülün ilk versiyonunda, NVDA'nın konfigürasyon dizinine yapıştırmak için basit küreselEklenti olarak önerilmiş, daha sonra Eklentiye dönüştürülmüştür.

## Notlar ##

Klavye dilini duyuran komut dosyasına bir hareket ayarlamak için aşağıdaki adımları izleyin:

* NVDA menüsünü açın, "NVDA + N" ile;
* NVDA'nın Tercihler menüsüne gidin;
* Ardından "Girdi hareketleri" iletişim kutusuna gidin.
* Daha sonra "Girdi" kategorisini seçin ve sağ ok ile açın.
* Etiketli öğeye gittiğinizde "Kullanılan klavyenin dilini duyurur, iki kez basılırsa sistemin varsayılan dilini duyurur" ;
* İşiniz bittiğinde, bir hareket eklemek için Alt + E tuşlarına basın ve "NVDA + F4" veya seçtiğiniz başka bir hareketi yazın;
* Bu yapılırsa, yukarı oka bir kez basın, "seçtiğiniz hareket, tüm düzenler" ifadesini duyarsınız;
* Sırasıyla, Enter  ile doğrulayın ve ardından sekme tuşuyla Tamam'a giderek tekrar Enter'e  basın;
* Seçtiğiniz hareket, klavye dilini duyuran komutu çağırmalıdır.

## Uyumluluk ##

* Bu eklenti, NVDA'nın 2019.3 ve sonrası sürümleriyle uyumludur.

## 20230729.0.0için değişiklikler ##

* Flake8 ve mypy kuralları koda uygulandı;
* Python 3'te tanıtılan ek açıklamaları desteklemek için desteklenen minimum NVDA sürümü 2019.3 olarak değiştirildi.
* Kullanıcıların tercih ettikleri hareketi seçmelerine izin vermek için klavye dilini duyuran komutu çağıran "NVDA + F4" hareketi kaldırıldı.

## 20230607.0.0 için değişiklikler ##

* Aşağıdaki iş akışları eklendi:
 * otomatik Çeviri Güncellemeleri - NVDA'nın çeviri sisteminden çevirileri otomatik olarak güncellemek için.
 * release-on-tag..yaml: yeni bir etiket gönderilir gönderilmez eklentiyi derlemek ve yayınlamak için;
 * manual-release.yaml: Eklentinin yeni sürümlerini el ile derlemek ve yayınlamak için.
* Çeviriler güncellendi.

## Sürüm 20230426.0.0 ve sonrası için değişiklikler ##

* • Mağaza kurallarına/gereksinimlerine göre sürüm numarası, minimum NVDA sürümü ve indirme bağlantısı değiştirildi.

## Sürüm 19.02 için değişiklikler ##

* Sürüm numaralandırılması YY.AA olarak değiştirildi. (Yıl 2 haneli, ardından nokta ve 2 haneli ay);
* Nvda 2019.1'den bu yana ortaya çıkan eklentinin yeni sürüm oluşturma biçimiyle uyumluluk eklendi.

## Sürüm 1.1 için değişiklikler ##

* Eklentinin adı getCurKeyboardLanguage iken sayCurrentKeyboardLanguage olarak değiştirildi;
* Eklentiye GPL lisansı eklendi;
* "Sistem durumu" kategorisine getCurKeyboardLanguage komutu eklendi;
* Koddaki bazı hatalar düzeltildi.

## Sürüm 1.0 için değişiklikler ##

* İlk Sürüm.

[1]: https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage

[2]: https://www.nvaccess.org/addonStore/legacy?file=sayCurrentKeyboardLanguage
