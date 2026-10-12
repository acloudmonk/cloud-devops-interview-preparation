# Repository Automation

Validation and content-quality automation live here. Scripts must be safe,
documented, and testable.

## Released-module quality check

Run the following command from the repository root:

```bash
python scripts/check_module_quality.py
```

The check discovers modules marked **Initial release** in the master competency
map and validates their ordered learning path, scenario and drill coverage,
revision material, references, and scored mock interview. It intentionally does
not replace human technical review.
