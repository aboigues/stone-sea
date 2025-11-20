import json, jsonschema

def validate_output(payload, schema_path):
    schema = json.loads(open(schema_path).read())
    jsonschema.validate(instance=payload, schema=schema)

def has_required_citations(payload):
    if not payload.get("exigences"):
        return False
    for ex in payload["exigences"]:
        if not ex.get("source") or not ex.get("edition"):
            return False
    return True
