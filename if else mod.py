print ("======================================== Operasi Penugasan By Dwi Bakti N ======================================================")
# operasi Penugasan costume

x = int (input ("Masukan Operasi Penugasan Anda Berupa Angka : ")) # penugasan yang di kalikan secara costume
 
x *= int (input ("Masukan Angka Yang ingin Di kali Pada Operasi Penugasan : ")) # nilai yang siap di kalikan

print ("Hasil Yang Keluar Adalah : ",x) # hasil dari perkalian simple

print ("======================================== Operasi Logika By Dwi Bakti N ======================================================")
# operasi logika costume 

logika = int (input ("Masukan Angka LOgika Anda Berupa Angka :")) # masukan Angka Logika Anda Secara Costume

logika2 = int (input ("Masukan Angka LOgika Anda Berupa Angka :")) # masukan yang nanti siap di benarkan pada bilangan logika

masuk = logika or logika2 # 2 itu adalah true yang memilih posisi kanan yang berarti benar atau true
print (masuk)

masuk2 = logika and logika2 # 1 itu adalah false yang memilih posisi kiri yang berti salah atau false
print  (masuk2)

masuk3 = not logika2 # not itu adalah mencari yang salah membentuk suatu logika
print (masuk3)

print ("======================================== Operasi Bitwise By Dwi Bakti N ======================================================")
# operasi bitwise costume 

bitwise = int (input ("Masukan Angka LOgika Anda Berupa Angka : ")) # bitwise yang ingin di jadikan costume berupa angka

bitwise2 = int (input ("Masukan Angka LOgika Anda Berupa Angka : ")) # angka yang siap di binery

masukan_angka_bitwise = bitwise2 & bitwise # ini adalah and dengan variable bitwise dalam bentuk binery
print (masukan_angka_bitwise)

masukan_angka_bitwise2 = bitwise2 | bitwise # ini adalah or dengan variable bitwise dalam bentuk binary
print (masukan_angka_bitwise2)

masukan_angka_bitwise3 = ~bitwise2 # ini adalah not dengan variable bitwise dalam bentuk binary
print (masukan_angka_bitwise3)

masukan_angka_bitwise4 = bitwise2 ^ bitwise # ini adalah xor dengan variable bitwise dalam bentuk binary
print (masukan_angka_bitwise4)

masukan_angka_bitwise5 = bitwise2 >> bitwise # ini adalah right memajukan bit dalam pemograman binary
print (masukan_angka_bitwise5)

masukan_angka_bitwise6 = bitwise2 << bitwise # iniadalah left memundurkan bit dalam pemograman binary
print (masukan_angka_bitwise6)

print ("======================================== Operasi Identitas By Dwi Bakti N ======================================================")
# operasi indentitas costume

identitas = int (input ("Masukan is dan not angka input ini : " )) # identitas costum yang ingin di masukan pada kolum true and false

identitas2 = 1 and ("a") # variable yang salah yang siap untuk di bedakan 

identitas3 = int (input ("Masukan is dan not angka input ini : ")) # identitas costume yang ingin di masukan pada variable identitas pertama yang siap di masukan true and false

print (identitas is identitas3) # membedakan identitas pada kolum benar

print (identitas is identitas2)

print (identitas is not identitas2) # membedakan pada kolum salah

print (identitas3 is not identitas)

print ("======================================== Operasi Keanggotaan By Dwi Bakti N ======================================================")

# operasi ke anggotaan 

tebakan_wibu = ['wibu wangy','wibu bau bawang','wibu akut','luh bukan wibu'] # variable yang ingin di samakan apakah variable tersebut benar atau salah
print ('wibu wangy' in tebakan_wibu  ) # variable yang ingin di masukan benar atau salah pada kolum save data sussscefuly
print ('wibu bau bawang' in tebakan_wibu )
print ('wibu akut'in tebakan_wibu )
print ('luh bukan wibu' not in tebakan_wibu ) # variable yang ingin di masukan salah pada kolum save failed 
