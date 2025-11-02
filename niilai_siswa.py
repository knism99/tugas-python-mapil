def main():
    print("=" * 50)
    print("PROGRAM PENGELOLAAN NILAI SISWA")
    print("=" * 50)
    print()
    
    try:
        nilai_a = float(input("Masukkan Nilai A: "))
        nilai_b = float(input("Masukkan Nilai B: "))
        
        if nilai_a < 0 or nilai_a > 100 or nilai_b < 0 or nilai_b > 100:
            print("\nError: Nilai harus berada dalam rentang 0-100!")
            return
        
        rata_rata = (nilai_a + nilai_b) / 2

        if rata_rata >= 75:
            status = "LULUS dengan predikat BAIK"
        elif rata_rata >= 60:
            status = "LULUS"
        else:
            status = "TIDAK LULUS"
        
        print("\n" + "=" * 50)
        print("HASIL PENILAIAN")
        print("=" * 50)
        print(f"Nilai A        : {nilai_a:.2f}")
        print(f"Nilai B        : {nilai_b:.2f}")
        print(f"Rata-rata      : {rata_rata:.2f}")
        print(f"Status         : {status}")
        print("=" * 50)
        
    except ValueError:
        print("\nError: Masukkan angka yang valid!")
        
main()
