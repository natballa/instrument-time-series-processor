import csv
from datetime import datetime
from utils.date_utils import is_business_day
from db.modifier_db import ModifierDB
from processor.base import InstrumentProcessorFactory

db = ModifierDB("modifiers.sqlite")
processors = {}

with open("data/example_input.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) != 3:
            continue

        name, date_str, value_str = row
        try:
            date = datetime.strptime(date_str.strip(), "%d-%b-%Y")
            if not is_business_day(date):
                continue
            value = float(value_str.strip())
            multiplier = db.get_multiplier(name.strip())
            value *= multiplier

            if name not in processors:
                processors[name] = InstrumentProcessorFactory.create(name)
            processors[name].add_entry(date, value)

        except Exception as e:
            print("Error:", row, e)


for name, processor in processors.items():
    print(f"{name}: {processor.result()}")
