import random
import re

HOOK_ENDING_LIBRARY = [
    "他以为一切尽在掌握，却不知自己早已落入别人的棋局。",
    "眼前的真相只是冰山一角，真正的阴谋还深埋在暗处。",
    "这一次的退让从不是妥协，而是蓄谋已久的反击。",
    "所有人都被表象蒙蔽，唯独他看清了全局的破绽。",
    "看似尘埃落定，下一秒，更大的风暴即将袭来。"
]
REVERSAL_LIBRARY = [
    "一直防备的敌人只是棋子，最信任的人才是幕后操盘手。",
    "当年的意外并非巧合，而是一场精心策划的灭口。",
    "他刻意展露的软弱，全是为了麻痹对手的伪装。",
    "所谓的受害者，其实才是整场事件的始作俑者。"
]

class DramaRhythmHookEngine:
    def __init__(self):
        self.hook_lib = HOOK_ENDING_LIBRARY
        self.reversal_lib = REVERSAL_LIBRARY

    def add_episode_hook(self, content: str) -> str:
        hook_text = random.choice(self.hook_lib)
        return content + f"\n\n——本集收尾钩子——\n{hook_text}"

    def insert_reversal_foreshadow(self, content: str) -> str:
        reversal_text = random.choice(self.reversal_lib)
        return content + f"\n【暗线反转铺垫】{reversal_text}"

    def cut_long_paragraph(self, content: str) -> str:
        lines = content.split("\n")
        new_lines = []
        for line in lines:
            if len(line) > 120:
                mid = len(line) // 2
                new_lines.append(line[:mid] + "\n" + line[mid:])
            else:
                new_lines.append(line)
        return "\n".join(new_lines)
