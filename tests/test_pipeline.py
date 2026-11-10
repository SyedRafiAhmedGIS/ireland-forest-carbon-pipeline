import pytest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_imports():
    from crs_handler import reproject_to_utm29n
    from sar_optical_fusion import apply_cloud_masking
    assert True
