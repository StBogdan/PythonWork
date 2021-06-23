# Name: Unique Email Addresses
# Link: https://leetcode.com/problems/unique-email-addresses/
# Method: Process email, store in set
# Time: O(n)
# Space: O(n)
# Difficulty: Easy


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set(map(self.simplify_email, emails)))

    def simplify_email(self, email: str):
        local, domain = email.split("@")
        if "+" in local:
            local = local.split("+")[0]

        local = local.replace(".", "")
        return f"{local}@{domain}"
