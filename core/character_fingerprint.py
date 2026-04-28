from typing import List, Dict, Tuple
from dataclasses import dataclass, field
from utils.logger import system_logger

CONTRADICTION_KEY_WORDS = [
    "一改往日", "突然转变", "性格大变", "前后矛盾",
    "瞬间黑化", "突然心软", "人设崩塌", "一反常态"
]

@dataclass
class CharacterFingerprintData:
    name: str
    gender: str
    age_range: str
    core_personality: str
    hidden_trait: str
    ultimate_goal: str
    forbidden_behavior: List[str]
    speech_style: str
    relationship_map: Dict[str, str]
    fixed_memory: List[str] = field(default_factory=list)

class CharacterFingerprintCore:
    def __init__(self):
        self.character_database: Dict[str, CharacterFingerprintData] = {}
        self.contradiction_words = CONTRADICTION_KEY_WORDS

    def create_character_fingerprint(self, data: Dict) -> CharacterFingerprintData:
        char_obj = CharacterFingerprintData(
            name=data["name"],
            gender=data["gender"],
            age_range=data["age_range"],
            core_personality=data["core_personality"],
            hidden_trait=data["hidden_trait"],
            ultimate_goal=data["ultimate_goal"],
            forbidden_behavior=data["forbidden_behavior"],
            speech_style=data["speech_style"],
            relationship_map=data["relationship_map"],
            fixed_memory=data.get("fixed_memory", [])
        )
        self.character_database[char_obj.name] = char_obj
        system_logger.info(f"【角色指纹绑定完成】{char_obj.name}")
        return char_obj

    def character_consistency_check(self, char_name: str, content: str) -> Tuple[bool, List[str]]:
        if char_name not in self.character_database:
            return True, []
        char = self.character_database[char_name]
        error_list = []
        for forbid_action in char.forbidden_behavior:
            if forbid_action in content:
                error_list.append(f"违规行为：{forbid_action}")
        for bad_word in self.contradiction_words:
            if bad_word in content:
                error_list.append(f"人设矛盾关键词：{bad_word}")
        for memory in char.fixed_memory:
            if "推翻" in content and memory in content:
                error_list.append(f"篡改固定记忆：{memory}")
        return len(error_list) == 0, error_list

    def get_character_prompt_prefix(self, char_name: str) -> str:
        if char_name not in self.character_database:
            return ""
        c = self.character_database[char_name]
        prompt = f"""
【角色绝对约束】
姓名：{c.name}
核心性格：{c.core_personality}
隐藏特质：{c.hidden_trait}
终极目标：{c.ultimate_goal}
说话风格：{c.speech_style}
严禁行为：{"、".join(c.forbidden_behavior)}
禁止人设反转、性格割裂、行为矛盾。
"""
        return prompt.strip()
