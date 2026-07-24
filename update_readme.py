import re
from pathlib import Path

README = Path("README.md")
content = README.read_text(encoding="utf-8")

leetcode_count = 0
gfg_count = 0

section = None

for line in content.splitlines():

    line = line.strip()

    # ----------------------------
    # Detect Sections
    # ----------------------------
    if line == "## 🟨 LeetCode":
        section = "leetcode"
        continue

    if line == "## 🟦 GeeksforGeeks (GFG)":
        section = "gfg"
        continue

    # Any new heading ends current section
    if line.startswith("#") and line not in (
        "## 🟨 LeetCode",
        "## 🟦 GeeksforGeeks (GFG)",
    ):
        section = None

    # ----------------------------
    # Count Table Rows
    # ----------------------------
    if re.match(r"^\|\s*\d+\s*\|", line):
        if section == "leetcode":
            leetcode_count += 1
        elif section == "gfg":
            gfg_count += 1

total = leetcode_count + gfg_count

new_progress = f"""## 📈 Progress

- ✅ Total Problems Solved: **{total}**
- 🟠 LeetCode: **{leetcode_count}**
- 🟢 GeeksforGeeks: **{gfg_count}**
"""

content = re.sub(
    r"## 📈 Progress.*?---",
    new_progress + "\n\n---",
    content,
    flags=re.S,
)

README.write_text(content, encoding="utf-8")

print(f"Updated README: Total={total}, LC={leetcode_count}, GFG={gfg_count}")
