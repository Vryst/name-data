
#data = input("Masukan data: ")
#print("data = ",data)

#nomor = input("Masukan Angka: ")
#print("Nomor = ",nomor)

#nama = "ucup"
#data = nama.count("u")
#print("jumlah u di " + nama + " = " + data)

#celah = "ucup".center(12,"—")
#print("hasil = " + celah)

#triple_line = ("""
#ini contoh , apa aja yg disini cuma contoh 
 #         yak, cuma contoh
  #      
#        ....
#        udh oi
#        """)

#print(triple_line)
                                    
          #gitu, yak, gitu lah..
          
  #lanjoeet~~~~
  
import datetime as dt
nama = input("Masukan nama anda = ")
print(f"silahkan masukan tanggal\nbulan \ndan tahun lahir anda")

tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahirnya adalah = {tanggal_lahir}")
print(f"Hari-nya adalah = {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365

print(f"Umur anda adalah :{umur_tahun} tahun")
 
print(5*"="+"SIP"+5*"=")

if nama == "ucup" :
                   print("Ok")
                   print("Keren")
elif nama == "vryst":
    print("Hai")
    print(nama)
elif nama == "sandi":
    print("Widih")
    print(f"hi mr.{nama}")
elif nama == "wahyu":
    print("Halo")
    print(nama)
else:
     print("Au ah gk kenal")
     
print("Akhir dari program")

  #gitu..