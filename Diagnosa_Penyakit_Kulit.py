# Data gejala
gejala = {
    "G1": "Kulit berbintil",
    "G2": "Kulit kemerahan",
    "G3": "Rasa gatal",
    "G4": "Rasa nyeri",
    "G5": "Demam",
    "G6": "Pembengkakan kulit",
    "G7": "Kulit pengelupas",
    "G8": "Benjolan di kulit",
    "G9": "Mata merah",
    "G10": "Kulit kepala berminyak",
    "G11": "Luka di bagian mulut"
}

# Data penyakit
penyakit = {
    "P1": "Alergi",
    "P2": "Bisul",
    "P3": "Cacar Air",
    "P4": "Jerawat",
    "P5": "Kudis",
    "P6": "Keloid",
    "P7": "Campak",
    "P8": "Sariawan",
    "P9": "Ketombe"
}

# Rules IF-THEN
rules = [
    (["G1","G2","G3"], "P1"),
    (["G1","G4","G5"], "P2"),
    (["G1","G3","G5"], "P3"),
    (["G1","G2"], "P4"),
    (["G1","G3","G7"], "P5"),
    (["G3","G8"], "P6"),
    (["G5","G9","G11"], "P7"),
    (["G6","G11"], "P8"),
    (["G3","G10"], "P9")
]

# Tampilkan gejala
print("=== DAFTAR GEJALA ===")
for k, v in gejala.items():
    print(f"{k} : {v}")

# Input user
fakta = [g.strip() for g in input("\nMasukkan gejala (contoh: G1,G3,G5): ").upper().split(",")]

# Forward chaining
print("\n=== PROSES INFERENSI ===")
kandidat = []

for i, (kondisi, hasil) in enumerate(rules, start=1):
    print(f"\nCek Rule R{i}: {kondisi} → {hasil}")

    if all(g in fakta for g in kondisi):
        print("✔ Rule terpenuhi")
        kandidat.append((kondisi, hasil))
    else:
        print("✖ Rule tidak terpenuhi")

# Resolusi konflik
print("\n=== HASIL DIAGNOSIS ===")
if kandidat:
    terbaik = max(kandidat, key=lambda x: len(x[0]))
    print("Diagnosis utama:", penyakit[terbaik[1]])
else:
    print("Tidak ditemukan diagnosis yang sesuai")