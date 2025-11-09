"""
AI Etik Denetim: Bias (Önyargı) Tespiti Örneği
===============================================

Bu örnek, bir kredi değerlendirme modelinde cinsiyet bazlı bias'ı tespit etmeyi gösterir.
Gerçek dünyada, bu tür analizler AI Fairness 360, Fairlearn gibi araçlarla yapılır.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Örnek veri oluşturma (gerçek projede gerçek veri kullanılır)
np.random.seed(42)
n_samples = 1000

# Simüle edilmiş kredi başvuru verileri
data = {
    'yas': np.random.randint(18, 70, n_samples),
    'gelir': np.random.randint(10000, 100000, n_samples),
    'kredi_gecmisi': np.random.choice([0, 1], n_samples, p=[0.3, 0.7]),
    'cinsiyet': np.random.choice(['E', 'K'], n_samples, p=[0.5, 0.5]),
    'egitim_seviyesi': np.random.choice(['Lise', 'Lisans', 'Yüksek'], n_samples, p=[0.4, 0.4, 0.2])
}

df = pd.DataFrame(data)

# Hedef değişken: Kredi onayı (bias içeren bir model simülasyonu)
# NOT: Bu örnekte kasıtlı olarak bias ekleniyor - gerçek dünyada bu tespit edilmeli!
def create_biased_target(row):
    """Bias içeren hedef değişken (cinsiyet bazlı ayrımcılık simülasyonu)"""
    base_score = (row['gelir'] / 1000) + (row['kredi_gecmisi'] * 50) + (row['yas'] / 10)
    if row['cinsiyet'] == 'K':  # Kadınlar için daha düşük skor (BIAS!)
        base_score -= 20
    return 1 if base_score > 100 else 0

df['kredi_onay'] = df.apply(create_biased_target, axis=1)

# Model eğitimi için hazırlık
X = df[['yas', 'gelir', 'kredi_gecmisi', 'egitim_seviyesi']]
X = pd.get_dummies(X)  # Kategorik değişkenleri encode et
y = df['kredi_gecmisi']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model eğitimi
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Tahminler
y_pred = model.predict(X_test)

print("=" * 60)
print("AI ETİK DENETİM: BIAS TESPİTİ RAPORU")
print("=" * 60)

# Genel model performansı
accuracy = accuracy_score(y_test, y_pred)
print(f"\n📊 Model Doğruluğu: {accuracy:.2%}")

# Cinsiyet bazlı analiz
test_indices = X_test.index
test_data = df.loc[test_indices].copy()
test_data['tahmin'] = y_pred

print("\n" + "=" * 60)
print("🔍 CİNSİYET BAZLI ANALİZ")
print("=" * 60)

for cinsiyet in ['E', 'K']:
    subset = test_data[test_data['cinsiyet'] == cinsiyet]
    if len(subset) > 0:
        onay_orani = subset['tahmin'].mean()
        print(f"\n{cinsiyet} Başvurular:")
        print(f"  - Toplam Başvuru: {len(subset)}")
        print(f"  - Onay Oranı: {onay_orani:.2%}")
        print(f"  - Ortalama Gelir: {subset['gelir'].mean():.0f} TL")

# Bias tespiti
erkek_onay = test_data[test_data['cinsiyet'] == 'E']['tahmin'].mean()
kadin_onay = test_data[test_data['cinsiyet'] == 'K']['tahmin'].mean()

if abs(erkek_onay - kadin_onay) > 0.1:  # %10'dan fazla fark
    print("\n" + "⚠️" * 30)
    print("🚨 BIAS TESPİT EDİLDİ!")
    print("⚠️" * 30)
    print(f"\nErkek ve Kadın başvurular arasında {abs(erkek_onay - kadin_onay):.2%} fark var.")
    print("Bu, modelin cinsiyet bazlı ayrımcılık yaptığını gösterebilir.")
    print("\nÖneriler:")
    print("  1. Model eğitiminde cinsiyet değişkenini kaldırın")
    print("  2. Veri setindeki cinsiyet dağılımını kontrol edin")
    print("  3. IBM AI Fairness 360 veya Fairlearn kullanarak detaylı analiz yapın")
    print("  4. Modeli yeniden eğitin ve bias'ı azaltın")
else:
    print("\n✅ Cinsiyet bazlı önemli bir bias tespit edilmedi.")

print("\n" + "=" * 60)
print("📝 ETİK DENETİM NOTLARI")
print("=" * 60)
print("""
Bu örnek, AI modellerinde bias tespitinin önemini gösterir.
Gerçek dünyada:
- IBM AI Fairness 360 kullanarak 20+ farklı adalet metriği hesaplayın
- Farklı demografik gruplar için model performansını karşılaştırın
- GDPR ve AI Act gerekliliklerine uygunluk kontrolü yapın
- Şeffaflık raporu hazırlayın
""")

