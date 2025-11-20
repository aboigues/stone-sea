#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
KPIs de conformité sur registre_normatif.json
Entrées:
  --registre registre_normatif.json
'''
import argparse, json
from pathlib import Path

def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registre", required=True)
    args = ap.parse_args()

    reg = load_json(Path(args.registre))
    exigs = reg.get("exigences", [])
    preuves = reg.get("preuves", [])
    ncs = reg.get("ncs", [])

    ok_ids = {p.get("exigence_id") for p in preuves if p.get("resultat")=="OK"}
    applicables = [e for e in exigs]
    taux = round(100*len([e for e in applicables if e.get("id") in ok_ids])/len(applicables),1) if applicables else 0.0

    ncs_ouvertes = [n for n in ncs if n.get("statut")=="ouvert"]
    ncs_majeures_ouvertes = [n for n in ncs_ouvertes if n.get("gravite")=="majeure"]

    print("=== KPIs conformité ===")
    print(f"- Exigences applicables: {len(applicables)}")
    print(f"- Exigences avec ≥1 preuve OK: {len(ok_ids)}")
    print(f"- Taux de conformité (approx.): {taux}%")
    print(f"- NC ouvertes: {len(ncs_ouvertes)}")
    print(f"- NC majeures ouvertes: {len(ncs_majeures_ouvertes)}")

if __name__ == "__main__":
    main()
