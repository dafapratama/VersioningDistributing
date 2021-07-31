import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://127.0.0.1:8000')

#masukan input barang
#pilihan Barang

print("====================================")
print("                                    ")
print("      Kelompok 3                    ")
print("====================================") 
print("kode barang : harga ")
print("====================================")
print("1. Minyak Goreng : Rp. 3000")
print("2. Gula : Rp. 14000")
print("3. Kopi : Rp. 2000")
print("4. Terigu : Rp. 8000")
print("5. Garam : Rp. 2500")
print("6. Detergen : Rp. 5000")
print("7. Indomie : Rp. 2500")
print("8. Sabun : Rp. 5000")
print("9. Pasta Gigi : Rp. 5000")
print("10. Shampo : Rp. 500")
print("====================================")
print("                                    ")

#kasir
kode_barang = input('Masukkan Kode Barang :')

kode_barang = int(kode_barang)
if proxy.pilihan(kode_barang) == 0 :
    print("Kode Barang Tidak Ada")
else :
    harga = proxy.pilihan(kode_barang)
    jumlah_beli = int(input("Jumlah Barang :"))

    Hasil = proxy.hasil(harga, jumlah_beli)
    print("Total Belanja :Rp.%s" %Hasil)

    bayar = int(input("Masukaan Pembayaran :Rp."))
    if bayar == Hasil:
        print("Uang anda pas, terimakasih sudah berbelanja")
    elif bayar > Hasil:
        kembalian = proxy.kembalian(bayar, Hasil)
        print("Kembalian anda sebesar :Rp.{}".format(kembalian))
    else:
        print("Uang anda tidak cukup")

    print(" Terima Kasih")