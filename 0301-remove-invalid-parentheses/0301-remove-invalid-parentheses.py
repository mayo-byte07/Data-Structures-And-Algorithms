class Solution(object):
    def removeInvalidParentheses(self, s):
        
        def is_valid(string):
            count=0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                        count-= 1

                if count < 0:
                    return False
            return count == 0 

        current_level={s}
        
        while True:
            valid_strings = [string for string in current_level if is_valid(string)]
            if valid_strings:
                return valid_strings

            next_level = set()
            for string in current_level:
                for i in range(len(string)):
                    if string[i] in '()':
                        new_string = string[:i] + string[i+1:]
                        next_level.add(new_string)
            
            current_level = next_level
#POTD Day 7