import math

g = 9.8  # m/s²

def calculate_drop_distance(v, h, x_pesawat, x_target):
    # Hitung waktu jatuh
    t = math.sqrt(2 * h / g)
    
    d_horizontal = v * t
    
    jarak_saat_ini = abs(x_target - x_pesawat)
    
    if abs(jarak_saat_ini - d_horizontal) < 0.01:  # Toleransi kecil untuk floating point
        return 0, d_horizontal, "Jatuhkan paket sekarang!"
    
    elif x_pesawat < x_target:
        jarak_perlu = d_horizontal - jarak_saat_ini
        return jarak_perlu, d_horizontal, f"Pesawat perlu maju {jarak_perlu:.2f} meter lagi bruh."
    
    else:
        jarak_perlu = jarak_saat_ini - d_horizontal
        return -jarak_perlu, d_horizontal, f"Pesawat perlu mundur {jarak_perlu:.2f} meter bruh."
    
    if d_horizontal > jarak_saat_ini:
        return None, d_horizontal, "Pesawat sudah terlalu dekat; paket akan jatuh sebelum target."

# Data dummy 
v = 50.0  
h = 100.0  
x_pesawat = 0.0  
x_target = 200.0  

jarak_perlu, d_horizontal, pesan = calculate_drop_distance(v, h, x_pesawat, x_target)
print(f"Jarak horizontal yang akan ditempuh paket: {d_horizontal:.2f} meter")
print(f"Jarak horizontal yang diperlukan pesawat tempuh: {jarak_perlu:.2f} meter" if jarak_perlu is not None else "Tidak dapat dihitung")
print(pesan)
