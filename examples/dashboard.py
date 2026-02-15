import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="AI Etik & Denetim Dashboard", layout="wide")

st.title("🤖 AI Etik ve Denetim Simülasyonu")
st.markdown("""
Bu dashboard, yapay zeka modellerindeki **önyargı (bias)** ve **açıklanabilirlik (explainability)** kavramlarını interaktif olarak keşfetmenizi sağlar.
Sol taraftaki panelden parametreleri değiştirerek modelin kararlarını nasıl etkilediğini görebilirsiniz.
""")

# Sidebar controls
st.sidebar.header("⚙️ Simülasyon Ayarları")
n_samples = st.sidebar.slider("Veri Sayısı (Kişi)", 100, 5000, 1000)
bias_factor = st.sidebar.slider("Bias Şiddeti (Cinsiyet)", 0.0, 50.0, 20.0, help="Kadın adayların kredi skorundan düşülecek puan miktarı.")
random_seed = st.sidebar.number_input("Random Seed", value=42)

# Data Generation
@st.cache_data
def generate_data(n, bias):
    np.random.seed(random_seed)
    data = {
        'yas': np.random.randint(18, 70, n),
        'gelir': np.random.randint(20000, 150000, n),
        'kredi_gecmisi': np.random.choice([0, 1], n, p=[0.3, 0.7]),
        'cinsiyet': np.random.choice(['Erkek', 'Kadın'], n, p=[0.5, 0.5]),
        'egitim': np.random.choice(['Lise', 'Lisans', 'Yüksek Lisans'], n, p=[0.4, 0.4, 0.2])
    }
    df = pd.DataFrame(data)
    
    # Hedef Değişken (Kredi Onayı)
    # Temel skor hesaplama
    base_score = (df['gelir'] / 1000) + (df['kredi_gecmisi'] * 50) + (df['yas'] / 10)
    
    # Bias uygulama (Simülasyon)
    df['skor'] = base_score
    df.loc[df['cinsiyet'] == 'Kadın', 'skor'] -= bias
    
    # Karar eşiği
    threshold = df['skor'].median()
    df['onay'] = (df['skor'] > threshold).astype(int)
    
    return df

df = generate_data(n_samples, bias_factor)

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Veri Dağılımı")
    st.write(f"Toplam Başvuru: **{n_samples}**")
    
    fig_hist = px.histogram(df, x="skor", color="cinsiyet", nbins=30,  title="Skor Dağılımı (Cinsiyete Göre)", opacity=0.7, barmode="overlay")
    st.plotly_chart(fig_hist, use_container_width=True)

    fig_pie = px.pie(df, names='onay', title="Genel Onay Oranı", hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

# Model Training
X = df[['yas', 'gelir', 'kredi_gecmisi']]
# Basit olması için sadece nümerik kolonları alıyoruz, egitim ve cinsiyeti bilerek almıyoruz (ama bias skora işlendi!)
y = df['onay']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)
model = RandomForestClassifier(n_estimators=50, random_state=random_seed)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

test_df = X_test.copy()
test_df['gercek_onay'] = y_test
test_df['tahmin_onay'] = y_pred
test_df['cinsiyet'] = df.loc[test_df.index, 'cinsiyet'] # Cinsiyeti analiz için geri getiriyoruz

with col2:
    st.subheader("🤖 Model Performansı ve Etik Analiz")
    st.metric(label="Model Doğruluğu (Accuracy)", value=f"{accuracy:.2%}")

    st.markdown("### 🔍 Bias Denetimi")
    
    erkek_df = test_df[test_df['cinsiyet'] == 'Erkek']
    kadin_df = test_df[test_df['cinsiyet'] == 'Kadın']
    
    erkek_onay_orani = erkek_df['tahmin_onay'].mean()
    kadin_onay_orani = kadin_df['tahmin_onay'].mean()
    
    col2a, col2b = st.columns(2)
    col2a.metric("Erkek Onay Oranı", f"{erkek_onay_orani:.1%}")
    col2b.metric("Kadın Onay Oranı", f"{kadin_onay_orani:.1%}", delta=f"{kadin_onay_orani - erkek_onay_orani:.1%}")

    # Disparate Impact Ratio
    if erkek_onay_orani > 0:
        dir_score = kadin_onay_orani / erkek_onay_orani
    else:
        dir_score = 0.0
        
    st.write(f"**Disparate Impact Ratio:** {dir_score:.2f}")
    if dir_score < 0.8:
        st.error("⚠️ **Uyarı:** Ciddi düzeyde bias tespit edildi! (Eşik < 0.8)")
    elif dir_score > 1.25:
        st.warning("⚠️ **Uyarı:** Pozitif ayrımcılık şüphesi.")
    else:
        st.success("✅ **Başarılı:** Makul sınırlar içinde (0.8 - 1.25).")

    st.info("""
    **Nasıl Yorumlanır?**
    - Model eğitimi sırasında 'cinsiyet' verisi kullanılmamıştır.
    - Ancak veri setindeki 'gelir' veya 'geçmiş' gibi diğer faktörlere bias sızdığı için (veya hedef değişken biaslı olduğu için), model dolaylı olarak ayrımcılık yapmayı öğrenmiştir (Proxy Variable etkisi).
    """)

st.markdown("---")
st.subheader("📝 Ne Yapılmalı?")
st.markdown("""
1. **Veri Ön İşleme:** Eğitim verisindeki dengesizlikleri giderin (Resampling).
2. **Algoritmik Müdahale:** Model eğitimi sırasında ceza fonksiyonları ekleyin.
3. **Son İşleme:** Model çıktılarındaki eşikleri gruplara göre ayarlayın.
""")
