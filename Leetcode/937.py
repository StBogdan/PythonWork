
# Name: Reorder Data in Log Files
# Link: https://leetcode.com/problems/reorder-data-in-log-files/
# Method: Sorting after splitting based on digit presence
# Time: O(n\*log(n))
# Space: O(n)
# Difficulty: Easy



from typing import List, Tuple


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
      ltr_logs  = []
      digit_logs = []
      
      for log in logs:
        _, log_data = log.split(' ', 1)
        if all(c == " " or c.isdigit() for c in log_data):
          digit_logs.append(log)
        else:
          ltr_logs.append(log)
          
      def get_log_comparator_val(log:str) -> Tuple[str, str]:
        log_id , log_data = log.split(" ", 1)
        return (log_data, log_id)

      ltr_logs.sort(key=get_log_comparator_val)
      return ltr_logs + digit_logs
              
