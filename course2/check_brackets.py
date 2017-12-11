# python3
import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def process_str(text):
    brackets_stack = []

    for i, char in enumerate(text, 1):  # Begin our index at 1.
        if char == '(' or char == '[' or char == '{':
            # Process an opening bracket - always allowed.
            brackets_stack.append(Bracket(char, i))
        # Process closing bracket - must always match the last-added bracket.
        if char == ')' or char == ']' or char == '}':
            if not brackets_stack:  # Nothing in the stack? Mismatch!
                return i
            prev = brackets_stack.pop()
            if not prev.match(char):
                return i  # Mismatch - return current position.

    # Finished processing the string - if any brackets remain in the stack,
    # then they are unclosed (return the last one's position).
    if brackets_stack:
        unclosed = brackets_stack.pop()
        return unclosed.position

    return 'Success'


if __name__ == "__main__":
    text = sys.stdin.read()
    print(process_str(text))
