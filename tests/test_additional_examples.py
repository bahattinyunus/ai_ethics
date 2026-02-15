import sys
import os
import pytest
import pandas as pd

# Add examples directory to path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'examples'))

from ethics_checklist import AIEthicsChecklist
from model_explainability_example import generate_hiring_data, train_model

def test_ethics_checklist_functionality():
    """Test AIEthicsChecklist class functionality."""
    checklist = AIEthicsChecklist("Test Project")
    
    # Test initialization
    assert checklist.project_name == "Test Project"
    assert "veri_etikligi" in checklist.checklist
    
    # Test marking items
    checklist.kontrol_et("veri_etikligi", "veri_gizliligi", True, "Test Note")
    assert checklist.checklist["veri_etikligi"]["veri_gizliligi"] is True
    assert checklist.notlar["veri_etikligi_veri_gizliligi"] == "Test Note"
    
    # Test adding risks
    checklist.risk_ekle("Test Risk", "yuksek")
    assert len(checklist.riskler) == 1
    assert checklist.riskler[0]["risk"] == "Test Risk"
    
    # Test calculation
    progress = checklist.ilerleme_hesapla()
    assert progress["toplam"] > 0
    assert progress["tamamlanan"] == 1
    assert progress["yuzde"] > 0
    
    # Test reporting
    report = checklist.rapor_olustur()
    assert "AI ETİK DENETİM RAPORU" in report
    assert "Test Project" in report

def test_model_explainability_components():
    """Test components of the model explainability example."""
    # Test data generation
    df = generate_hiring_data(n_samples=50)
    assert not df.empty
    assert len(df) == 50
    assert 'ise_alindi' in df.columns
    
    # Test model training
    model, X_test, y_test = train_model(df)
    assert model is not None
    assert len(y_test) > 0
    
    # Verify model performance is reasonable (not random) on training data
    # (Since it's a simple rule-based generation, accuracy should be high)
    assert model.score(X_test, y_test) > 0.5
