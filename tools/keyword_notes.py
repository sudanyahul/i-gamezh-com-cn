from dataclasses import dataclass, field
from typing import List, Optional

# 示例配置数据
DEFAULT_URL = "https://i-gamezh.com.cn"
DEFAULT_KEYWORDS = ["爱游戏", "游戏笔记", "关键词管理"]


@dataclass
class KeywordNote:
    """使用 dataclass 组织关键词笔记"""
    title: str
    keywords: List[str] = field(default_factory=list)
    content: str = ""
    url: Optional[str] = None
    tags: List[str] = field(default_factory=list)

    def add_keyword(self, keyword: str) -> None:
        """添加一个关键词，避免重复"""
        if keyword not in self.keywords:
            self.keywords.append(keyword)

    def add_tag(self, tag: str) -> None:
        """添加一个标签"""
        if tag not in self.tags:
            self.tags.append(tag)

    def has_keyword(self, keyword: str) -> bool:
        """检查是否包含某个关键词"""
        return keyword in self.keywords

    def merge(self, other: "KeywordNote") -> "KeywordNote":
        """合并另一个笔记的关键词和标签"""
        combined_title = f"{self.title} & {other.title}"
        combined_keywords = list(set(self.keywords + other.keywords))
        combined_tags = list(set(self.tags + other.tags))
        combined_content = f"{self.content}\n\n---\n\n{other.content}"
        combined_url = self.url or other.url
        return KeywordNote(
            title=combined_title,
            keywords=combined_keywords,
            content=combined_content,
            url=combined_url,
            tags=combined_tags
        )


def format_note_simple(note: KeywordNote) -> str:
    """简单的格式化输出"""
    lines = [
        f"标题: {note.title}",
        f"关键词: {', '.join(note.keywords)}",
        f"标签: {', '.join(note.tags)}",
        f"内容: {note.content[:50]}{'...' if len(note.content) > 50 else ''}",
    ]
    if note.url:
        lines.append(f"URL: {note.url}")
    return "\n".join(lines)


def format_note_detailed(note: KeywordNote) -> str:
    """详细的格式化输出，适合展示"""
    separator = "=" * 50
    lines = [
        separator,
        f"📌 {note.title}",
        separator,
        f"🔑 关键词: {', '.join(note.keywords)}",
        f"🏷️ 标签: {', '.join(note.tags)}",
    ]
    if note.url:
        lines.append(f"🌐 关联 URL: {note.url}")
    lines.append("")
    lines.append("📝 内容:")
    # 简单缩进内容
    content_indented = "\n".join(f"   {line}" for line in note.content.split("\n"))
    lines.append(content_indented)
    lines.append(separator)
    return "\n".join(lines)


def format_note_as_dictionary(note: KeywordNote) -> str:
    """将笔记格式化为类似字典的字符串"""
    items = [
        f"  'title': '{note.title}'",
        f"  'keywords': {note.keywords}",
        f"  'tags': {note.tags}",
        f"  'content': '''{note.content}'''",
    ]
    if note.url:
        items.append(f"  'url': '{note.url}'")
    return "{\n" + ",\n".join(items) + "\n}"


def create_sample_notes() -> List[KeywordNote]:
    """创建一组示例笔记"""
    notes = []

    # 示例笔记 1
    note1 = KeywordNote(
        title="爱游戏平台介绍",
        keywords=["爱游戏", "游戏平台", "互动娱乐"],
        content="爱游戏是一个专注于玩家体验的游戏平台，提供丰富的游戏内容和社区互动功能。",
        url=DEFAULT_URL,
        tags=["平台", "介绍"]
    )
    note1.add_keyword("游戏社区")

    # 示例笔记 2
    note2 = KeywordNote(
        title="关键词笔记技巧",
        keywords=["关键词", "笔记方法", "组织整理"],
        content="使用关键词笔记可以帮助快速定位信息，推荐结合标签和分类进行管理。",
        tags=["技巧", "效率"]
    )
    note2.add_tag("学习")

    # 示例笔记 3（合并前两个）
    note3 = note1.merge(note2)
    note3.title = "爱游戏关键词笔记指南"

    notes.extend([note1, note2, note3])
    return notes


def main():
    """主函数：演示关键词笔记的创建和格式化输出"""
    sample_notes = create_sample_notes()

    print("=== 简单格式输出 ===")
    for i, note in enumerate(sample_notes, 1):
        print(f"\n--- 笔记 {i} ---")
        print(format_note_simple(note))

    print("\n\n=== 详细格式输出 ===")
    for i, note in enumerate(sample_notes, 1):
        print(f"\n{format_note_detailed(note)}")

    print("\n\n=== 字典格式输出 ===")
    for i, note in enumerate(sample_notes, 1):
        print(f"\n笔记 {i}:")
        print(format_note_as_dictionary(note))

    # 演示关键词检查功能
    print("\n\n=== 关键词检查 ===")
    first_note = sample_notes[0]
    check_word = "爱游戏"
    if first_note.has_keyword(check_word):
        print(f"笔记 '{first_note.title}' 包含关键词 '{check_word}'")
    else:
        print(f"笔记 '{first_note.title}' 不包含关键词 '{check_word}'")


if __name__ == "__main__":
    main()