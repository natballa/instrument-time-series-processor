# Instrument Time Series Processor

📈 Processes time series of financial instruments, applies price modifiers, and computes per-instrument metrics.

---

## What It Does

1. Reads a CSV file of records:  
   `INSTRUMENT_NAME,DATE,VALUE`  
2. Filters out non-business days (weekends).  
3. Looks up a price multiplier in an SQLite table and applies it (defaults to 1.0 if none).  
4. Routes each record to the appropriate processor:
   - **INSTRUMENT1**: overall mean  
   - **INSTRUMENT2**: mean for November 2014  
   - **INSTRUMENT3**: minimum value  
   - **All others**: sum of the 10 most recent values  

---

## Project Structure

```
instrument_stats/
│
├── data/                       # input.csv – your raw data
├── db/
│   ├── init_db.py              # creates and populates modifiers.sqlite and RAW_PRICES
│   └── modifiers.sqlite        # generated on first run
├── processor/                  # per-instrument logic
│   ├── base.py
│   ├── instrument1.py
│   ├── instrument2.py
│   ├── instrument3.py
│   └── generic.py
├── utils/
│   └── date_utils.py           # is_business_day()
├── tests/
│   └── test_processors.py      # pytest test suite
├── main.py                     # orchestration script
└── run.sh                      # initialize DB + run processing
```

---

## Installation & Run

1. **Clone the repo**  
   ```bash
   git clone <your-repo-url>
   cd instrument_stats
   ```

2. **Ensure you have Python 3.8+** (no external dependencies).

3. **Run**  
   ```bash
   sh run.sh
   ```

Results will print to stdout, one line per instrument.

---

## Testing

This project uses **pytest**.

```bash
pip install pytest
pytest
```

Covers all processor types: `instrument1`, `instrument2`, `instrument3`, and `generic`.

---

## Technologies

- Python 3.8+ (built-in `sqlite3`)  
- `csv`, `datetime`, `heapq`  
- SQLite for on-disk storage  

---

## Possible Enhancements

- Stream‐based CSV parser for very large files  
- Configuration via YAML/JSON instead of hard-coded names  
- Export results to a database or visualization dashboard  

---

## Author

**Natalia Balla**  
Test assignment solution for time-series processing.  
