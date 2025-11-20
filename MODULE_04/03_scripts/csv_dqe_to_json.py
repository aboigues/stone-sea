#!/usr/bin/env python3
# csv_dqe_to_json.py
import csv, json, sys

def row_to_item(r):
    def fnum(v, default=0.0):
        try: return float(v)
        except: return default
    q = fnum(r.get("quantite", 0))
    pu = fnum(r.get("prix_unitaire", 0))
    m = round(q * pu, 2)
    return {
        "code": (r.get("code") or "").strip(),
        "intitule": (r.get("intitule") or "").strip(),
        "description": (r.get("description") or "").strip(),
        "unite": (r.get("unite") or "").strip(),
        "quantite": q,
        "prix_unitaire": pu,
        "montant": m,
        "hypotheses": (r.get("hypotheses") or "").strip(),
        "sources": [s.strip() for s in (r.get("sources") or "").split(";") if s.strip()],
        "liens_normatifs": [s.strip() for s in (r.get("liens_normatifs") or "").split(";") if s.strip()],
        "tags": [t.strip() for t in (r.get("tags") or "").split(";") if t.strip()]
    }

def main():
    if len(sys.argv) < 3:
        print("Usage: python csv_dqe_to_json.py in.csv out.json"); sys.exit(2)
    with open(sys.argv[1], newline="", encoding="utf-8") as f:
        items = [row_to_item(r) for r in csv.DictReader(f)]
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print(f"[OK] {len(items)} postes exportés -> {sys.argv[2]}")

if __name__ == "__main__":
    main()
