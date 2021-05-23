
# Name: Design Browser History
# Link: https://leetcode.com/problems/design-browser-history/
# Method: List and keeping track of index (alternatively, 2 stacks)
# Time: ~O(1)
# Space: O(n)
# Difficulty: Medium

class BrowserHistory:

    def __init__(self, homepage: str):
        self._history = [homepage]
        self._poz_index = 0
        self._limit_index = 0
        

    def visit(self, url: str) -> None:
        self._poz_index += 1
        
        if self._poz_index == len(self._history):
            self._history.append(url)
        else:
            self._history[self._poz_index]=url
            
        self._limit_index = self._poz_index
        

    def back(self, steps: int) -> str:
        self._poz_index -= min(steps, self._poz_index)
        return self._history[self._poz_index]
        

    def forward(self, steps: int) -> str:
        step_to_go = min(steps, self._limit_index - self._poz_index)
        self._poz_index += step_to_go 
        return self._history[self._poz_index]
