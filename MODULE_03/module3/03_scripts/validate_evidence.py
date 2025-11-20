#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation de l'évidence JSON (structure minimale + règles qualité).
Utilisation:
  python validate_evidence.py evidence.json schema.json
"""

import json, sys, re

def load_json(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def check_required_keys(obj, keys, ctx="root"):
    missing = [k for k in keys if k not in obj]
    return (len(missing) == 0, [f"[{ctx}] manquant: {k}" for k in missing])

def percent_traced(constats):
    if not constats: return 0.0
    traced = [c for c in constats if c.get("citations_sources")]
    return 100.0 * len(traced) / max(1, len(constats))

def check_units(constats):
    msgs = []
    for c in constats:
        if c.get("valeur_constatee") is not None and not c.get("unite"):
            msgs.append(f"Constat {c.get('id')} sans unité.")
    return (len(msgs) == 0, msgs)

def validate_schema_min(evidence):
    ok, msgs = True, []

    # Blocs requis
    ok0, m0 = check_required_keys(evidence, ["meta", "references", "constats", "synthese"], "root")
    ok &= ok0; msgs += m0

    # Meta
    if "meta" in evidence:
        ok1, m1 = check_required_keys(
            evidence["meta"],
            ["chantier", "lot", "document_source", "modele_ia", "version_prompts"],
            "meta"
        )
        ok &= ok1; msgs += m1

    # Références
    if "references" in evidence and not isinstance(evidence["references"], list):
        ok = False; msgs.append("[references] doit être une liste.")
    else:
        for i, ref in enumerate(evidence.get("references", [])):
            okr, mr = check_required_keys(ref, ["famille", "numero", "couverture"], f"references[{i}]")
            ok &= okr; msgs += mr

    # Constats
    if "constats" in evidence and not isinstance(evidence["constats"], list):
        ok = False; msgs.append("[constats] doit être une liste.")
    else:
        for i, c in enumerate(evidence.get("constats", [])):
            okc, mc = check_required_keys(c, ["id", "objet", "exigence", "conforme"], f"constats[{i}]")
            ok &= okc; msgs += mc

    # Synthèse
    if "synthese" in evidence:
        oks, ms = check_required_keys(
            evidence["synthese"],
            ["non_conformites_majeures", "non_conformites_mineures", "points_attention", "risque_global", "decision"],
            "synthese"
        )
        ok &= oks; msgs += ms

    return ok, msgs

def main():
    if len(sys.argv) < 3:
        print("Usage: python validate_evidence.py evidence.json schema.json")
        sys.exit(2)

    evidence = load_json(sys.argv[1])
    schema = load_json(sys.argv[2])  # non utilisé pour jsonschema strict afin d'éviter une dépendance externe

    ok, msgs = validate_schema_min(evidence)
    if not ok:
        print("[ERROR] Structure invalide:")
        for m in msgs: print(" -", m)
        sys.exit(2)

    pct = percent_traced(evidence.get("constats", []))
    ok_units, msg_units = check_units(evidence.get("constats", []))

    print(f"[INFO] Constats={len(evidence.get('constats', []))} | Traçabilité={pct:.1f}%")
    if pct < 90.0:
        print("[WARN] Traçabilité < 90% (objectif).")
    if not ok_units:
        print("[ERROR] Unités manquantes:")
        for m in msg_units: print(" -", m)
        sys.exit(2)

    print("[OK] Validation passée.")
    sys.exit(0)

if __name__ == "__main__":
    main()
