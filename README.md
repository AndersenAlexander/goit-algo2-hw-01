# GOIT ALGO2 HW-01 — Divide & Conquer

## Tasks

**Task 1 (Mandatory):** `min_max_divide_conquer(arr) -> (min, max)`

- Recursive divide & conquer
- Time: **O(n)**, stack **O(log n)**

**Task 2\* (Optional):** `quick_select(arr, k) -> value`

- Randomized pivot (Quickselect)
- Average **O(n)**, worst-case **O(n²)** (rare)

## Project Layout

<img width="683" height="334" alt="Screenshot 2025-10-25 211154" src="https://github.com/user-attachments/assets/ae1875fa-8bd2-497a-bbd7-8de2c1902408" />


## Example output
```bash
$ python main.py
Divide & Conquer min/max of [12, -3, 7, 7, 42, 0, 5] -> (-3, 42)
k=1: -3
k=2: 0
k=3: 5
k=4: 7
k=5: 7
k=6: 12
k=7: 42



## How to run (Windows PowerShell)

```powershell
# from repo root
powershell -ExecutionPolicy Bypass -File .\scripts\run_all.ps1
# only tests:
powershell -ExecutionPolicy Bypass -File .\scripts\run_all.ps1 -NoDemo
```

## How to run (manual)

py -3.12 -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
python -m pytest -q
python .\main.py

## Notes

pytest.ini sets pythonpath=. so imports like from src.algorithms ... work out-of-the-box.

For packaging, exclude .venv/, **pycache**/, .pytest_cache/.

## Submission

Zip the project (without .venv/ & caches): HW1_FirstName LastName.zip

Upload the zip to LMS and include the public repository link.


