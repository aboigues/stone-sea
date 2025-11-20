#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Calcule un échantillonnage pour un essai donné.
Entrées:
  --essai_id BET-RESIST (ou autre)
  --plan plan_controle.json
  --quantites mesures_exemple.json
'''
import argparse, json, math
from pathlib import Path

def jload(p: Path): return json.loads(p.read_text(encoding="utf-8"))

def calc(rule: dict, quants: dict) -> int:
    ech = rule.get("echantillonnage", {}) or {}
    mode = ech.get("mode")
    p = ech.get("parametres") or {}
    if mode == "fixe": return int(p.get("nb",0))
    if mode == "pourcentage":
        base = float(quants.get("base",0)); pct = float(p.get("pct",0))
        return max(1, math.ceil(base*pct/100)) if base>0 else 0
    if mode == "surface":
        s = float(quants.get("surface_m2",0)); pas=float(p.get("surface",0))
        return max(1, math.ceil(s/pas)) if pas>0 else 0
    if mode == "unites_ouvrage":
        v = float(quants.get("volume_beton_m3",0)); par=float(p.get("par_volume_m3",0))
        return max(1, math.ceil(v/par)) if par>0 else 0
    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--essai_id", required=True)
    ap.add_argument("--plan", required=True)
    ap.add_argument("--quantites", required=True)
    args = ap.parse_args()

    plan = jload(Path(args.plan))
    quants = jload(Path(args.quantites))
    d = {e.get("id"):e for e in plan.get("essais",[])}
    rule = d.get(args.essai_id)
    if not rule:
        print("[ERR] Essai introuvable"); return
    n = calc(rule, quants)
    print(f"[ECHANT] {args.essai_id} → {n} prélèvements/mesures")

if __name__ == "__main__":
    main()
