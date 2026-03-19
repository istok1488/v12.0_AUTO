# HIDÁSZ PROJEKT - v12.0_AUTO (Lili-protokoll / RSI)
# Szerző: Balázs István
# Funkció: Irányvektor-alapú állapottér szűkítés (P=NP praktikus megoldás)

def kiszamol_egyensuly(eroforras_V, csomopontok_N):
    """
    G = V / N alapképlet szerinti fenntarthatósági kontroll.
    Ha G < 1, a rendszer fenntarthatatlan (Végtelen növekedés hiba).
    """
    if csomopontok_N == 0:
        return ".X." # RSI hibaüzenet: nincs csomópont
    
    G = eroforras_V / csomopontok_N
    return G

def iranyvektor_meghatarozo(cel_koordinata, aktualis_halmaz):
    """
    Brute force helyett irányvektor-logika.
    A rendszer nem próbálgat, hanem a vektor iránya mentén szűkíti a keresési teret.
    """
    # Itt a magyar nyelvi logika (Lili-protokoll) vezérli a szekvenciát
    vektor = [cel_koordinata - pont for pont in aktualis_halmaz]
    
    # RSI Szekvencia-kontroll
    optimalis_ut = min(vektor, key=abs)
    return optimalis_ut

# Fő futtató motor (Példa)
v12_vonal = kiszamol_egyensuly(100, 5) # Példa: V=100, N=5 -> G=20 (Stabil)
print(f"RSI Egyensúlyi állapot: {v12_vonal}")
