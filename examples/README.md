# 🧪 AI Etik Denetim Pratik Örnekleri

Bu klasör, AI etik denetimi için pratik kod örnekleri içerir.

## 📁 Dosyalar

### 1. `bias_detection_example.py`
**Bias (Önyargı) Tespiti Örneği**

Bir kredi değerlendirme modelinde cinsiyet bazlı bias'ı nasıl tespit edeceğinizi gösterir.

**Kullanım:**
```bash
python bias_detection_example.py
```

**Öğrenecekleriniz:**
- Model bias'ını nasıl tespit edersiniz
- Demografik gruplar arası performans farklarını nasıl analiz edersiniz
- Bias tespit edildiğinde ne yapmalısınız

---

### 2. `model_explainability_example.py`
**Model Açıklanabilirliği Örneği**

SHAP kullanarak model kararlarını nasıl açıklayabileceğinizi gösterir.

**Kullanım:**
```bash
# SHAP ile (önerilir)
pip install shap
python model_explainability_example.py

# SHAP olmadan (basit versiyon)
python model_explainability_example.py
```

**Öğrenecekleriniz:**
- Model kararlarını nasıl açıklarsınız
- GDPR "Right to Explanation" gerekliliğini nasıl karşılarsınız
- SHAP değerlerini nasıl yorumlarsınız

---

### 3. `ethics_checklist.py`
**Etik Denetim Checklist Script'i**

AI projeleriniz için etik denetim checklist'i oluşturmanızı sağlar.

**Kullanım:**
```bash
python ethics_checklist.py
```

**Özellikler:**
- Kapsamlı etik denetim checklist'i
- Otomatik rapor oluşturma
- JSON formatında kayıt
- Risk takibi

**Checklist Kategorileri:**
- ✅ Veri Etiği
- ✅ Model Etiği
- ✅ Uyumluluk (GDPR, KVKK, AI Act)
- ✅ Risk Yönetimi
- ✅ Şeffaflık

---

## 🚀 Kurulum

1. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Örnekleri çalıştırın:
```bash
python bias_detection_example.py
python model_explainability_example.py
python ethics_checklist.py
```

## 📚 Önerilen Araçlar

Bu örnekler temel seviyededir. Gerçek projelerde şu araçları kullanmanız önerilir:

- **IBM AI Fairness 360** - Kapsamlı bias tespiti
- **Fairlearn** - Microsoft'un adil ML aracı
- **SHAP** - Model açıklanabilirliği
- **LIME** - Yerel model açıklanabilirliği
- **What-If Tool** - Google'ın model analiz aracı

## 🔗 İlgili Kaynaklar

- [IBM AI Fairness 360](https://github.com/Trusted-AI/AIF360)
- [Fairlearn](https://fairlearn.org/)
- [SHAP Documentation](https://shap.readthedocs.io/)
- [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

## ⚠️ Not

Bu örnekler eğitim amaçlıdır. Gerçek projelerde:
- Gerçek veri setleri kullanın
- Daha kapsamlı bias analizi yapın
- Yasal danışmanlık alın
- Detaylı dokümantasyon hazırlayın

