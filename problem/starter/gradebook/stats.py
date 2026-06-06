"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score (rounded to 2 decimals)."""

    scores = {}

    for r in records:
        name = r["name"]
        score = r["score"]
        scores.setdefault(name, []).append(score)

    averages = {}

    for name, marks in scores.items():
        averages[name] = round(sum(marks) / len(marks), 2)

    return averages


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects in the records."""

    return {r["subject"] for r in records}


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""

    averages = average_per_student(records)

    return max(averages.items(), key=lambda x: x[1])


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""

    averages = average_per_student(records)

    return sorted(
        [name for name, avg in averages.items() if avg >= threshold]
    )

