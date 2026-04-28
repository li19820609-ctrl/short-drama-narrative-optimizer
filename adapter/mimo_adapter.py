class MiMoModelAdapter:
    def __init__(self):
        self.api_key = ""
        self.api_base = "https://api.mimo.xiaomimimo.com/v1"
        self.model_name = "mimo-v2.5-longcontext"
        self.enable = False

    def set_auth(self, key: str):
        self.api_key = key
        self.enable = True

    def build_full_system_prompt(self, base_prompt: str) -> str:
        system_rule = """
严格遵循：人设指纹、硬事实轨道、剧情刹车、短剧节奏规则。
禁止AI套话、逻辑崩坏、人设割裂、篡改主线设定。
适配短剧强钩子、快节奏、高留存创作要求。
"""
        return system_rule + "\n" + base_prompt
