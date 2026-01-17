import yaml
import frontmatter
from pathlib import Path


def pick_cover(paper_dir: Path) -> str:
    # 1️⃣ photo.*
    for ext in ("png", "jpg", "jpeg"):
        photo = paper_dir / f"photo.{ext}"
        if photo.exists():
            return "/" + photo.as_posix()

    # 2️⃣ images/*.png (first one)
    img_dir = paper_dir / "images"
    if img_dir.exists():
        for img in sorted(img_dir.glob("*.png")):
            return "/" + img.as_posix()

    # 3️⃣ global fallback
    return "/research/photo.jpg"


papers = []

for md in Path("research").rglob("index.md"):
    post = frontmatter.load(md)

    if post.get("layout") != "paper":
        continue

    if "paper_id" not in post:
        raise RuntimeError(f"❌ Missing paper_id in {md}")

    paper_dir = md.parent  # research/<paper-name>

    papers.append({
        "id": post["paper_id"],
        "title": post.get("title"),
        "authors": post.get("authors", []),
        "publisher": post.get("venue"),
        "date": post.get("date"),
        "image": pick_cover(paper_dir),
        "type": "paper",
        "link": f"https://doi.org/{post['paper_id'].replace('doi:', '')}",
    })

with open("_data/sources.yaml", "w") as f:
    yaml.dump(papers, f, sort_keys=False, allow_unicode=True)
