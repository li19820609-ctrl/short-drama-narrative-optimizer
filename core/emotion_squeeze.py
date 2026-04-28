import random

EMOTION_LAYER_POOL = {
    "压抑层": ["隐忍", "委屈", "无力", "负重", "克制"],
    "冲突层": ["愤怒", "抵触", "对峙", "猜忌", "决裂"],
    "爆发层": ["反噬", "撕破伪装", "绝地反击", "真相曝光", "彻底清算"],
    "留白层": ["意难平", "宿命感", "遗憾", "执念", "余恨"]
}
DEFAULT_EMOTION_INTENSITY = 4

class EmotionSqueezeFullEngine:
    def __init__(self):
        self.emotion_lib = EMOTION_LAYER_POOL
        self.intensity = DEFAULT_EMOTION_INTENSITY

    def set_emotion_intensity(self, num: int):
        self.intensity = max(1, min(6, num))

    def extract_base_emotion(self, text: str) -> str:
        if any(k in text for k in ["压迫", "陷害", "欺负"]):
            return "压抑层"
        elif any(k in text for k in ["对峙", "争吵", "揭穿"]):
            return "冲突层"
        elif any(k in text for k in ["反击", "曝光", "复仇"]):
            return "爆发层"
        return "留白层"

    def squeeze_full_emotion(self, content: str) -> str:
        base_key = self.extract_base_emotion(content)
        select_emotions = []
        for layer, word_list in self.emotion_lib.items():
            if layer == base_key:
                select_emotions.extend(random.sample(word_list, 2))
            else:
                select_emotions.append(random.choice(word_list))
        final_tag = "｜".join(list(set(select_emotions)))
        emotion_prefix = f"【多层情绪强化】{final_tag}\n"
        return emotion_prefix + content
