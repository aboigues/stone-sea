import csv, json, sys
from collections import Counter
from pathlib import Path

def evaluate(results_folder, golden_csv):
    gold = list(csv.DictReader(open(golden_csv)))
    verdicts = []
    for row in gold:
        path = Path(results_folder) / f"{row['doc_id']}.result.json"
        if not path.exists():
            verdicts.append(("manquant", 1))
            continue
        res = json.load(open(path))
        found = [e for e in res.get("exigences", []) if row["exigence"].lower() in e.get("intitule","").lower()]
        if not found:
            verdicts.append(("manquant",1))
            continue
        ex = found[0]
        ok_v = ex.get("decision") == row["verdict_attendu"]
        ok_s = row["source_attendue"] in ex.get("source","")
        ok_e = row["edition_attendue"] in ex.get("edition","")
        verdicts.append(("ok" if (ok_v and ok_s and ok_e) else "ko",1))
    from collections import defaultdict
    agg = defaultdict(int)
    for k,_ in verdicts: agg[k]+=1
    total = sum(agg.values())
    print({"total": total, "ok": agg.get("ok",0), "ko": agg.get("ko",0), "manquant": agg.get("manquant",0)})

if __name__ == "__main__":
    evaluate(sys.argv[1], sys.argv[2])
