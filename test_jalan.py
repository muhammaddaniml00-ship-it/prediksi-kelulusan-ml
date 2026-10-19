import sys

hasil = []
hasil.append("Python: " + sys.version.split()[0])
try:
    import numpy, pandas, matplotlib, sklearn
    hasil.append("OK: numpy, pandas, matplotlib, scikit-learn SUDAH terinstall")
    hasil.append("numpy " + numpy.__version__)
    hasil.append("pandas " + pandas.__version__)
    hasil.append("sklearn " + sklearn.__version__)
except ImportError as e:
    hasil.append("BELUM terinstall: " + str(e))

with open("hasil_test.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(hasil))
