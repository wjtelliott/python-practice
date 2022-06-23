# Functional Prompt:

def flatten_sort_list(in_list, sort = True):
    # Create a new list to return
    result = list()

    # Iterate over list
    for i in in_list:

        # Check if we have a nested list. Append if not
        if not isinstance(i, list): result.append(i)
        # We have a nested list, recurs call this func
        # making sure not to sort our result in the nested func
        else: result += flatten_sort_list(i, False)

    # Return our result, and sort if we are the originally called func
    return result if not sort else sorted(result)

# Expected output: [1, 2, 3, 4, 9]
print(flatten_sort_list([3,4,[1,2,[9]]]))




# OOP Prompt:

# I created an enum for the condition in the case.
# Normally I would have put this import at the top of the file.
from enum import Enum
class Condition(Enum):
    PERFECT = 1
    REPAIRED = 2
    TRASHED = 3

class Podracer:
    def __init__(self,
        in_speed: int = 1,
        in_cond: Condition = Condition.PERFECT) -> None:

        self.max_speed = in_speed
        self.condition = in_cond
        
    def reapir(self) -> None:
        self.condition = Condition.REPAIRED

class AnakinsPod(Podracer):
    def __init__(self,
        in_speed: int = 1,
        in_cond:Condition = Condition.PERFECT) -> None:

        super().__init__(in_speed, in_cond)
    
    def boost(self) -> None:
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def __init__(self,
        in_speed: int = 1,
        in_cond: Condition = Condition.PERFECT) -> None:

        super().__init__(in_speed, in_cond)
    
    def flame_jet(self, other_pod: Podracer) -> None:
        other_pod.condition = Condition.TRASHED

# First Pod:
pod = Podracer(1, Condition.TRASHED)
print(f"New podracer made with speed {pod.max_speed}kph and condition `{pod.condition}`")
pod.reapir()
print(f"We have now fixed the pod. It is now {pod.condition}")

# Second Pod:
new_pod = AnakinsPod(2, Condition.PERFECT)
print(f"Anakin\'s pod has speed {new_pod.max_speed}kph and is `{new_pod.condition}`")
new_pod.boost()
print(f"Anakin\'s pod now goes {new_pod.max_speed}kph")

# Third Pod:
third_pod = SebulbasPod()

"""
The prompt said to run flame_jet() on third_pod, and then the
third_pod's condition should be trashed, but earlier it said that the
flame_jet() function should change `another` pod to trashed, so I
did the latter here.
"""

third_pod.flame_jet(new_pod)
print(f"Sebulba\'s pod has {new_pod.condition} Anakin\'s pod!")