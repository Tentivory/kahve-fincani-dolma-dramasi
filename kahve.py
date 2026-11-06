#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Fincanı Dolma Draması
Dünyanın en yavaş ve en absürt simülasyonu.
"""

import time
import random
import sys

def dramatik_bekle(saniye):
    """Beklerken dramatik yorumlar yapar."""
    yorumlar = [
        "Kahve taneleri uyanıyor...",
        "Su ısınıyor, evren ısınıyor...",
        "Fincan 'doldum' diyor ama yalan söylüyor...",
        "Bürokrasi onayı bekleniyor...",
        "Bir fincan daha, bir hayat daha...",
        "Kahve molası resmi olarak başladı."
    ]
    print(random.choice(yorumlar))
    time.sleep(saniye)

def main():
    print("=" * 50)
    print("KAHVE FINCANI DOLMA DRAMASI BAŞLADI")
    print("=" * 50)
    print("Lütfen oturun. Bu uzun sürecek. \u00c7ok uzun.\n")
    
    doluluk = 0
    while doluluk < 100:
        artis = random.randint(1, 5)
        doluluk = min(doluluk + artis, 100)
        print(f"Fincan doluluk oranı: %{doluluk}")
        dramatik_bekle(random.uniform(0.5, 2.0))
        
        if doluluk == 42:
            print("\n*** GİZLİ MESAJ: 42 sayısı her şeyin cevabıdır. Bürokrasi de öyle. ***\n")
        
        if random.random() < 0.1:
            print("\nKahve döküldü! Baştan başla...\n")
            doluluk = max(0, doluluk - 20)
    
    print("\nFİNCAN DOLDU!")
    print("Ama sen hâlâ kod yazmıyorsun.")
    print("Bir fincan daha?")
    
    # Sonsuz döngüye gir
    while True:
        print("Bir fincan daha içiliyor...")
        time.sleep(3)
        if random.random() < 0.05:
            print("\n[Gizli not: Bu simülasyon aslında bir metafor. Neyin metaforu? Söylemem.]\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nKahve molası iptal edildi. Bürokrasi kazandı.")
        sys.exit(0)
