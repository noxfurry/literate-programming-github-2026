
from collections import Counter
import re


def top_words(text: str) -> list[tuple[str, int]]:
    words = re.findall(r"[^\W\d_]+", text.lower(), flags=re.UNICODE)
    counts = Counter(words)

    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:10]

