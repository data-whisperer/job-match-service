"""
Test configuration and fixtures.
"""

import os
import sys
from pathlib import Path

# Add the src directory to the Python path
src_path = str(Path(__file__).parent.parent)
sys.path.insert(0, src_path) 