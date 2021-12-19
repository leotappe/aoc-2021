"""
Advent of Code 2021 | Day 18 | Part 1
"""
import sys


class Regular:
    def __init__(self, parent=None, value=None):
        self.parent = parent
        self.value = value

    def __str__(self):
        return str(self.value)

    def explode(self, depth):
        return False

    def split(self):
        if self.value < 10:
            return False
        pair = Pair(parent=self.parent)
        pair.left = Regular(parent=pair, value=self.value // 2)
        pair.right =Regular(parent=pair, value=(self.value + 1) // 2)
        if self == self.parent.left:
            self.parent.left = pair
        else:
            self.parent.right = pair
        return True

    def magnitude(self):
        return self.value


class Pair:
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return f'[{self.left},{self.right}]'

    def __add__(self, other):
        pair = Pair()
        pair.left = self
        pair.right = other
        self.parent = other.parent = pair
        pair.reduce()
        return pair

    def reduce(self):
        while self.left.explode(1) or self.right.explode(1) or self.left.split() or self.right.split():
            pass

    def explode(self, depth):
        if depth < 4:
            return self.left.explode(depth + 1) or self.right.explode(depth + 1)

        assert isinstance(self.left, Regular)
        assert isinstance(self.right, Regular)

        pred = self.predecessor()
        if pred is not None:
            pred.value += self.left.value

        succ = self.successor()
        if succ is not None:
            succ.value += self.right.value

        if self == self.parent.left:
            self.parent.left = Regular(parent=self.parent, value=0)
        else:
            self.parent.right = Regular(parent=self.parent, value=0)
        
        return True

    def split(self):
        return self.left.split() or self.right.split()

    def predecessor(self):
        while self.parent is not None and self == self.parent.left:
            self = self.parent
        
        if self.parent is None:
            return None

        self = self.parent.left

        while not isinstance(self, Regular):
            self = self.right

        return self

    def successor(self):
        while self.parent is not None and self == self.parent.right:
            self = self.parent
        
        if self.parent is None:
            return None

        self = self.parent.right
        
        while not isinstance(self, Regular):
            self = self.left

        return self

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def parse(s, parent):
    if s[0] != '[':
        return Regular(parent=parent, value=int(s))
    
    s = s[1:-1]
    opening = 0

    for i, c in enumerate(s):
        if c == '[':
            opening += 1
        elif c == ']':
            opening -= 1
        
        if opening == 0:
            while s[i] != ',':
                i += 1
            pair = Pair(parent=parent)
            pair.left = parse(s[:i], pair)
            pair.right = parse(s[i + 1:], pair)
            return pair

    print('Malformed string')
    exit(-1)


def main():
    with open(sys.argv[1]) as f:
        numbers = [parse(line.strip(), None) for line in f.readlines()]

    acc = numbers[0]

    for n in numbers[1:]:
        acc = acc + n

    print(acc)
    print(acc.magnitude())


if __name__ == '__main__':
    main()
