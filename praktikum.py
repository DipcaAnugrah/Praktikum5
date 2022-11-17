no = 0
lanjut = 'y'
nama= []
nim = []
uts = []
uas = []
tugas = []
akhir = []
while lanjut == 'y':
        na = str(input('Nama\t\t: '))
        ni= int(input('NIM\t\t: '))
        ut = int(input('Nilai UTS\t: '))
        us= int(input('nilai uas\t: '))
        tug= int(input('Nilai tugas\t: '))
        akh = float(tug*0.3)+(ut*0.35)+(us*0.35)
        nama.append(na)
        nim.append(ni)
        uts.append(ut)
        uas.append(us)
        tugas.append(tug)
        akhir.append(akh)
        no +=1
        lanjut = input('Tambah data (y/t)? ')
        
print('========================================================')
print('|NO |   Nama   |    NIM    |Tugas| UTS | UAS | Akhir |')
print('========================================================')
for i in range (no):
    print('|',i+1,'| ',nama[i],'  |',nim[i],'|',tugas[i],' | ',uts[i],'| ',uas[i],'|',
    round(akhir[i],2),'|')