
b = '\033[34;1m'
g = '\033[32;1m'
p = '\033[35;1m'
c = '\033[36;1m'
r = '\033[31;1m'
w = '\033[37;1m'
y = '\033[33;1m'
print b+"                        __________"
print b+"                      .~#########%%;~. "
print b+"                     /############%%;`\ "
print b+"                    /######/~\/~\%%;,;,\ "
print b+"                   |#######\    /;;;;.,.|"
print b+"                   |#########\/%;;;;;.,.|"
print b+"          XX       |##/~~\####%;;;/~~\;,|       XX"
print b+"        XX..X      |#|  o  \##%;/  o  |.|      X..XX"
print b+"      XX.....X     |##\____/##%;\____/.,|     X.....XX"
print b+" XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX"
print b+"X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X"
print b+"X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| "
print b+"X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X"
print b+" X# \.X        @#%,.@                  @#%,.@        X./   #"
print b+"  ##  X          @#%,.@              @#%,.@          X   #"
print b+", "# #X            @#%,.@          @#%,.@            X ##"
print b+"   `###X             @#%,.@      @#%,.@             ####'"
print b+"  . ' ###              @#%.,@  @#%,.@              ###`"
print b+"    .  ;                 @#%.@#%,.@                ;` ' ."
print b+"      '                    @#%,.@                   ,."
print b+"      ` ,                @#%,.@  @@                `"
print b+"                          @@@  @@@  "
print g+"#################################"
print g+ "# Author : 3XP3T4S1             #"
print g+ "# Tools : matematika            #"
print g+ "# Versi : 0.1                   #"
print g+"# Youtube : Jakarta Cyber Army  #"
print g+"# Website : www.gagapilmu.tech  #"
print g+"# Cyber : Jakarta Cyber Army    #"
print g+"# Fanspage : Jakarta Cyber Army #"
print g+"#################################"
def hitung() :
  pil='y'
  while (pil=='y'):
   print("===============================")
   print("       Pilih salah satu       ")
   print("===============================")
   print("1. Hitung Luas Segitiga        ")
   print("2. Hitung Keliling Segitiga    ")
   print("3. Hitung Luas Lingkaran       ")
   print("4. Hitung Keliling Lingkaran   ")
   pil="y"
   pilih=int(raw_input("Masukkan Pilihan : "))
   if pilih==1 :
      a=int(raw_input("masukkan Alas (cm) : "))
      t=int(raw_input("Masukkan TInggi (cm) : "))
      l=0.5*a*t
      print(l)
      pil=raw_input("Apakah ingin menghitung kembali ??? : ")
   elif pilih==2 :
      s1=int(raw_input("masukkan sisi Pertama (cm) : "))
      s2=int(raw_input("Masukkan sisi kedua   (cm) : "))
      s3=int(raw_input("Masukkan sisi ketiga  (cm) : "))
      k=s1+s2+s3
      print(k)
      pil=raw_input("Apakah ingin menghitung kembali ??? : ")
   elif pilih==3 :
      d=int(raw_input("masukkan jari-jari lingkaran (cm) : "))
      ll=3.14*d*d
      print(ll)
      pil=raw_input("Apakah ingin menghitung kembali : ")
   else :
      d=int(raw_input("masukkan jari-jari lingkaran (cm) : "))
      kl=2*3.14*d
      print(kl)
      pil=raw_input("Apakah ingin menghitung kembali : ")
hitung ()