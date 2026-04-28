from typing import List, Dict, Tuple
from dataclasses import dataclass
from utils.logger import system_logger

@dataclass
class HardFactOrbitData:
    world_view_rule: List[str]
    core_event_truth: List[str]
    time_line_lock: str
    core_character_setting: List[str]
    forbidden_modify_key: List[str]

class HardFactOrbitLock:
    def __init__(self):
        self.global_fact_bank: List[str] = []
        self.lock_data = None

    def init_world_orbit(self, config: Dict):
        self.lock_data = HardFactOrbitData(
            world_view_rule=config["world_view_rule"],
            core_event_truth=config["core_event_truth"],
            time_line_lock=config["time_line_lock"],
            core_character_setting=config["core_character_setting"],
            forbidden_modify_key=config["forbidden_modify_key"]
        )
        self.global_fact_bank.extend(self.lock_data.world_view_rule)
        self.global_fact_bank.extend(self.lock_data.core_event_truth)
        system_logger.info("【硬事实轨道全局锁定完成】")

    def global_orbit_check(self, content: str) -> Tuple[bool, List[str]]:
        fail_list = []
        for lock_key in self.lock_data.forbidden_modify_key:
            if f"取消{lock_key}" in content or f"改变{lock_key}" in content:
                fail_list.append(f"违规篡改：{lock_key}")
        for fact in self.global_fact_bank:
            if "并非如此" in content and fact in content:
                fail_list.append(f"推翻核心事实：{fact}")
        return len(fail_list) == 0, fail_list
