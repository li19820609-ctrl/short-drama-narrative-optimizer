import re

STYLE_MASK_LIBRARY = {
    "都市复仇": "冷硬克制、暗流涌动、隐忍反击、句句藏刀",
    "豪门恩怨": "虚伪拉扯、利益博弈、表面温和、内里算计",
    "古风虐恋": "隐忍悲情、宿命拉扯、克制留白、爱恨交织",
    "逆袭爽文": "前期受压、步步反杀、节奏紧凑、即时打脸",
    "悬疑探案": "细节埋坑、层层递进、伏笔密布、细思极恐"
}

class StyleMaskAdapter:
    def __init__(self):
        self.style_lib = STYLE_MASK_LIBRARY

    def get_style_prompt(self, drama_type: str) -> str:
        if drama_type not in self.style_lib:
            drama_type = "逆袭爽文"
        return f"【短剧风格强制约束】{self.style_lib[drama_type]}"

    def style_unify_polish(self, content: str, drama_type: str) -> str:
        content = re.sub(r"\n{3,}", "\n\n", content)
        if drama_type == "都市复仇":
            content = content.replace("温柔劝说", "冷漠对峙")
        if drama_type == "豪门恩怨":
            content = content.replace("直白撕破", "假意周旋")
        return content
