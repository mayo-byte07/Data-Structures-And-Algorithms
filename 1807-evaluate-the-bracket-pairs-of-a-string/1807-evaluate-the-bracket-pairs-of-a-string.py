class Solution(object):
    def evaluate(self, s, knowledge):
        # 1. Convert the list of pairs into a dictionary for O(1) lookups
        knowledge_dict = {key: value for key, value in knowledge}
        
        result = []
        current_key = []
        inside_bracket = False
        
        # 2. Iterate through the string character by character
        for char in s:
            if char == '(':
                inside_bracket = True
            elif char == ')':
                inside_bracket = False
                # Build the key string we just extracted
                key_str = "".join(current_key)
                # Append the mapped value, or "?" if it doesn't exist
                result.append(knowledge_dict.get(key_str, "?"))
                # Reset the key buffer for the next bracket pair
                current_key = []
            elif inside_bracket:
                current_key.append(char)
            else:
                result.append(char)
                
        # 3. Join the resulting array into a single string
        return "".join(result)