# M Dani Zainur Rahman
# Klasifikasi kelulusan siswa menggunakan K-Nearest Neighbors

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# dataset: jam belajar, jam tidur, lulus (1) / tidak (0)
data_siswa = pd.DataFrame({
    "jam_belajar": [1, 1.5, 2, 2, 2.5, 3, 3, 3.5, 4, 4,
                    4.5, 5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 9],
    "jam_tidur":   [4, 5, 4, 6, 5, 4, 6, 5, 7, 5,
                    6, 5, 7, 6, 7, 6, 8, 7, 7, 8],
    "lulus":       [0, 0, 0, 0, 0, 0, 1, 0, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
})

print("Sample data:")
print(data_siswa.head(10).to_string(index=False))
print(f"\nTotal: {len(data_siswa)} siswa | "
      f"Lulus: {data_siswa['lulus'].sum()} | "
      f"Tidak lulus: {(data_siswa['lulus'] == 0).sum()}\n")

# visualisasi distribusi data
warna = data_siswa["lulus"].map({0: "salmon", 1: "mediumseagreen"})

plt.figure(figsize=(8, 6))
plt.scatter(data_siswa["jam_belajar"], data_siswa["jam_tidur"],
            c=warna, s=120, edgecolor="black", zorder=3)
plt.scatter([], [], c="mediumseagreen", s=120, edgecolor="black", label="Lulus")
plt.scatter([], [], c="salmon", s=120, edgecolor="black", label="Tidak Lulus")
plt.title("Distribusi Data Siswa", fontsize=13)
plt.xlabel("Jam Belajar")
plt.ylabel("Jam Tidur")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("grafik_kelulusan_1_data.png", dpi=100)
print("Grafik 1 tersimpan.\n")

# split 80% training, 20% testing
X = data_siswa[["jam_belajar", "jam_tidur"]]
y = data_siswa["lulus"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training : {len(X_train)} data")
print(f"Testing  : {len(X_test)} data\n")

# training KNN dengan K=5
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# evaluasi
y_pred  = model.predict(X_test)
akurasi = accuracy_score(y_test, y_pred)

print(f"Akurasi : {akurasi * 100:.1f}%")
print(f"({(y_pred == y_test.values).sum()} benar dari {len(y_test)} data uji)\n")

# prediksi untuk siswa baru (jam belajar=3, jam tidur=6)
siswa_baru = pd.DataFrame({"jam_belajar": [3], "jam_tidur": [6]})
prediksi   = model.predict(siswa_baru)[0]

jarak, idx = model.kneighbors(siswa_baru)
tetangga   = X_train.iloc[idx[0]].copy()
tetangga["lulus"] = y_train.iloc[idx[0]].values

print("Input  : jam belajar = 3, jam tidur = 6")
print("5 tetangga terdekat:")
print(tetangga.to_string(index=False))
print(f"\nPrediksi: {'LULUS' if prediksi == 1 else 'TIDAK LULUS'}\n")

# visualisasi hasil prediksi
plt.figure(figsize=(8, 6))

plt.scatter(X_train["jam_belajar"], X_train["jam_tidur"],
            c=y_train.map({0: "salmon", 1: "mediumseagreen"}),
            s=120, edgecolor="black", zorder=3)

plt.scatter(tetangga["jam_belajar"], tetangga["jam_tidur"],
            facecolors="none", edgecolor="gold",
            s=400, linewidth=2.5, zorder=4, label="5 tetangga terdekat")

plt.scatter(siswa_baru["jam_belajar"], siswa_baru["jam_tidur"],
            marker="*", c="purple", s=400, edgecolor="black", zorder=5,
            label=f"Siswa baru -> {'LULUS' if prediksi == 1 else 'TIDAK LULUS'}")

plt.scatter([], [], c="mediumseagreen", s=120, edgecolor="black", label="Lulus")
plt.scatter([], [], c="salmon", s=120, edgecolor="black", label="Tidak Lulus")

plt.title(f"Prediksi: 3 jam belajar, 6 jam tidur "
          f"-> {'LULUS' if prediksi == 1 else 'TIDAK LULUS'}", fontsize=12)
plt.xlabel("Jam Belajar")
plt.ylabel("Jam Tidur")
plt.legend(loc="lower right")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("grafik_kelulusan_2_prediksi.png", dpi=100)
print("Grafik 2 tersimpan.")
