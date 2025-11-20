#!/usr/bin/env python3
# cr_json_to_md.py
import json, sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python cr_json_to_md.py cr.json out.md"); sys.exit(2)
    cr = json.load(open(sys.argv[1], encoding="utf-8"))
    meta = cr["meta"]
    md = []
    md.append(f"# CR Chantier — {meta['projet']} — {meta['date']}")
    md.append(f"- Participants: {', '.join(meta['participants'])}")
    if meta.get("meteo"): md.append(f"- Météo: {meta['meteo']}")
    if meta.get("documents_consultes"):
        md.append("- Docs consultés: " + ", ".join(meta["documents_consultes"]))
    md.append("\n## Avancement")
    md.append("- Tâches prévues: " + "; ".join(cr["avancement"]["taches_prevues"]))
    md.append("- Tâches réalisées: " + "; ".join(cr["avancement"]["taches_realisees"]))
    if cr["avancement"]["ecarts"]: md.append("- Écarts: " + "; ".join(cr["avancement"]["ecarts"]))
    md.append("\n## Points")
    for p in cr["points"]:
        md.append(f"- [{p['type']}/{p['gravite']}] {p['id']} — {p['description']}")
        if p.get("liens"): md.append(f"  - Liens: {', '.join(p['liens'])}")
    if cr["photos"]:
        md.append("\n## Photos")
        for ph in cr["photos"]:
            rep = f" ({ph['repere_plan']})" if ph.get("repere_plan") else ""
            com = f" — {ph['commentaire']}" if ph.get("commentaire") else ""
            md.append(f"- {ph['fichier']}{rep}{com}")
    if cr["actions"]:
        md.append("\n## Actions")
        for a in cr["actions"]:
            crit = f" — critère: {a['critere_succes']}" if a.get("critere_succes") else ""
            md.append(f"- {a['qui']} ▶ {a['quoi']} pour {a['quand']}{crit}")
    open(sys.argv[2], "w", encoding="utf-8").write("\n".join(md))
    print(f"[OK] CR exporté -> {sys.argv[2]}")

if __name__ == "__main__":
    main()
