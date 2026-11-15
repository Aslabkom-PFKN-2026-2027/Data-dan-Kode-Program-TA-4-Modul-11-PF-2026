import os
import matplotlib.pyplot as plt
import numpy as np

# 1. PEMBACAAN DATA EKSPERIMEN
try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data_potensial_laplace.csv")
except NameError:
    data_path = "data_potensial_laplace.csv"

if not os.path.exists(data_path):
    raise FileNotFoundError(
        f"Berkas '{data_path}' tidak ditemukan! "
        "Pastikan berkas CSV berada pada direktori yang sama dengan skrip ini."
    )
# Memuat data potensial skalar (matriks 41x41 dalam satuan Volt)
V = np.loadtxt(data_path, delimiter=",")


# 2. DISKRETISASI KISI KOORDINAT SPASIAL
x = np.linspace(-2.0, 2.0, V.shape[1])
y = np.linspace(-2.0, 2.0, V.shape[0])
X, Y = np.meshgrid(x, y)


# 3. INISIALISASI KANVAS MULTI-PANEL 
fig = plt.figure(figsize=(11, 4.8), dpi=100)
# Panel Kiri: Peta Kontur Garis Ekipotensial 2D
ax1 = fig.add_subplot(1, 2, 1)
# Kontur berwarna dengan resolusi halus (29 level interval tegangan)
levels = np.linspace(-35, 35, 29)
cf = ax1.contourf(X, Y, V, levels=levels, cmap="RdBu_r", extend="both")
# Garis isoline ekipotensial dengan anotasi angka tegangan
c_levels = [-25, -15, -8, -4, -1, 0, 1, 4, 8, 15, 25]
c = ax1.contour(X, Y, V, levels=c_levels, colors="black", linewidths=0.6, alpha=0.8)
ax1.clabel(c, inline=True, fmt="%d V", fontsize=7)
# Penanda posisi elektroda muatan dipol listrik
ax1.plot(-0.8, 0.0, "o", color="crimson", markersize=8, markeredgecolor="white", label="Muatan Positif (+1 nC)")
ax1.plot(0.8, 0.0, "o", color="navy", markersize=8, markeredgecolor="white", label="Muatan Negatif (-1 nC)")
# Aksesori grafik panel 2D
ax1.set_title("(a) Peta Garis Ekipotensial 2D", fontsize=10, fontweight="bold", pad=8)
ax1.set_xlabel("Koordinat Posisi x (meter)", fontsize=8.5)
ax1.set_ylabel("Koordinat Posisi y (meter)", fontsize=8.5)
ax1.set_aspect("equal")
ax1.grid(True, linestyle=":", alpha=0.5, color="gray")
ax1.legend(loc="upper right", fontsize=8, framealpha=0.9)
# Bilah warna (colorbar)
cb = fig.colorbar(cf, ax=ax1, fraction=0.046, pad=0.04)
cb.set_label("Potensial Listrik V (Volt)", fontsize=8)

# Panel Kanan: Relief Permukaan Potensial 3D
ax2 = fig.add_subplot(1, 2, 2, projection="3d")
# Permukaan potensial 3D dengan pencahayaan dan gradasi warna RdBu_r
surf = ax2.plot_surface(
    X, Y, V, cmap="RdBu_r", edgecolor="black", linewidth=0.1, alpha=0.92, vmin=-35, vmax=35
)
# Aksesori grafik panel 3D
ax2.set_title("(b) Relief Permukaan Potensial 3D", fontsize=10, fontweight="bold", pad=12)
ax2.set_xlabel("x (m)", fontsize=8, labelpad=4)
ax2.set_ylabel("y (m)", fontsize=8, labelpad=4)
ax2.set_zlabel("Potensial V (Volt)", fontsize=8, labelpad=4)
ax2.view_init(elev=32, azim=-62)
ax2.tick_params(axis="both", which="major", labelsize=7.5)

# Finalisasi Tata Letak
plt.tight_layout()
plt.show()
