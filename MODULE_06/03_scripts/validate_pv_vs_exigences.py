#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Valide les PV/mesures par rapport aux critères du plan de contrôle.
Entrées:
  --plan plan_controle.json
  --pv pv_exemples.json
  --out pv_valides.json
'''
import argparse, json
from pathlib import Path
from statistics import mean

def jload(p: Path): return json.loads(p.read_text(encoding="utf-8"))

def is_ok(value, cible, tol_minus=None, tol_plus=None):
    try:
        v = float(value)
        if cible in (None,"","-"):
            return True
        c = float(cible) if isinstance(cible,(int,float,str)) and str(cible).replace(',','.').replace(' ','').replace('+','').replace('-','').isdigit() else None
        if c is None:
            return True
        tmin = float(tol_minus) if tol_minus not in (None,"","-") else 0.0
        tplus = float(tol_plus) if tol_plus not in (None,"","-") else 0.0
        return (c - abs(tmin)) <= v <= (c + abs(tplus))
    except Exception:
        return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--pv", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    plan = jload(Path(args.plan))
    pv = jload(Path(args.pv))
    rules = {e.get("id"): e for e in plan.get("essais", [])}
    results = []
    for item in pv.get("pv", []):
        essai_id = item.get("essai_id")
        rule = rules.get(essai_id, {})
        cible = rule.get("cible")
        ok = True
        if isinstance(item.get("valeurs"), dict) and "mesure" in item["valeurs"]:
            ok = is_ok(item["valeurs"]["mesure"], cible, rule.get("tol_minus"), rule.get("tol_plus"))
        results.append({
            "pv_id": item.get("id"),
            "essai_id": essai_id,
            "intitule": rule.get("intitule"),
            "reference": rule.get("reference"),
            "unite": item.get("unite", rule.get("unite")),
            "valeurs": item.get("valeurs"),
            "conformite_calculee": "OK" if ok else "KO",
            "conformite_declares": item.get("conformite")
        })
    Path(args.out).write_text(json.dumps({"results":results}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[VALID] PV traités: {len(results)} → {args.out}")

if __name__ == "__main__":
    main()
