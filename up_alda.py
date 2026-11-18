print("===== kasir kantin kampus =====")
total = 0

while True:
    print("\n---- daftar makanan ----")
    print("1. ayam penyet - 12.000")
    print("2. nasi gurih - 13.000")
    print("3. mie ayam - 10.000")
    print("4. pecel lele - 20.000")
    print("5. nasi kuning - 15.000")
    print("6. indomie goreng - 12.000")
    print("0. selesai memilih makanan")

    pilihan = int(input("mau beli makanan yang mana? (0-6):"))

    if pilihan == 0:
        break
    elif pilihan == 1:
        total = 12000
        nama_makanan = "ayam penyet"
    elif pilihan == 2:
        total = 13000
        nama_makanan = "nasi gurih"
    elif pilihan == 3:
        total = 12000
        nama_makanan = "indomie goreng"
    elif pilihan == 4:
        total = 20000
        nama_makanan = "pecel lele"
    elif pilihan == 5:
        total = 15000
        nama_makanan = "nasi kuning"
    elif pilihan == 6:
        total = 10000
        nama_makanan = "mie ayam"
    else:
        print("pilihan tidak valid, silahkan pilih lagi")
        continue

    jumlah = int(input(f"mau tambahan makanan ini {nama_makanan}:"))
    subtotal = total * jumlah
    total += subtotal
    print(f"subtotal {nama_makanan} ({jumlah}x):,Rp{subtotal:,}")

    if total > 65600:
        diskon_persen = 20
        total_diskon = total * 0.20
    else:
        diskon_persen = 0
        total_diskon = 0

total_bayar = total - total_diskon

print("\n=========================")
print("      struk pembayaran     ")
print("==========================")
print(f"total belanja : RP{total:,}")
print(f"diskon : {diskon_persen}%")
print(f"potongan : RP{total_diskon:,}")
print("--------------------------")
print(f"total bayar : RP{total_bayar:,}")
print("==========================")
print("        trima kasih      ")
print("==========================")