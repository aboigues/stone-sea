#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
KPIs de réalisation et de conformité des essais.
Entrées:
  --planning planning.json
  --pv pv_exemples.json
'''
import argparse, json
from pathlib import Path

def jload(p: Path): return json.loads(p.read_text(encoding="utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--planning", required=True)
    ap.add_argument("--pv", required=True)
    args = ap.parse_args()

    plan = jload(Path(args.planning))
    pv = jload(Path(args.pv))
    a_faire = {t["essai_id"]: t["a_realiser"] for t in plan.get("planning", [])}
    faits_par_essai = {}
    oks = 0; kos = 0
    for item in pv.get("pv", []):
        eid = item.get("essai_id")
        faits_par_essai[eid] = faits_par_essai.get(eid, 0) + 1
        if item.get("conformite") == "OK": oks += 1
        elif item.get("conformite") == "KO": kos += 1
    couverture = {eid: f"{min(faits_par_essai.get(eid,0), a_faire.get(eid,0))}/{a_faire.get(eid,0)}" for eid in a_faire}
    print("=== KPIs Essais ===")
    print(f"- Essais planifiés: {len(a_faire)}")
    print(f"- PV: OK={oks} | KO={kos}")
    print("- Couverture par essai:")
    for eid, val in couverture.items():
        print(f"  · {eid}: {val}")

if __name__ == "__main__":
    main()
