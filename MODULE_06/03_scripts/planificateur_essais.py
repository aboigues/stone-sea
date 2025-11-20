#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Planifie les essais à partir d'un plan de contrôle et d'un quantitatif.
Entrées:
  --plan plan_controle.json
  --quantites mesures_exemple.json
  --out planning.json
'''
import argparse, json, math
from pathlib import Path
from datetime import datetime

def jload(p: Path): return json.loads(p.read_text(encoding="utf-8"))

def compute_nb_samples(rule: dict, quantites: dict) -> int:
    ech = rule.get("echantillonnage", {}) or {}
    mode = ech.get("mode")
    params = (ech.get("parametres") or {})
    if mode == "fixe":
        return int(params.get("nb", 0))
    if mode == "pourcentage":
        pct = float(params.get("pct", 0))
        base = float(quantites.get("base", 0))
        return max(1, math.ceil(base * pct / 100.0)) if base > 0 else 0
    if mode == "surface":
        pas = float(params.get("surface", 0))
        s = float(quantites.get("surface_m2", 0))
        return max(1, math.ceil(s / pas)) if pas > 0 else 0
    if mode == "unites_ouvrage":
        par_vol = float(params.get("par_volume_m3", 0))
        v = float(quantites.get("volume_beton_m3", 0))
        return max(1, math.ceil(v / par_vol)) if par_vol > 0 else 0
    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--quantites", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    plan = jload(Path(args.plan))
    quants = jload(Path(args.quantites))
    essais = plan.get("essais", [])
    planning = []
    for e in essais:
        n = compute_nb_samples(e, quants)
        planning.append({
            "essai_id": e.get("id"),
            "intitule": e.get("intitule"),
            "lot": e.get("lot"),
            "a_realiser": n,
            "frequence": e.get("frequence"),
            "reference": e.get("reference")
        })
    out = {"meta":{"date":datetime.utcnow().isoformat()+"Z","projet":plan.get("meta",{}).get("projet")}, "planning":planning}
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[PLANIF] Essais: {len(essais)} | Tâches générées: {len(planning)} → {args.out}")

if __name__ == "__main__":
    main()
