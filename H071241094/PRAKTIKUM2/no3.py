nilai = int(input('Masukkan nilai akhir :'))
kehadiran = int(input('Masukkan persentase kehadiran :'))

# if 85 <= nilai <= 100 :
#     if kehadiran >= 75 :
#         print('Lulus dengan predikat A')
# elif 75 <= nilai <= 84 :
#     if kehadiran >= 75 :
#         print('Lulus dengan predikat B') 
# elif 60 <= nilai <= 69 :
#     if kehadiran >= 75 :
#         print('Lulus dengan predikat C')
# elif nilai < 60 :
#     if kehadiran >= 75 :
#         print('Lulus dengan predikat D')
# else :
#     print('Tidak lulus')
if kehadiran >=75 :
    if nilai >=85 :
        predikat = "lulus dengan predikat A"
    elif nilai >=70 :
        predikat = "lulus dengan predikat B"
    elif nilai >=60 :
        predikat = "lulus dengan predikat C"
    else : 
        nilai = int(input("masukan nilai tugas tambahan"))
        if nilai >=70 : 
            predikat = "lulus dengan predikat C"
        else : 
            predikat = "tidak lulus"

else :
     print('Tidak lulus')
print(predikat)