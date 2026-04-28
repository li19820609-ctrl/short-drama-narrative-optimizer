import time
from core.character_fingerprint import CharacterFingerprintCore
from core.fact_orbit_lock import HardFactOrbitLock
from core.emotion_squeeze import EmotionSqueezeFullEngine
from core.style_mask import StyleMaskAdapter
from core.plot_brake import PlotEmergeBrakeSystem
from core.rhythm_hook import DramaRhythmHookEngine
from core.anti_ai_polish import AntiAIPolishEngine
from adapter.mimo_adapter import MiMoModelAdapter
from utils.logger import system_logger

class FullDramaNarrativeEngine:
    def __init__(self):
        self.char_core = CharacterFingerprintCore()
        self.fact_orbit = HardFactOrbitLock()
        self.emotion_engine = EmotionSqueezeFullEngine()
        self.style_engine = StyleMaskAdapter()
        self.plot_brake = PlotEmergeBrakeSystem()
        self.rhythm_engine = DramaRhythmHookEngine()
        self.anti_ai = AntiAIPolishEngine()
        self.mimo_adapter = MiMoModelAdapter()
        system_logger.info("【短剧全系统总线初始化完成】")

    def init_project_base_setting(self, world_config: dict):
        self.fact_orbit.init_world_orbit(world_config)

    def create_new_character(self, char_data: dict):
        return self.char_core.create_character_fingerprint(char_data)

    def single_episode_full_process(self, ep_num, raw_plot_text, drama_type, main_char_name):
        self.fact_orbit.global_orbit_check(raw_plot_text)
        self.char_core.character_consistency_check(main_char_name, raw_plot_text)
        self.plot_brake.scan_plot_risk(raw_plot_text)
        fix_content = self.plot_brake.brake_correct_content(raw_plot_text)
        emo_content = self.emotion_engine.squeeze_full_emotion(fix_content)
        style_content = self.style_engine.style_unify_polish(emo_content, drama_type)
        rhythm_content = self.rhythm_engine.cut_long_paragraph(style_content)
        reverse_content = self.rhythm_engine.insert_reversal_foreshadow(rhythm_content)
        hook_content = self.rhythm_engine.add_episode_hook(reverse_content)
        final_content = self.anti_ai.remove_ai_template(hook_content)
        final_content = self.anti_ai.humanize_optimize(final_content)
        system_logger.info(f"【第{ep_num}集 优化完成】")
        return final_content

if __name__ == "__main__":
    drama_system = FullDramaNarrativeEngine()

    world_config_example = {
        "world_view_rule": ["现代都市世界观，无超自然力量"],
        "core_event_truth": ["主角家族当年遭遇恶意构陷"],
        "time_line_lock": "现代都市｜单线时间流",
        "core_character_setting": ["主角复仇主线永久生效"],
        "forbidden_modify_key": ["家族冤案","反派身份"]
    }

    drama_system.init_project_base_setting(world_config_example)

    main_character_config = {
        "name": "沈聿",
        "gender": "男",
        "age_range": "25-30岁",
        "core_personality": "隐忍冷静、心思缜密",
        "hidden_trait": "内心背负仇恨",
        "ultimate_goal": "查清当年冤案",
        "forbidden_behavior": ["无脑冲动","轻易信任他人"],
        "speech_style": "言辞简短、冷硬克制",
        "relationship_map": {"苏晚":"唯一信任","陆明远":"敌对"}
    }

    drama_system.create_new_character(main_character_config)

    test_plot = "沈聿孤身进入陆氏集团，暗中收集冤案关键证据，面对反派试探全程不动声色。"
    result = drama_system.single_episode_full_process(1, test_plot, "都市复仇", "沈聿")

    print("\n===== 短剧成品文案 =====")
    print(result)
