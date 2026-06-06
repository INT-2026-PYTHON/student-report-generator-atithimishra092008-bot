"""gradebook.reports — build a printable report from grade records."""

from .stats import (
    average_per_student,
    subjects_offered,
    top_scorer,
    passing_students,
)


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.
    """

    averages = average_per_student(records)
    subjects = sorted(subjects_offered(records))
    top_name, top_avg = top_scorer(records)
    passed = passing_students(records)

    report = []
    report.append("=== Gradebook Report ===")
    report.append(f"Total records: {len(records)}")
    report.append(f"Subjects offered: {', '.join(subjects)}")
    report.append("")
    report.append("Averages:")

    for name in sorted(averages):
        report.append(f"  {name}: {averages[name]}")

    report.append("")
    report.append(f"Top scorer: {top_name} ({top_avg})")
    report.append(
        f"Passing students (>= 60.0): {', '.join(passed)}"
    )

    return "\n".join(report)
    
