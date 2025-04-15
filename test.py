import pandas as pd


def excel_to_txt(input_excel, output_txt):
    try:
        # Membaca file Excel
        df = pd.read_excel(input_excel)

        # Membuka file teks untuk ditulis
        with open(output_txt, "w") as file:
            # Menulis header kolom
            file.write("\t".join(df.columns) + "\n")

            # Menulis setiap baris data
            for _, row in df.iterrows():
                file.write("\t".join(map(str, row.values)) + "\n")

        print(f"File TXT berhasil dibuat: {output_txt}")
    except Exception as e:
        print(f"Terjadi salahan: {e}")


# Lokasi file
input_excel = "data.xlsx"  # Pastikan file ini ada di folder proyek
output_txt = "output.txt"

# Menjalankan fungsi
excel_to_txt(input_excel, output_txt)
