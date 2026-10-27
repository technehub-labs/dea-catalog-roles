#!/usr/bin/env python3
"""Validate role instances against the vendored OpenDEAM role schema."""

import json
import pathlib
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

try:
    from jsonschema import Draft7Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT7
except ImportError:
    sys.exit("jsonschema required: pip install jsonschema")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schemas"
SCHEMA = json.loads((SCHEMA_DIR / "role.schema.json").read_text())


def load_registry() -> Registry:
    resources = []
    for path in SCHEMA_DIR.glob("*.json"):
        contents = json.loads(path.read_text())
        resource = Resource.from_contents(contents, default_specification=DRAFT7)
        resources.append((contents.get("$id", path.name), resource))
    return Registry().with_resources(resources)


def validator_for(schema: dict) -> Draft7Validator:
    return Draft7Validator(schema, registry=load_registry())


def main() -> int:
    entity_files = sorted((ROOT / "entities").rglob("*.yaml"))
    if not entity_files:
        sys.exit("no entity instances found under entities/")

    failures = 0
    for path in entity_files:
        instance = yaml.safe_load(path.read_text())
        validator = validator_for(SCHEMA)
        errors = sorted(
            validator.iter_errors(instance),
            key=lambda e: list(e.absolute_path),
        )
        if errors:
            failures += 1
            for err in errors:
                loc = ".".join(str(p) for p in err.absolute_path) or "<root>"
                print(f"FAIL {path.relative_to(ROOT)} [{loc}]: {err.message}")
        else:
            print(f"OK   {path.relative_to(ROOT)} ({instance.get('id')})")

    if failures:
        sys.exit(f"{failures} entity file(s) failed schema validation")
    print(f"validated {len(entity_files)} role instance(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
