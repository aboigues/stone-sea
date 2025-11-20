#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Fusion de fichiers NC JSON en un registre consolidé.
Entrées:
  --inputs f1.json f2.json ...
  --out registre_nc_merged.json
'''
import argparse, json, uuid
from pathlib import Path
from datetime import datetime

def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    merged = []
    for f in args.inputs:
        obj = load_json(Path(f))
        if isinstance(obj, list):
            merged.extend(obj)
        elif isinstance(obj, dict) and "ncs" in obj:
            merged.extend(obj["ncs"])
        else:
            merged.append(obj)
    # dédoublonnage simple par (exigence_id, description)
    seen = set()
    uniq = []
    for nc in merged:
        key = (nc.get("exigence_id"), (nc.get("description") or "").strip())
        if key not in seen:
            seen.add(key)
            if "id" not in nc or not nc["id"]:
                nc["id"] = "NC-" + uuid.uuid4().hex[:8]
            uniq.append(nc)
    out = {"meta":{"date":datetime.utcnow().isoformat()+"Z","nb_nc":len(uniq)},"ncs":uniq}
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[MERGE] NC uniques: {len(uniq)} → {args.out}")

if __name__ == "__main__":
    main()
