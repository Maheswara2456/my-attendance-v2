from utils.firebase import init_firebase

db = init_firebase()


def load_attendance(user_id):
    """
    Load attendance records for a user
    """
    doc = db.collection("attendance").document(user_id).get()
    if doc.exists:
        data = doc.to_dict()
        return data.get("records", [])
    return []


def save_attendance(user_id, records):
    """
    Save attendance records safely (merge, no overwrite)
    """
    if not isinstance(records, list):
        raise ValueError("Records must be a list")

    db.collection("attendance").document(user_id).set(
        {
            "records": records
        },
        merge=True  # 🔒 SAFE: does not overwrite other fields
    )
