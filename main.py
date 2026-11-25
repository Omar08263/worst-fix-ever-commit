# Worst Fix Ever: Funniest Commit Message — program/v1 entry.
# Writes one commit message (1-100 chars) to /output/entry.txt.
# Deterministic: no network, no randomness, no environment reads.
import os

LINE = "fix: the bug only hit left-handed users; it now hits everyone, fairly"

def main() -> None:
    # Python len() counts Unicode code points: the gate counts characters.
    chars = len(LINE)
    if chars < 1 or chars > 100:
        raise SystemExit(f"line is {chars} chars, must be 1-100")
    if LINE.strip() == "":
        raise SystemExit("line must not be only whitespace")
    if "\r" in LINE or "\n" in LINE:
        raise SystemExit("line must be a single line with no line breaks")
    if LINE != LINE.strip():
        raise SystemExit("line must not start or end with whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)
    import stat as _stat
    mode = _stat.S_IMODE(os.stat("/output/entry.txt").st_mode)
    if mode != 0o644:
        raise SystemExit(f"entry.txt mode is {oct(mode)}, must be 0o644")
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != LINE:
        raise SystemExit("read-back mismatch: entry.txt differs from LINE")
    print(f"wrote {chars} chars ({len(LINE.encode('utf-8'))} bytes) to /output/entry.txt")

main()
