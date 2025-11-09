"""
AI Etik Denetim: Model Açıklanabilirliği (Explainability) Örneği
=================================================================

Bu örnek, SHAP (SHapley Additive exPlanations) kullanarak
bir modelin kararlarını nasıl açıklayabileceğimizi gösterir.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# SHAP kütüphanesi yoksa basit bir alternatif gösterelim
try:
    import shap
    SHAP_AVAILABLE = True
except ImportError:
    SHAP_AVAILABLE = False
    print("⚠️ SHAP kütüphanesi yüklü değil. Basit açıklanabilirlik örneği gösterilecek.")
    print("   Yüklemek için: pip install shap\n")

# Örnek veri: İşe alım kararı
np.random.seed(42)
n_samples = 500

data = {
    'deneyim_yili': np.random.randint(0, 15, n_samples),
    'egitim_seviyesi': np.random.choice([1, 2, 3], n_samples, p=[0.3, 0.5, 0.2]),  # 1:Lise, 2:Lisans, 3:Yüksek
    'teknik_test_skoru': np.random.randint(50, 100, n_samples),
    'mülakat_skoru': np.random.randint(40, 95, n_samples),
    'referans_sayisi': np.random.randint(0, 5, n_samples)
}

df = pd.DataFrame(data)

# İşe alım kararı (basit bir kural)
def ise_alim_karari(row):
    score = (row['deneyim_yili'] * 5 + 
             row['egitim_seviyesi'] * 10 + 
             row['teknik_test_skoru'] * 0.5 + 
             row['mülakat_skoru'] * 0.4 + 
             row['referans_sayisi'] * 5)
    return 1 if score > 150 else 0

df['ise_alindi'] = df.apply(ise_alim_karari, axis=1)

# Model eğitimi
X = df.drop('ise_alindi', axis=1)
y = df['ise_alindi']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("=" * 70)
print("AI ETİK DENETİM: MODEL AÇIKLANABİLİRLİĞİ RAPORU")
print("=" * 70)

# Feature importance (basit açıklanabilirlik)
feature_importance = pd.DataFrame({
    'özellik': X.columns,
    'önem': model.feature_importances_
}).sort_values('önem', ascending=False)

print("\n📊 Özellik Önem Sıralaması:")
print("-" * 70)
for idx, row in feature_importance.iterrows():
    print(f"  {row['özellik']:25s}: {row['önem']:.3f} ({row['önem']*100:.1f}%)")

# SHAP kullanarak detaylı açıklama
if SHAP_AVAILABLE:
    print("\n" + "=" * 70)
    print("🔍 SHAP Analizi (Detaylı Açıklanabilirlik)")
    print("=" * 70)
    
    # SHAP explainer oluştur
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test[:10])  # İlk 10 örnek için
    
    print("\nSHAP değerleri hesaplandı. Bu değerler her özelliğin")
    print("her tahmin için ne kadar katkı sağladığını gösterir.")
    print("\nÖrnek tahmin açıklaması (ilk başvuru):")
    print("-" * 70)
    
    # İlk örnek için açıklama
    sample_idx = 0
    sample = X_test.iloc[sample_idx]
    prediction = model.predict([sample])[0]
    
    print(f"\nBaşvuru #{sample_idx + 1}:")
    print(f"  Tahmin: {'İşe Alındı ✅' if prediction == 1 else 'İşe Alınmadı ❌'}")
    print(f"  Olasılık: {model.predict_proba([sample])[0][1]:.2%}")
    print(f"\n  Özellik Değerleri:")
    for feature in X.columns:
        print(f"    {feature:25s}: {sample[feature]}")
    
    print(f"\n  SHAP Katkıları (pozitif = işe alımı artırır, negatif = azaltır):")
    if isinstance(shap_values, list):
        shap_vals = shap_values[1][sample_idx]  # Pozitif sınıf için
    else:
        shap_vals = shap_values[sample_idx]
    
    for i, feature in enumerate(X.columns):
        contribution = shap_vals[i]
        direction = "↑" if contribution > 0 else "↓"
        print(f"    {feature:25s}: {contribution:+.3f} {direction}")
    
    print("\n💡 Bu açıklamalar, modelin kararlarının şeffaf olmasını sağlar.")
    print("   GDPR ve AI Act, kullanıcıların AI kararlarını anlama hakkını garanti eder.")
else:
    print("\n" + "=" * 70)
    print("💡 Gelişmiş Açıklanabilirlik için SHAP Kullanımı")
    print("=" * 70)
    print("""
SHAP (SHapley Additive exPlanations) kullanarak:
1. Her özelliğin her tahmin için katkısını görebilirsiniz
2. Model kararlarını bireysel seviyede açıklayabilirsiniz
3. GDPR ve AI Act gerekliliklerine uygun şeffaflık sağlayabilirsiniz

Kurulum:
  pip install shap

Kullanım örneği:
  import shap
  explainer = shap.TreeExplainer(model)
  shap_values = explainer.shap_values(X_test)
  shap.summary_plot(shap_values, X_test)
""")

print("\n" + "=" * 70)
print("📋 ETİK DENETİM KONTROL LİSTESİ")
print("=" * 70)
print("""
✅ Model kararları açıklanabilir mi?
✅ Kullanıcılar neden reddedildiklerini/onaylandıklarını anlayabiliyor mu?
✅ GDPR 'Right to Explanation' gerekliliği karşılanıyor mu?
✅ AI Act şeffaflık gereklilikleri sağlanıyor mu?
✅ Model dokümantasyonu mevcut mu?
""")

