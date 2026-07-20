class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        return ["Fizz" * (x := i % 3 < 1) + "Buzz" * (y := i % 5 < 1) + str(i) * (not (x or y)) for i in range(1, n + 1)]
