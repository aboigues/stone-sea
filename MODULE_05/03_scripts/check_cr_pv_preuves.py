#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Contrôle de présence de preuves pour exigences à sévérité 'majeure'.
Entrées:
  --registre <registre.json>
Sortie:
  STDOUT + JSON optionnel
'''
import argparse, json
from pathlib import Path
from datetime import datetime

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registre", required=True)
    ap.add_argument("--out_json", default=None)
    args = ap.parse_args()

    reg = load_json(Path(args.registre))
    exigs = reg.get("exigences", [])
    preuves = reg.get("preuves", [])
    preuves_by_ex = {}
    for p in preuves:
        preuves_by_ex.setdefault(p.get("exigence_id"), []).append(p)
    manquantes = []
    majeures = [e for e in exigs if e.get("severite") == "majeure"]
    for e in majeures:
        if len(preuves_by_ex.get(e.get("id"), [])) == 0:
            manquantes.append(e.get("id"))
    print(f"[PREUVES] Exigences majeures: {len(majeures)} | Avec preuves: {len([eid for eid in preuves_by_ex if eid in [x.get('id') for x in majeures]])} | Manquantes: {len(manquantes)}")
    if manquantes:
        print("Manquantes:", ", ".join(manquantes))
    if args.out_json:
        Path(args.out_json).write_text(
            json.dumps({"date":datetime.utcnow().isoformat()+"Z","exigences_majeures_sans_preuve":manquantes}, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

if __name__ == "__main__":
    main()
