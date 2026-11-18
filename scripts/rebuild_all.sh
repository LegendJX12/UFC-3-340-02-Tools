#!/usr/bin/env bash
# Rebuild the whole database and every generated file, in the right order.
# Run from the repository root:   bash scripts/rebuild_all.sh
# Add --plots to also recompute the generated and digitized plot files (slower).
# LaTeX check needs KaTeX once:   npm install   (uses package.json in the repo root)
set -euo pipefail
cd "$(dirname "$0")/.."
R=reference
DB=$R/ufc_340_02.db

if [[ "${1:-}" == "--plots" ]]; then
  python3 scripts/generate_missing.py --out graphs/generated
  python3 scripts/digitize_figures.py --pdf-root source/pdf --out graphs/generated --checks $R/plots/digitized_checks
fi

python3 scripts/build_db.py --ocr-root ocr --grf-root graphs --index $R/index/UFC_3-340-02_index.xlsx --pdf-root source/pdf --out $DB
python3 scripts/map_grf.py --db $DB --grf-root graphs --csv $R/plots/grf_to_guide.csv
python3 scripts/audit_missing.py --db $DB --csv $R/missing_data.csv
python3 scripts/load_tables.py --db $DB --tables $R/tables
python3 scripts/check_equations.py --db $DB --csv $R/equations/equation_check.csv --issues $R/formulas/formula_issues.csv --review $R/manual/equation_review.csv
python3 scripts/check_equation_lines.py --db $DB --csv $R/equations/equation_lines.csv --review $R/manual/equation_review.csv --status $R/equations/equation_status.csv
python3 scripts/fix_formulas.py --db $DB --csv $R/formulas/formula_fixes.csv --review $R/formulas/formula_review.csv --manual $R/manual/formula_manual_fixes.csv
KATEX_ARG=()
if [[ -d node_modules/katex ]]; then KATEX_ARG=(--katex scripts/katex_check.js); else echo "KaTeX not installed (run: npm install); skipping LaTeX check"; fi
python3 scripts/build_equations.py --db $DB --corrections $R/manual/equation_corrections.csv --csv $R/equations/equations.csv "${KATEX_ARG[@]}"
echo "Rebuild done."
