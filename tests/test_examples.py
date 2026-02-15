import sys
import os
import pytest
import pandas as pd
import numpy as np

# Add examples directory to path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'examples'))

from bias_detection_example import train_and_evaluate
from dashboard import generate_data

def test_bias_detection_training():
    """Test if bias detection model trains without error."""
    model, X_test, y_test, y_pred, df = train_and_evaluate(n_samples=100, seed=42)
    
    assert model is not None
    assert len(y_pred) == len(y_test)
    assert not df.empty
    assert 'cinsiyet' in df.columns

def test_dashboard_data_generation():
    """Test if dashboard data generation works."""
    df = generate_data(n=50, bias=10)
    
    assert not df.empty
    assert len(df) == 50
    assert 'skor' in df.columns
    assert 'onay' in df.columns
    assert 'cinsiyet' in df.columns
