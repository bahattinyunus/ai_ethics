# Git dosyalarını ekleme script'i
# Bu script'i repo dizininde çalıştırın

Write-Host "AI Ethics Repo - Git Dosyalarını Ekleme" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

# Mevcut dizini kontrol et
if (-not (Test-Path "readme.md")) {
    Write-Host "HATA: readme.md bulunamadı. Lütfen repo dizininde çalıştırın!" -ForegroundColor Red
    exit 1
}

# Git repo kontrolü
if (-not (Test-Path ".git")) {
    Write-Host "Git repo başlatılıyor..." -ForegroundColor Yellow
    git init
}

# Dosyaları ekle
Write-Host "`nDosyalar git'e ekleniyor..." -ForegroundColor Cyan
git add .gitignore
git add LICENSE
git add readme.md
git add examples/

# Durum kontrolü
Write-Host "`nGit durumu:" -ForegroundColor Cyan
git status --short

Write-Host "`n✅ Dosyalar başarıyla eklendi!" -ForegroundColor Green
Write-Host "`nŞimdi commit yapabilirsiniz:" -ForegroundColor Yellow
Write-Host "  git commit -m 'Add AI ethics code examples and documentation'" -ForegroundColor White
Write-Host "`nSonra push yapın:" -ForegroundColor Yellow
Write-Host "  git push" -ForegroundColor White

