def calculate_attendance(series):
    present = 0
    total = 0

    for cell in series:
        # Safety: skip non-strings
        if not isinstance(cell, str):
            continue

        cell = cell.strip().upper()
        if not cell:
            continue

        # Split multiple classes in same day
        parts = cell.replace(" ", "").split("+")

        for part in parts:
            if part == "P":
                present += 1
                total += 1
            elif part == "A":
                total += 1
            # Any other value is safely ignored

    percent = round((present / total) * 100, 2) if total > 0 else 0
    return present, total, percent
