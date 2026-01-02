def calculate_attendance(series):
    present = 0
    absent = 0

    for val in series:
        val = val.strip().upper()
        if not val:
            continue

        for part in val.split("+"):
            if part == "P":
                present += 1
            elif part == "A":
                absent += 1
            elif part == "P-P":
                present += 2
            elif part == "A-A":
                absent += 2
            elif part == "P-LAB":
                present += 2
            elif part == "A-LAB":
                absent += 2

    total = present + absent
    percent = (present / total) * 100 if total else 0
    return present, total, percent


def required_classes_for_75(present, total):
    if total == 0:
        return 0

    if (present / total) >= 0.75:
        return 0

    x = 0
    while (present + x) / (total + x) < 0.75:
        x += 1

    return x


def predict_attendance(present, total, attend=True):
    """
    attend=True  -> you attend next class
    attend=False -> you skip next class
    """
    if attend:
        present += 1

    total += 1

    return (present / total) * 100 if total else 0
