"""
AI Etik Denetim Checklist Script
==================================

Bu script, bir AI projesinin etik açıdan denetlenmesi için
kullanılabilecek bir checklist sağlar.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class AIEthicsChecklist:
    """AI Etik Denetim Checklist Sınıfı"""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.checklist = {
            "veri_etikligi": {
                "veri_toplama_izni": False,
                "veri_gizliligi": False,
                "veri_kalitesi": False,
                "veri_cesitliligi": False,
                "veri_guvenligi": False
            },
            "model_etikligi": {
                "bias_tespiti": False,
                "adil_algoritma": False,
                "aciklanabilirlik": False,
                "performans_esitligi": False,
                "model_dokumantasyonu": False
            },
            "uyumluluk": {
                "gdpr_uyumlu": False,
                "kvkk_uyumlu": False,
                "ai_act_uyumlu": False,
                "sektor_standartlari": False
            },
            "risk_yonetimi": {
                "risk_analizi": False,
                "sosyal_etki_degerlendirmesi": False,
                "guvenlik_testleri": False,
                "acil_durdurma_mekanizmasi": False
            },
            "seffaflik": {
                "kullanici_bilgilendirmesi": False,
                "karar_aciklamasi": False,
                "raporlama": False,
                "dokumantasyon": False
            }
        }
        self.notlar = {}
        self.riskler = []
    
    def kontrol_et(self, kategori: str, alt_kategori: str, durum: bool, notlar: Optional[str] = None):
        """Bir checklist maddesini işaretle"""
        if kategori in self.checklist and alt_kategori in self.checklist[kategori]:
            self.checklist[kategori][alt_kategori] = durum
            if notlar:
                key = f"{kategori}_{alt_kategori}"
                self.notlar[key] = notlar
        else:
            print(f"⚠️ Geçersiz kategori veya alt kategori: {kategori}.{alt_kategori}")
    
    def risk_ekle(self, risk: str, seviye: str = "orta"):
        """Risk kaydı ekle"""
        self.riskler.append({
            "risk": risk,
            "seviye": seviye,
            "tarih": datetime.now().strftime("%Y-%m-%d")
        })
    
    def ilerleme_hesapla(self) -> Dict:
        """Checklist ilerlemesini hesapla"""
        toplam = 0
        tamamlanan = 0
        
        for kategori in self.checklist.values():
            for durum in kategori.values():
                toplam += 1
                if durum:
                    tamamlanan += 1
        
        yuzde = (tamamlanan / toplam * 100) if toplam > 0 else 0
        
        return {
            "tamamlanan": tamamlanan,
            "toplam": toplam,
            "yuzde": yuzde
        }
    
    def rapor_olustur(self) -> str:
        """Etik denetim raporu oluştur"""
        ilerleme = self.ilerleme_hesapla()
        
        rapor = f"""
{'='*70}
AI ETİK DENETİM RAPORU
{'='*70}

Proje Adı: {self.project_name}
Rapor Tarihi: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

İLERLEME DURUMU
{'-'*70}
Tamamlanan: {ilerleme['tamamlanan']}/{ilerleme['toplam']} ({ilerleme['yuzde']:.1f}%)

DETAYLI KONTROL LİSTESİ
{'-'*70}
"""
        
        for kategori, alt_kategoriler in self.checklist.items():
            rapor += f"\n📋 {kategori.upper().replace('_', ' ')}\n"
            for alt_kategori, durum in alt_kategoriler.items():
                durum_ikon = "✅" if durum else "❌"
                rapor += f"  {durum_ikon} {alt_kategori.replace('_', ' ').title()}\n"
                if f"{kategori}_{alt_kategori}" in self.notlar:
                    rapor += f"     Not: {self.notlar[f'{kategori}_{alt_kategori}']}\n"
        
        if self.riskler:
            rapor += f"\n⚠️ TESPİT EDİLEN RİSKLER\n{'-'*70}\n"
            for i, risk in enumerate(self.riskler, 1):
                rapor += f"  {i}. [{risk['seviye'].upper()}] {risk['risk']}\n"
                rapor += f"     Tarih: {risk['tarih']}\n"
        
        rapor += f"\n{'='*70}\n"
        
        # Genel değerlendirme
        if ilerleme['yuzde'] >= 80:
            rapor += "✅ Proje etik denetim açısından iyi durumda.\n"
        elif ilerleme['yuzde'] >= 50:
            rapor += "⚠️ Proje etik denetim açısından orta seviyede. İyileştirme gerekiyor.\n"
        else:
            rapor += "❌ Proje etik denetim açısından yetersiz. Acil iyileştirme gerekiyor.\n"
        
        rapor += f"{'='*70}\n"
        
        return rapor
    
    def json_olarak_kaydet(self, dosya_adi: str):
        """Raporu JSON formatında kaydet"""
        data = {
            "proje_adi": self.project_name,
            "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "checklist": self.checklist,
            "notlar": self.notlar,
            "riskler": self.riskler,
            "ilerleme": self.ilerleme_hesapla()
        }
        
        with open(dosya_adi, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Rapor kaydedildi: {dosya_adi}")


def main():
    """Örnek kullanım"""
    print("AI Etik Denetim Checklist Örneği\n")
    
    # Yeni checklist oluştur
    checklist = AIEthicsChecklist("Kredi Değerlendirme Sistemi")
    
    # Bazı kontrolleri işaretle
    checklist.kontrol_et("veri_etikligi", "veri_toplama_izni", True, 
                        "KVKK uyumlu onay formları kullanılıyor")
    checklist.kontrol_et("veri_etikligi", "veri_gizliligi", True,
                        "Veriler şifrelenmiş ve güvenli saklanıyor")
    checklist.kontrol_et("model_etikligi", "bias_tespiti", True,
                        "AI Fairness 360 ile bias analizi yapıldı")
    checklist.kontrol_et("model_etikligi", "aciklanabilirlik", True,
                        "SHAP kullanılarak model açıklanabilirliği sağlandı")
    checklist.kontrol_et("uyumluluk", "gdpr_uyumlu", True)
    checklist.kontrol_et("uyumluluk", "kvkk_uyumlu", True)
    checklist.kontrol_et("uyumluluk", "ai_act_uyumlu", False,
                        "AI Act kategorisi belirlenmeli")
    checklist.kontrol_et("seffaflik", "kullanici_bilgilendirmesi", True)
    checklist.kontrol_et("seffaflik", "karar_aciklamasi", True)
    
    # Risk ekle
    checklist.risk_ekle("Cinsiyet bazlı bias tespit edildi, düzeltme gerekli", "yuksek")
    checklist.risk_ekle("Model dokümantasyonu eksik", "orta")
    
    # Rapor oluştur
    rapor = checklist.rapor_olustur()
    print(rapor)
    
    # JSON olarak kaydet
    checklist.json_olarak_kaydet("etik_denetim_raporu.json")
    
    print("\n💡 Bu checklist'i kendi projeleriniz için özelleştirebilirsiniz.")


if __name__ == "__main__":
    main()

