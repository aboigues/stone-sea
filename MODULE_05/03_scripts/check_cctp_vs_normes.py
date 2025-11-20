#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Contrôle documentaire CCTP vs exigences normatives (sans dépendances externes).
Heuristique: recherche de mots-clés des exigences dans le CCTP.
Entrées:
  --cctp <fichier.md>
  --exigences <exigences.json>
Sorties:
  STDOUT: résumé
  --out_json rapport.json
  --out_md rapport.md
'''
import argparse, json
from pathlib import Path
from datetime import datetime

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def check(cctp_text: str, exigences: list) -> list:
    c = cctp_text.lower()
    results = []
    for ex in exigences:
        hits = []
        for kw in ex.get("mots_cles", []):
            if kw and kw.lower() in c:
                hits.append(kw)
        statut = "OK" if hits else "KO"
        results.append({
            "exigence_id": ex.get("id"),
            "ref_norme": ex.get("ref_norme"),
            "severite": ex.get("severite"),
            "intitule": ex.get("intitule"),
            "doc_presence": statut,
            "mots_cles_trouves": hits
        })
    return results

def summarize(results):
    total = len(results)
    oks = sum(1 for r in results if r["doc_presence"]=="OK")
    kos = total - oks
    return {"total":total,"OK":oks,"KO":kos,"taux_ok": round(100*oks/total,1) if total>0 else 0.0}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cctp", required=True)
    ap.add_argument("--exigences", required=True)
    ap.add_argument("--out_json", default=None)
    ap.add_argument("--out_md", default=None)
    args = ap.parse_args()

    cctp_text = load_text(Path(args.cctp))
    ex_obj = load_json(Path(args.exigences))
    exigences = ex_obj.get("exigences", ex_obj if isinstance(ex_obj, list) else [])
    results = check(cctp_text, exigences)
    synth = summarize(results)
    print(f"[CCTP] Exigences: {synth['total']} | OK: {synth['OK']} | KO: {synth['KO']} | Taux OK: {synth['taux_ok']}%")

    if args.out_json:
        Path(args.out_json).write_text(
            json.dumps({"meta":{"date":datetime.utcnow().isoformat()+"Z"}, "resultats":results, "synthese":synth}, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
    if args.out_md:
        lines = ["# Rapport contrôle CCTP vs Normes", ""]
        lines.append(f"- Date: {datetime.utcnow().isoformat()}Z")
        lines.append(f"- Exigences: {synth['total']} | OK: {synth['OK']} | KO: {synth['KO']} | Taux OK: {synth['taux_ok']}%")
        lines.append("\n## Détail")
        for r in results:
            mc = ", ".join(r['mots_cles_trouves']) if r['mots_cles_trouves'] else "—"
            lines.append(f"- {r['exigence_id']} ({r['ref_norme']}) — {r['intitule']}: {r['doc_presence']} | mots-clés: {mc}")
        Path(args.out_md).write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
