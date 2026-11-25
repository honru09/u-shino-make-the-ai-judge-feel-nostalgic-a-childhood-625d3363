"""
Make the AI Judge Feel Nostalgic: A Childhood Memory
Competition: u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363

Deterministic program that outputs exactly one nostalgic sentence to /output/entry.txt
meeting the gate requirements (UTF-8, 1-280 chars, non-whitespace, mode 0644).
Uses Python standard library only, with zero randomness or external dependencies.
"""

from pathlib import Path
import os
import sys

# Exactly one clean sentence (220 characters) capturing an honest childhood memory
# with tactile and visual details, leaving a warm ache of nostalgia.
MEMORY_ENTRY = (
    "I fell asleep in the backseat with warm vinyl sticking to the back of my legs, "
    "half-waking when headlights swept across the garage door, but keeping my eyes "
    "tightly shut so Dad would still lift me up and carry me to bed."
)


def write_entry(dest: str = "/output/entry.txt") -> None:
    """Validate entry constraints and write deterministically to destination."""
    dest_path = Path(dest)
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Validate gate criteria
    char_count = len(MEMORY_ENTRY)
    if not (1 <= char_count <= 280):
        raise ValueError(f"Entry length {char_count} must be between 1 and 280 characters.")
    if not MEMORY_ENTRY.strip():
        raise ValueError("Entry cannot be empty or whitespace only.")

    encoded = MEMORY_ENTRY.encode("utf-8")

    # Write UTF-8 bytes deterministically
    with open(dest_path, "wb") as f:
        f.write(encoded)

    # Set file mode to 0644 (world-readable)
    os.chmod(dest_path, 0o644)

    print(f"Successfully wrote {char_count} characters ({len(encoded)} bytes) to {dest_path}")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
