dipca1=['hello','program','Teknik','Informatika',1]
print('===Akses List Dipca===')
print(dipca1)
print(dipca1[2])
print(dipca1[1:4])
dipca1.pop()
print(dipca1)
print()
print('===Ubah Element Dipca===')
dipca1[3] = 'Manajemen'
print(dipca1)
dipca1[3:] = 'Sipil',2
print(dipca1)
print()
print('===Tambah Element Dipca===')
dipca2 = dipca1[:2]
print(dipca2)
dipca2.append('semester')
dipca2.append(3)
print(dipca1+dipca2)

