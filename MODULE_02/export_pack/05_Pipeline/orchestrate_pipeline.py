import hashlib, json, time
from validators import validate_output, has_required_citations

def hash_file(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def run_case(input_doc, lot, model, schema_path, version_prompts="v2"):
    # 1) Hash entrée
    h = hash_file(input_doc)
    # 2) Appel modèle (placeholder à remplacer par votre API)
    ai_json = {
      "lot": lot,
      "verdict_global": "INCERTAIN",
      "exigences": [],
      "sources_globales": [],
      "journal": {
        "horodatage": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "hash_entree": h,
        "modele": model,
        "version_prompts": version_prompts
      }
    }
    # 3) Validation JSON Schema
    validate_output(ai_json, schema_path)
    # 4) Vérif citations
    if not has_required_citations(ai_json):
        ai_json["verdict_global"] = "NON CONFORME"
    # 5) Sauvegarde
    out = input_doc + ".result.json"
    open(out, "w").write(json.dumps(ai_json, indent=2))
    return out
