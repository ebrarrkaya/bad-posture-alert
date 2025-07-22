Kamburluk yani postür bozukluğu, özellikle masa başında çalışırken çoğumuzun farketmeksizin yaptığı bir duruş bozukluğudur. Başlangıçta sadece estetik bir problem gibi görünse de zamanla çok daha ciddi problemlere yol açabilir. Özellikle çocukluk ve ergenlik dönemlerinde gelişir ve omurganın doğal dizilimini bozar. Baş ve boyun öne doğru kayar, omuzlar düşer, sırt bölgesi dışa doğru kavislenir. Bu da baş ağrısı, boyun tutulması, sırt ve bel ağrısı gibi kronik sorunlara zemin hazırlar.



Bu sorundan yola çıkarak görüntü işleme aracılığıyla "MediaPipe Pose" modeli kullanarak kameradan alınan görüntüde insan vücudunu algılayan ve omuz ile bel omuru noktaları arasını ölçüp sürekli olarak kontrol eden bir sistem geliştirdim. 



Sistem, iki nokta arasındaki düşey mesafe hesaplanarak kullanıcının dik durup durmadığını analiz ediyor. Eğer bu mesafe, önceden belirlenmiş eşik değerin altına düşerse, "Duruş bozukluğu algılandı. Lütfen dik durun!" şeklinde bir uyarıyı görsel olarak gösterir ve aynı anda yapay zeka ile oluşturduğum bir sesli uyarı çalıyor. Böylece kullanıcıya hem görsel hem işitsel bir geri bildirim verilmiş oluyor. Ayrıca kişinin kameraya hangi profilden baktığını algılayabiliyor (sağ veya sol) ve değerlendirmeyi ilgili tarafa göre yapıyor.
