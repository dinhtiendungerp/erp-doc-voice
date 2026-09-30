"""Đóng gói team-skill/natural-writing.zip để upload lên Claude.ai, Cowork, Claude Desktop.

Zip gồm router-SKILL.md (đổi tên thành SKILL.md) và bản chụp thư mục natural-writing/
làm dự phòng khi máy không tải được repo. Chạy lại mỗi khi sửa natural-writing/:

    python team-skill/build.py
"""
import datetime
import pathlib
import subprocess
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "team-skill" / "natural-writing.zip"


def text(path):
    # Working tree trên Windows có thể là CRLF, đổi về LF cho giống blob trên git
    return path.read_bytes().replace(b"\r\n", b"\n")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout.strip()


commit = git("log", "-1", "--format=%h", "--", "natural-writing")
dirty = git("status", "--porcelain", "--", "natural-writing")
version = f"Chụp ngày {datetime.date.today():%d/%m/%Y} từ natural-writing/ ở commit {commit}"
if dirty:
    version += ", cộng thay đổi chưa commit"

files = {
    "natural-writing/SKILL.md": text(ROOT / "team-skill" / "router-SKILL.md"),
    "natural-writing/snapshot/VERSION.txt": (version + "\n").encode("utf-8"),
    "natural-writing/snapshot/natural-writing.md": text(ROOT / "natural-writing" / "SKILL.md"),
}
for p in sorted((ROOT / "natural-writing" / "references").glob("*.md")):
    files[f"natural-writing/snapshot/references/{p.name}"] = text(p)

# Giờ trong zip cố định để build lại cùng nội dung thì ra cùng file, không sinh diff thừa
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for name, data in files.items():
        info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, data)

print(f"{OUT.relative_to(ROOT).as_posix()}: {len(files)} files, {OUT.stat().st_size} bytes, "
      f"commit {commit}{' + uncommitted changes' if dirty else ''}")
