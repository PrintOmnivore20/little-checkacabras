from ..generic.Rules import set_rule, add_rule
from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin


class Logic(LogicMixin):

    def _has_total(self, player: int, total: int):
        return (self.item_count('Random Hat', player) +
                self.item_count('Checkacabra', player)) >= total

# Sets rules on completion condition
def set_completion_rules(world: MultiWorld, player: int):

    hat_req = 42
    checka_req = 15-5
    completion_requirements = lambda state: \
        state.has("Random Hat", player, hat_req) and \
        state.has("Checkacabra", player, checka_req)
    world.completion_condition[player] = lambda state: completion_requirements(state)
