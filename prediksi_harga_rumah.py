# M Dani Zainur Rahman
# Prediksi harga rumah menggunakan Linear Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)

# dataset: luas rumah (m2) dan harga (juta Rp)
luas_rumah = np.array([
    30,  45,  50,  60,  65,  70,  75,  80,  85,  90,
    95, 100, 105, 110, 120, 130, 140, 150, 160, 170,
    35,  55,  72,  88, 115, 125, 145, 165, 180, 200
], dtype=float)

# harga ~5 juta/m2 dengan noise acak
harga_rumah = luas_rumah * 5 + np.random.normal(0, 40, len(luas_rumah))

data = pd.DataFrame({
    "Luas (m2)": luas_rumah,
    "Harga (juta Rp)": harga_rumah.round(1),
})

print("Sample data (10 baris pertama):")
print(data.head(10).to_string(index=False))
print(f"\nTotal: {len(data)} data\n")

# scatter plot distribusi data
plt.figure(figsize=(8, 5))
plt.scatter(luas_rumah, harga_rumah, color="steelblue", s=60, edgecolor="black")
plt.title("Luas vs Harga Rumah", fontsize=14)
plt.xlabel("Luas (m2)")
plt.ylabel("Harga (juta Rp)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("grafik_1_data_asli.png", dpi=100)
print("Grafik 1 tersimpan.\n")

# split data 80% training, 20% testing
X = luas_rumah.reshape(-1, 1)
y = harga_rumah

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training : {len(X_train)} data")
print(f"Testing  : {len(X_test)} data\n")

# training model
model = LinearRegression()
model.fit(X_train, y_train)

m = model.coef_[0]
b = model.intercept_

print(f"Persamaan regresi : harga = {m:.2f} * luas + {b:.2f}")
print(f"Koefisien (slope) : {m:.2f} juta Rp per m2\n")

# evaluasi pada data test
y_pred = model.predict(X_test)

hasil = pd.DataFrame({
    "Luas (m2)": X_test.flatten(),
    "Harga Asli": y_test.round(1),
    "Prediksi": y_pred.round(1),
    "Selisih": (y_test - y_pred).round(1),
})
print("Hasil prediksi vs aktual:")
print(hasil.to_string(index=False))
print()

mae = mean_absolute_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)

print(f"MAE : {mae:.2f} juta Rp")
print(f"R2  : {r2:.3f}\n")

# plot garis regresi
plt.figure(figsize=(8, 5))
plt.scatter(X_train, y_train, color="steelblue", s=60,
            edgecolor="black", label="Training")
plt.scatter(X_test, y_test, color="orange", s=60,
            edgecolor="black", marker="^", label="Testing")

x_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
plt.plot(x_line, model.predict(x_line), color="red",
         linewidth=2, label=f"y = {m:.1f}x + {b:.1f}")

plt.title("Linear Regression: Luas vs Harga", fontsize=14)
plt.xlabel("Luas (m2)")
plt.ylabel("Harga (juta Rp)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("grafik_2_garis_model.png", dpi=100)
print("Grafik 2 tersimpan.\n")

# prediksi input baru
input_baru = np.array([[110]])
print(f"Prediksi harga rumah 110 m2 : {model.predict(input_baru)[0]:.1f} juta Rp\n")

# prediksi beberapa ukuran sekaligus
for luas in [75, 100, 150, 250]:
    pred = model.predict([[luas]])[0]
    print(f"  {luas} m2  ->  {pred:.1f} juta Rp")
