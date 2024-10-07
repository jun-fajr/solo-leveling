def max_skill_level(N: int, M: int, Ai: list[int], Bi: list[int]) -> int:
    # Membuat pasangan tingkat kemahiran (Ai) dan peningkatan (Bi) untuk tiap lawan
    opponents = list(zip(Ai, Bi))
    
    # Sortir lawan berdasarkan tingkat kemahiran mereka (Ai)
    opponents.sort()
    
    # Simpan tingkat kemahiran awal Juned
    current_skill = M
    
    # Coba kalahkan lawan satu per satu
    for a, b in opponents:
        # Jika Juned bisa mengalahkan lawan (Ai <= current_skill)
        if a <= current_skill:
            # Tambahkan tingkat kemahiran Juned sebanyak Bi
            current_skill += b
        else:
            # Jika tidak bisa mengalahkan lawan, hentikan
            break
    
    # Kembalikan tingkat kemahiran maksimal yang didapatkan Juned
    return current_skill

# Input
if __name__ == "__main__":
    try:
        # Membaca input N
        N = int(input("Masukkan N: "))
        
        # Membaca input M
        M = int(input("Masukkan M: "))
        
        # Membaca array Ai (tingkat kemahiran lawan)
        Ai = []
        for i in range(N):
            ai = int(input(f"Masukkan Ai (tingkat kemahiran lawan) untuk lawan ke-{i + 1}: "))
            Ai.append(ai)
        
        # Membaca array Bi (penambahan kemahiran setelah mengalahkan lawan)
        Bi = []
        for i in range(N):
            bi = int(input(f"Masukkan Bi (penambahan kemahiran setelah menang) untuk lawan ke-{i + 1}: "))
            Bi.append(bi)
        
        # Output hasil
        print("Tingkat kemahiran maksimal:", max_skill_level(N, M, Ai, Bi))
    
    except ValueError:
        print("Masukkan input yang valid")
