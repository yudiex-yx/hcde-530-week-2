import csv
from pathlib import Path

# CSV lives next to this script (stable path even if cwd differs). DictReader
# keys rows by header name so reordering columns does not break positional logic.
filename = Path(__file__).resolve().parent / "demo_responses.csv"
responses = []

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        responses.append(row)


def count_words(response):
    """Whitespace-delimited token count for a single response string.

    Counts are a **length proxy**, not linguistic words: ``split()`` does not
    strip punctuation from tokens (e.g. ``"hello,"`` is one token), and
    hyphenation is unchanged. ``None``, empty, or whitespace-only inputs count
    as zero tokens after stripping.
    """
    if response is None:
        return 0
    text = response.strip()
    if not text:
        return 0
    return len(text.split())


print(f"{'ID':<6} {'Role':<22} {'Words':<6} {'Response (first 60 chars)'}")
print("-" * 75)

word_counts = []

for row in responses:
    participant = row["participant_id"]
    role = row["role"]
    response = row["response"]
    text = response if response is not None else ""

    count = count_words(response)
    word_counts.append(count)

    if len(text) > 60:
        preview = text[:60] + "..."
    else:
        preview = text

    print(f"{participant:<6} {role:<22} {count:<6} {preview}")

print()
print("── Summary ─────────────────────────────────")
print(f"  Total responses : {len(word_counts)}")
if word_counts:
    print(f"  Shortest        : {min(word_counts)} words")
    print(f"  Longest         : {max(word_counts)} words")
    print(f"  Average         : {sum(word_counts) / len(word_counts):.1f} words")
