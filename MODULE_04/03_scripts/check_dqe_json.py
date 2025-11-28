#!/usr/bin/env python3
# check_dqe_json.py
import json, sys

VALID_UNITS = {"m","m2","m3","u","kg","h","forfait"}

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_dqe_json.py dqe.json"); sys.exit(2)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    errs = []
    for i, it in enumerate(data):
        if it.get("unite") not in VALID_UNITS:
            errs.append(f"[{i}] unité invalide: {it.get('unite')}")
        q = it.get("quantite", 0)
        pu = it.get("prix_unitaire", 0)
        if (q < 0) or (pu < 0):
            errs.append(f"[{i}] quantite/prix négatif")
        m = round(q * pu, 2)
        if abs(m - it.get("montant", 0)) > 0.01:
            errs.append(f"[{i}] montant incohérent, attendu {m}")
        if not it.get("sources"):
            errs.append(f"[{i}] sources manquantes")
        if not it.get("code") or not it.get("intitule"):
            errs.append(f"[{i}] code/intitule manquant")
    if errs:
        print("[ERROR] DQE invalide:"); [print(" -", e) for e in errs]; sys.exit(2)
    print("[OK] DQE validé.")

if __name__ == "__main__":
    main()
