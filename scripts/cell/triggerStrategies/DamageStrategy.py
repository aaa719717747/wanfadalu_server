# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class DamageStrategy(TriggerStrategy):
    """
    伤害策略
    """

    def __init__(self):
        TriggerStrategy.__init__(self)

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        self.damage = strategyData["伤害"]

    def execute(self):
        super().execute()
        if self.otherEntity.canDamage is True:
            self.otherEntity.receiveDamage(self.trigger.owner, self.damage)
