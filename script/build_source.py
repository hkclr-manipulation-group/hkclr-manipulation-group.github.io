import yaml
import frontmatter
from pathlib import Path

papers = []

for md in Path("research").glob("*.md"):
    post = frontmatter.load(md)

    # ✅ 跳过非论文页面（如 index.md）
    if post.get("layout") != "paper":
        continue

    if "paper_id" not in post:
        raise RuntimeError(f"❌ Missing paper_id in {md}")

    papers.append({
        "id": post["paper_id"],
        "title": post.get("title"),
        "authors": post.get("authors", []),
        "publisher": post.get("venue"),
        "date": post.get("date"),
        "image": post.get("image"),
        "type": "paper",
        "link": f"https://doi.org/{post['paper_id'].replace('doi:', '')}",
    })

with open("_data/sources.yaml", "w") as f:
    yaml.dump(papers, f, sort_keys=False)
