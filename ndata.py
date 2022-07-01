import datetime as dt

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
bg = '\033[3m'
underline = '\033[4m'
end = '\033[0m'



arrowr = 20*"→"
arrowl = 20*"←"
arr2 = 31*"→"
arl2 = 31*"←"
sp1 = 15*"—"



nama = input(bold + "Masukan nama anda = " + bold + bg + end)

print(f"{bold}{blue}{arr2}\n{arl2}{end}")

print(f"""\n\n{bold}Silahkan masukan tanggal lahir,
Bulan,
Dan tahun lahir anda.{end}
""")

print(f"{bold}{blue}{arr2}\n{arl2}{end}")


tanggal = int(input(bold + "\n\nTanggal = " + end))
bulan = int(input(bold + "Bulan \t= " + end))
tahun = int(input(bold + "Tahun \t= " + end))

hari_ini = dt.date.today()
print(21*"—")

print(f"{bold}Hari ini = {bg}{hari_ini}{end}")

print(21*"—")


tanggal_lahir = dt.date(tahun,bulan,tanggal)

print(f"\n{bold}Tanggal lahirnya adalah = {green}{tanggal_lahir}{end}")

hari_lahir = f"{tanggal_lahir:%A}"

if hari_lahir == "Monday":
    print(f"{bold}Hari lahirnya adalah = {green}Senin{end}")
    
elif hari_lahir == "Tuesday":
    print(f"{bold}Hari lahirnya adalah = {green}Selasa{end}")
    
elif hari_lahir == "Wednesday":
    print(f"{bold}Hari lahirnya adalah = {green}Rabu{end}")
    
elif hari_lahir == "Thursday":
    print(f"{bold}Hari lahirnya adalah = {green}Kamis{end}")
    
elif hari_lahir == "Friday":
    print(f"{bold}Hari lahirnya adalah = {green}Jum'at{end}")
    
elif hari_lahir == "Saturday":
    print(f"{bold}Hari lahirnya adalah = {green}Sabtu{end}")
    
elif hari_lahir == "Sunday":
    print(f"{bold}Hari lahirnya adalah = {green}Minggu{end}")
    

umur = hari_ini - tanggal_lahir
umur1 = umur // 365

print(f"{bold}Umur anda adalah = {green}{umur1.days} tahun{end}")

print(f"""\n\n{bold}Terimakasih {green}{nama}{end} {bold}telah berkunjung{end}

{bold}{blue}{underline}{sp1}/Akhir dari program\{sp1}{end}
""")