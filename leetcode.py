class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return sorted(self.stack)[0]


# Success
# Details
# Runtime: 604 ms, faster than 23.64% of Python3 online submissions for Min Stack.
# Memory Usage: 17.6 MB, less than 42.52% of Python3 online submissions for Min Stack.
# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class MinStack:
    def __init__(self):
        self.stack = [(-1, float("inf"))]

    def push(self, x):
        self.stack.append([x, min(x, self.stack[-1][1])])

    def pop(self):
        if len(self.stack) > 1:
            self.stack.pop()

    def top(self):
        if len(self.stack) == 1:
            return None
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


# ================================================#
#                  question v                     #
# ================================================#

# 155. Min Stack
# Easy

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


# Constraints:

# Methods pop, top and getMin operations will always be called on non-empty stacks.
