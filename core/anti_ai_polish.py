import re

AI_FLUENT_FILTER_WORDS = [
    "综上所述", "由此可见", "不难看出", "在整体来看",
    "总而言之", "与此同时", "某种程度上", "客观来说",
    "值得一提的是", "不可否认", "往往会", "通常情况下"
]

class AntiAIPolishEngine:
    def __init__(self):
        self.ai_filter_list = AI_FLUENT_FILTER_WORDS

    def remove_ai_template(self, content: str) -> str:
        for bad_word in self.ai_filter_list:
            content = content.replace(bad_word, "")
        return content

    def humanize_optimize(self, content: str) -> str:
        content = re.sub(r"。{2,}", "。", content)
        content = re.sub(r"\s+", "\n", content)
        return content.strip()
