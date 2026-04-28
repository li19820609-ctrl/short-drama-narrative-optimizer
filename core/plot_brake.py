from enum import Enum

PLOT_BRAKE_KEY_WORDS = [
    "强行降智", "逻辑崩坏", "脱离世界观", "过度玄幻",
    "无厘头转折", "设定冲突", "时间线混乱", "战力崩坏"
]
PLOT_BRAKE_TRIGGER_LIMIT = 3

class PlotRiskLevel(Enum):
    SAFE = 0
    WARNING = 1
    TRIGGER_BRAKE = 2
    FORCE_CORRECT = 3

class PlotEmergeBrakeSystem:
    def __init__(self):
        self.brake_words = PLOT_BRAKE_KEY_WORDS
        self.trigger_count = 0
        self.risk_level = PlotRiskLevel.SAFE

    def scan_plot_risk(self, content: str) -> PlotRiskLevel:
        hit_count = 0
        for word in self.brake_words:
            if word in content:
                hit_count += 1
        self.trigger_count += hit_count
        if self.trigger_count >= PLOT_BRAKE_TRIGGER_LIMIT:
            self.risk_level = PlotRiskLevel.TRIGGER_BRAKE
        elif hit_count > 0:
            self.risk_level = PlotRiskLevel.WARNING
        else:
            self.risk_level = PlotRiskLevel.SAFE
        return self.risk_level

    def brake_correct_content(self, content: str) -> str:
        if self.risk_level == PlotRiskLevel.TRIGGER_BRAKE:
            fix_tip = "\n【剧情刹车修正】已收敛不合理设定，回归主线逻辑。"
            return content + fix_tip
        return content
