"""Builds the Skeletons scenario PDF with rst2pdf (cross-platform).

Usage: python generate.py
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "Chrysalis Skeletons scenario 03.txt"
TARGET = HERE / "Chrysalis Skeletons scenario 03.pdf"

subprocess.run([sys.executable, "-m", "rst2pdf.createpdf", str(SOURCE), "-c", "-o", str(TARGET)], check=True)
