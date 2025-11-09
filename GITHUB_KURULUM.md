# 🚀 GitHub'a Yükleme Talimatları

Kodlarınızı GitHub'da görmek için aşağıdaki adımları izleyin:

## Yöntem 1: PowerShell Script (Önerilen)

1. **PowerShell'i açın** ve repo dizinine gidin:
   ```powershell
   cd "C:\github repolarım\ai_ethics"
   ```

2. **Script'i çalıştırın:**
   ```powershell
   .\git_add_files.ps1
   ```

3. **Commit yapın:**
   ```powershell
   git commit -m "Add AI ethics code examples and documentation"
   ```

4. **Push yapın:**
   ```powershell
   git push
   ```

## Yöntem 2: Manuel Git Komutları

Repo dizininde şu komutları çalıştırın:

```bash
# Dosyaları ekle
git add .gitignore LICENSE readme.md examples/

# Durumu kontrol et
git status

# Commit yap
git commit -m "Add AI ethics code examples and documentation"

# Push yap
git push
```

## Yöntem 3: GitHub Desktop

1. **GitHub Desktop**'ı açın
2. Repository'yi seçin: `ai_ethics`
3. Değişiklikler otomatik görünecek
4. Commit mesajı yazın: "Add AI ethics code examples and documentation"
5. "Commit to main" butonuna tıklayın
6. "Push origin" butonuna tıklayın

## 📁 Eklenen Dosyalar

- ✅ `.gitignore` - Git ignore dosyası
- ✅ `LICENSE` - MIT lisansı
- ✅ `readme.md` - Güncellenmiş dokümantasyon
- ✅ `examples/bias_detection_example.py` - Bias tespiti örneği
- ✅ `examples/model_explainability_example.py` - Model açıklanabilirliği örneği
- ✅ `examples/ethics_checklist.py` - Etik denetim checklist'i
- ✅ `examples/requirements.txt` - Gerekli kütüphaneler
- ✅ `examples/README.md` - Örnekler dokümantasyonu

## ⚠️ Sorun Giderme

Eğer "fatal: pathspec did not match any files" hatası alırsanız:

1. Repo dizininde olduğunuzdan emin olun
2. Dosyaların var olduğunu kontrol edin:
   ```powershell
   ls examples/
   ls readme.md
   ls LICENSE
   ```

3. Git repo'sunun başlatıldığından emin olun:
   ```powershell
   git init
   ```

## ✅ Başarı Kontrolü

Push yaptıktan sonra GitHub'da şunları görmelisiniz:

- `examples/` klasörü ve içindeki tüm Python dosyaları
- Güncellenmiş `readme.md`
- `LICENSE` dosyası
- `.gitignore` dosyası

