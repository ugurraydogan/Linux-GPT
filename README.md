Bu proje, OpenAI API'sini kullanarak sorularınızı yanıtlayacak veya görevlerinizi gerçekleştirecek bir Python uygulamasıdır. Proje, güvenli bir şekilde API anahtarınızı yönetmenize ve terminal üzerinden AI ile etkileşim kurmanıza olanak tanır.
2. Gereksinimler

Bu uygulamayı kullanmadan önce aşağıdaki gereksinimlere sahip olmanız gerekir:

    Python 3.7 veya üstü
    pip (Python paket yöneticisi)
    Bir OpenAI API anahtarı

3. Kurulum
Adım 1: Proje Dosyalarını İndirin

Bu depoyu klonlayarak veya indirerek proje dosyalarına erişebilirsiniz:

git clone https://github.com/kullaniciadi/proje-adi.git
cd proje-adi

Adım 2: Sanal Ortam Oluşturun

Sisteminize karışıklık yaratmamak için bir Python sanal ortamı oluşturmanız önerilir:

python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate      # Windows

Adım 3: Bağımlılıkları Yükleyin

requirements.txt dosyasını kullanarak gerekli Python kütüphanelerini yükleyin:

pip install -r requirements.txt

Adım 4: API Anahtarını Ayarlayın

    Proje klasöründe bir .env dosyası oluşturun:

touch .env

Açılan .env dosyasına OpenAI API anahtarınızı şu şekilde ekleyin:

    OPENAI_API_KEY=sk-anahtariniz-buraya

4. Kullanım
Adım 1: Uygulamayı Çalıştırın

Proje klasöründe aşağıdaki komutla uygulamayı başlatabilirsiniz:

python main.py

Adım 2: API ile Etkileşim

    Uygulama çalıştığında terminal üzerinden OpenAI API'ye sorular sorabilir veya komutlar verebilirsiniz.
    Örneğin:

    Soru: Bugün hava durumu nasıl?

    Alınan yanıtlar doğrudan terminalde görüntülenecektir.

5. Örnek Kullanım
Terminal Çıktısı Örneği:

assistant > Merhaba! Size nasıl yardımcı olabilirim?

6. Sıkça Sorulan Sorular
Soru: API anahtarımı nereden alabilirim?

    OpenAI hesabınıza giriş yaparak API Keys sayfasından bir anahtar oluşturabilirsiniz.

Soru: Uygulama çalışmıyor, ne yapmalıyım?

    .env dosyasının doğru yerde ve API anahtarınızı içerdiğinden emin olun.
    Python sürümünüzün 3.7 veya üzeri olduğundan emin olun:

python --version

Gereksinimlerin yüklendiğinden emin olun:

    pip install -r requirements.txt

Sisteminize karışıklık yaratmamak için bir Python sanal ortamı oluşturmanız önerilir

python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate      # Windows

Katkıda bulunmak için ugurraydogan24@icloud.com adresime mail atabilirsiniz.
