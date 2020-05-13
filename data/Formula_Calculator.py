ulang = "Y"
while ulang == "Y" or ulang == "y" or ulang == "YES" or ulang == "yes":
    print("\n","="*16,"\n","KALKULATOR RUMUS"," ","by: Ansofhn","\n","="*16,"\n")         #Judul Kalkulator Rumus
    print("1.Bangun Datar")
    print("2.Bangun Ruang\n")
    pilihan1 = int(input("Apa yang ingin anda hitung? (1/2) : "))       #Input apa yang ingin dihitung
    
    if pilihan1 == (1):
        print("\n","="*13,"\n","BANGUN DATAR","\n","="*13)              #Hasil tampilan input Bangun Datar
        print("1.Luas")
        print("2.Keliling\n")
        pilihan = int(input("Pilih yang mana? (1/2) : "))               
        if pilihan == (1):                                              
            print("\n","="*6,"\n"," LUAS","\n","="*6)                    #Menghitung luas bangun datar
            print("1. Luas Segitiga")
            print("2. Luas Persegi")
            print("3. Luas Persegi Panjang")
            print("4. Luas Jajar Genjang")
            print("5. Luas Belah Ketupat")
            print("6. Luas Layang-layang")
            print("7. Luas Trapesium")
            print("8. Luas Lingkaran\n")
            rumus = int(input("Masukkan rumus yang ingin anda hitung? (1-8) : "))

            #Luas Segitiga
            if rumus == (1):
                print("\n","="*13,"\n","LUAS SEGITIGA","\n","="*13,"\n")
                a = float(input("Masukkan alas(cm): "))
                t = float(input("Masukkan tinggi(cm): "))
                luas = (a*t)/2
                print("Hasilnya adalah :",int(luas),"cm2")
            #Luas Persegi
            elif rumus == (2):
                print("\n","="*13,"\n","LUAS PERSEGI","\n","="*13,"\n")
                s = int(input("Masukkan Sisi(cm): "))
                luas = s*s
                print("Hasilnya adalah :",int(luas),"cm2")     
            #Luas Persegi Panjang  
            elif rumus == (3):
                print("\n","="*20,"\n","LUAS PERSEGI PANJANG","\n","="*20,"\n")
                p = int(input("Masukkan panjang(cm): "))
                l = int(input("Masukkan lebar(cm): "))
                luas = p*l
                print("Hasilnya adalah :",int(luas),"cm2")  
            #luas jajar Genjang 
            elif rumus == (4):
                print("\n","="*18,"\n","LUAS JAJAR GENJANG","\n","="*18,"\n")
                a = int(input("Masukkan alas(cm): "))
                t = int(input("Masukkan tingi(cm): "))
                luas = a*t
                print("Hasilnya adalah :",int(luas),"cm2")  
            #Luas Belah ketupat      
            elif rumus == (5):
                print("\n","="*18,"\n","LUAS BELAH KETUPAT","\n","="*18,"\n")
                d1 = float(input("Masukkan nilai d1(cm): "))
                d2 = float(input("masukkan nilai d2(cm): "))
                luas = (d1*d2)/2
                print("Hasilnya adalah :",int(luas),"cm2")    
            #Luas Layang-layang   
            elif rumus == (6):
                print("\n","="*18,"\n","LUAS LAYANG-LAYANG","\n","="*18,"\n")
                d1 = float(input("Masukkan nilai d1(cm): "))
                d2 = float(input("Masukkan nilai d2(cm): "))
                luas = (d1*d2)/2
                print("Hasilnya adalah :",int(luas),"cm2")   
            #Luas Trapesium        
            elif rumus == (7):
                print("\n","="*15,"\n","LUAS TRAPESIUM","\n","="*15,"\n")
                a = float(input("Masukkan sisi sejajar atas(cm): "))
                b = float(input("Masukkan sisi sejajar bawah(cm): "))
                t = float(input("Masukkan tinggi(cm): "))
                luas = ((a+b)/2)*t
                print("Hasilnya adalah :",int(luas),"cm2")
            #Luas Lingkaran
            elif rumus == (8):
                print("\n","="*15,"\n","LUAS LINGKARAN","\n","="*15,"\n")
                r = float(input("Masukkan jari-jari(cm): "))
                if (r%7) == 0:
                    luas = (22*(r**2))/7
                else :
                    luas = 3.14*(r**2)
                print("Hasilnya adalah :",int(luas),"cm2")
        if pilihan == (2):
            print("\n","="*9,"\n","KELILING","\n","="*9)                    #Menghitung Keliling Bangun Datar
            print("1. Keliling Segitiga")
            print("2. Keliling Persegi")
            print("3. Keliling Persegi Panjang")
            print("4. Keliling Jajar Genjang")
            print("5. Keliling Belah Ketupat")
            print("6. Keliling Layang-layang")
            print("7. Keliling Trapesium")
            print("8. Keliling Lingkaran\n")
            rumus = int(input("Masukkan rumus yang ingin anda hitung? (1-8) : "))

            #Keliling Segitiga
            if rumus == (1):
                print("\n","="*18,"\n","KELILING SEGITIGA","\n","="*18,"\n")
                a = float(input("masukkan sisi a(cm): "))
                b = float(input("Masukkan sisi b(cm): "))
                c = float(input("Masukkan sisi c(cm): "))
                keliling = a+b+c
                print("Hasilnya adalah :",int(keliling),"cm")
            #Keliling Persegi
            elif rumus == (2):
                print("\n","="*16,"\n","KELILING PERSEGI","\n","="*16,"\n")
                s = float(input("Masukkan sisi(cm): "))
                keliling = 4*s
                print("Hasilnya adalah :",int(keliling),"cm")
            #Keliling Persegi Panjang
            elif rumus == (3):
                print("\n","="*24,"\n","KELILING PERSEGI PANJANG","\n","="*24,"\n")
                p = float(input("Masukkan panjang(cm): "))
                l = float(input("Masukkan lebar(cm): "))
                keliling = 2*(p+l)
                print("Hasilnya adalah :",int(keliling),"cm")
            #Keliling Jajar Genjang
            elif rumus == (4):
                print("\n","="*22,"\n","KELILING JAJAR GENJANG","\n","="*22,"\n")
                p = float(input("Masukkan sisi sejajar atas/bawah(cm): "))
                m = float(input("Masukkan sisi sejajar kanan/kiri(cm): "))
                keliling = 2*(p+m)
                print("Hasilnya adalah :",int(keliling),"cm")
            #Keliling Belah Ketupat
            elif rumus == (5):
                print("\n","="*22,"\n","KELILING BELAH KETUPAT","\n","="*22,"\n")
                s = float(input("Masukkan sisi(cm): "))
                keliling = 4*s
                print("Hasilnya adalah :",int(keliling),"cm")
            #Keliling Layang-layang
            elif rumus == (6):
                print("\n","="*22,"\n","KELILING LAYANG-LAYANG","\n","="*22,"\n")
                sp = float(input("Masukkan sisi sejajar atas(cm): "))
                spa = float(input("Masukkan sisi sejajar bawah(cm): "))
                keliling = 2*(sp+spa)
                print("Hasilnya adalah :",int(keliling),"cm")
            #Keliling Trapesium
            elif rumus == (7):
                print("\n","="*18,"\n","KELILING TRAPESIUM","\n","="*18,"\n")
                a = float(input("Masukkan sisi sejajar atas(cm): "))
                b = float(input("Masukkan sisi sejajar bawah(cm): "))
                k = float(input("Masukkan sisi sejajar kanan(cm): "))
                s = float(input("Masukkan sisi sejajar kiri(cm): "))
                keliling = a+b+k+s
                print("Hasilnya adalah :",int(keliling),"cm")
            #Keliling Lingkaran
            elif rumus == (8):
                print("\n","="*18,"\n","KELILING LINGKARAN","\n","="*18,"\n")
                r = int(input("Masukkan jari-jari lingkaran(cm): "))
                if (r%7) == 0:
                    keliling = (2*22*r)/7
                else :
                    keliling = 2*3.14*r
                print("Hasilnya adalah :",int(keliling),"cm")
            
    elif pilihan1 == (2):
        print("\n","="*12,"\n","BANGUN RUANG","\n","="*12,"\n")             #Hasil tampilan input Bangun Ruang
        print("1.Volume")
        print("2.Luas Permukaan\n")
        pilihan = int(input("Pilih yang mana? (1/2): "))

        if pilihan == (1):
            print("\n","="*7,"\n","VOLUME","\n","="*7)                      #Menghitung Volume Bangun ruang
            print("1. Volume Kubus")
            print("2. Volume Balok")
            print("3. Volume Prisma Segitiga")
            print("4. Volume Limas Segitiga")
            print("5. Volume Limas Segi Empat")
            print("6. Volume Tabung")
            print("7. Volume Kerucut")
            print("8. Volume Bola\n")
            rumus = int(input("Masukkan rumus yang ingin anda hitung? (1-8) : "))
            #Volume Kubus
            if rumus == (1):
                print("\n","="*12,"\n","VOLUME KUBUS","\n","="*12,"\n")
                s = int(input("Masukkan sisi(cm): "))
                volume = s**3
                print("Hasilnya adalah :",int(volume),"cm3")
            #Voume Balok
            elif rumus == (2):
                print("\n","="*12,"\n","VOLUME BALOK","\n","="*12,"\n")
                p = int(input("Masukkan panjang(cm): "))
                l = int(input("Masukkan lebar(cm): "))
                t = int(input("Masukkan tinggi(cm): "))
                volume = p*l*t
                print("Hasilnya adalah :",int(volume),"cm3")
            #Volume prisma segitiga
            elif rumus == (3):
                print("\n","="*22,"\n","VOLUME PRISMA SEGITIGA","\n","="*22,"\n")
                a = int(input("Masukkan alas segitiga(cm): "))
                t = int(input("Masukkan tinggi segitiga(cm): "))
                tp = int(input("Masukkan tinggi prisma(cm): "))
                volume = ((a*t)/2)*tp
                print("Hasilnya adalah :",int(volume),"cm3")
            #Volume limas segitiga
            elif rumus == (4):
                print("\n","="*21,"\n","VOLUME LIMAS SEGITIGA","\n","="*21,"\n")
                a = int(input("Masukkan alas segitiga(cm): "))
                t = int(input("Masukkan tinggi segitiga(cm): "))
                tl = int(input("Masukkan tinggi limas(cm): "))
                volume = (((a*t)/2)*t)/3
                print("Hasilnya adalah :",int(volume),"cm3")
            #Volume Limas segi empat
            elif rumus == (5):
                print("\n","="*23,"\n","VOLUME LIMAS SEGI EMPAT","\n","="*23,"\n")
                s = int(input("Masukkan sisi alas limas(cm): "))
                t = int(input("Masukkan tinggi limas(cm): "))
                volume = ((s**2)*t)/3
                print("Hasilnya adalah :",int(volume),"cm3")
            #Volume Tabung
            elif rumus == (6):
                print("\n","="*13,"\n","VOLUME TABUNG","\n","="*13,"\n")
                r = int(input("Masukkan jari-jari(cm): "))
                t = int(input("Masukkan tinggi tabung(cm): "))
                if (r%7) == 0:
                    volume = (22*(r**2)*t)/7
                else :
                    volume = 3.14*(r**2)*t
                print("Hasilnya adalah :",int(volume),"cm3")
            #Volume Kerucut
            elif rumus == (7):
                print("\n","="*14,"\n","VOLUME KERUCUT","\n","="*14,"\n")
                r = int(input("Masukkan jari-jari(cm): "))
                t = int(input("Masukkan tinggi kerucut(cm): "))
                if (r%7) == 0:
                    volume = ((22*(r**2)*t)/7)/3
                else :
                    volume = (3.14*(r**2)*t)/3
                print("Hasilnya adalah :",int(volume),"cm3")
            #Volume bola
            elif rumus == (8):
                print("\n","="*11,"\n","VOLUME BOLA","\n","="*11,"\n")
                r = int(input("Masukkan jari-jari: "))
                if (r%7) == 0:
                    volume = 4/3*((22/7)*(r**3))
                else :
                    volume = 4/3*(3.14*(r**3))
                print("Hasilnya adalah :",int(volume),"cm3")

        if pilihan == (2):
            print("\n","="*14,"\n","LUAS PERMUKAAN","\n","="*14)           #Menghitung luas Permukaan Bangun ruang
            print("1. Luas Permukaan Kubus")
            print("2. Luas Permukaan Balok")
            print("3. Luas Permukaan Prisma Segitiga")
            print("4. Luas Permukaan Limas Segitiga")
            print("5. Luas Permukaan Limas Segi Empat")
            print("6. Luas Permukaan Tabung")
            print("7. Luas Permukaan Kerucut")
            print("8. Luas Permukaan Bola\n")
            rumus = int(input("Masukkan rumus yang ingin anda hitung? (1-8) : "))
            #Luas permukaan kubus
            if rumus == (1):
                print("\n","="*20,"\n","LUAS PERMUKAAN KUBUS","\n","="*20,"\n")
                s = int(input("Masukkan panjang sisi kubus(cm): "))
                Lp = 6*s**2
                print("Hasilnya adalah :",int(Lp),"cm2")
            #luas permukaan balok
            elif rumus == (2):
                print("\n","="*20,"\n","LUAS PERMUKAAN BALOK","\n","="*20,"\n")
                p = int(input("Masukkan Panjang(cm): "))
                l = int(input("Masukkan lebar(cm): "))
                t = int(input("Masukkan tinggi(cm): "))
                Lp = 2*((p*l)+(p*t)+(l*t))
                print("Hasilnya adalah :",int(Lp),"cm2")
            #Luas permukaan prisma segitiga
            elif rumus == (3):
                print("\n","="*30,"\n","LUAS PERMUKAAN PRISMA SEGITIGA","\n","="*30,"\n")
                a = int(input("Masukkan alas segitiga(cm): "))
                t = int(input("Masukkan tinggi segitiga(cm): "))
                s = int(input("Masukkan jumlah nilai sisi alas prisma(cm): "))
                tp = int(input("Masukkan tinggi prisma(cm): "))
                Lp = (2*((a*t)/2))+(s*tp)
                print("Hasilnya adalah :",int(Lp),"cm2")
            #Luas permukaan limas segitiga
            elif rumus == (4):
                print("\n","="*29,"\n","LUAS PERMUKAAN LIMAS SEGITIGA","\n","="*29,"\n")
                a = int(input("Masukkan alas segitiga(cm): "))
                t = int(input("Masukkan tinggi segitiga(cm): "))
                at = int(input("Masukkan alas sisi tegak(cm): "))
                tt = int(input("Masukkan tinggi sisi tegak(cm): "))
                Lp = ((a*t)/2)+(3*((at*tt)/2)) 
                print("Hasilnya adalah :",int(Lp),"cm2")
            #Luas permukaan limas segiempat
            elif rumus == (5):
                print("\n","="*31,"\n","LUAS PERMUKAAN LIMAS SEGI EMPAT","\n","="*31,"\n")
                s = int(input("Masukkan sisi alas limas(cm): "))
                t = int(input("Masukkan tinggi sisi tegak(cm): "))
                Lp = (s*s)+(4*((s*t)/2))
                print("HAsilnya adalah :",int(Lp),"cm2")
            #Luas permukaan Tabung
            elif rumus == (6):
                print("\n","="*21,"\n","LUAS PERMUKAAN TABUNG","\n","="*21,"\n")
                r = int(input("Masukkan jari-jari(cm): "))
                t = int(input("Masukkan tinggi tabung(cm): "))
                if (r%7) == 0:
                    Lp = (2*(22/7*r))*(r+t)
                else :
                    Lp = (2*3.14*r)*(r+t)
                print("Hasilnya adalah :",int(Lp),"cm2")
            #Luas permukaan kerucut
            elif rumus == (7):
                print("\n","="*22,"\n","LUAS PERMUKAAN KERUCUT","\n","="*22,"\n")
                r = int(input("Masukkan jari-jari(cm): "))
                s = int(input("Masukkan nilai garis pelukis kerucut(cm): "))
                if (r%7) == 0:
                    Lp = ((22/7)*r)*(r+s)
                else :
                    Lp = (3.14*r)*(r+s)
                print("Hasilnya adalah :",int(Lp),"cm2")
            #Luas Permukaan Bola
            elif rumus == (8):
                print("\n","="*19,"\n","LUAS PERMUKAAN BOLA","\n","="*19,"\n")
                r = int(input("Masukkan jari-jari(cm): "))
                if (r%7) == 0:
                    Lp = 4*(22/7)*r**2
                else :
                    Lp = 4*3.14*r**2
                print("Hasilnya adalah :",int(Lp),"cm2")

    print ("="*45)
    ulang = input("Apakah anda ingin lanjut menghitung? (Y/N): ")
    if ulang == "N" or ulang == "n" or ulang == "NO" or ulang == "no":
        print("\nProgram Berakhir, Terima kasih sudah menggunakan Kalkulator rumus\n")
        break