class Box:
    def __init__(self, x, y, w, h):
        '''
        Create an instance of the box class whose lower-left corner is at (x,y)
        and whose width is w and height is h. The width w and height h must be
        positive.
        '''

        if w <= 0 or h <= 0:
            raise ValueError("cannot create box with nonpositive dimensions")
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def moveBy(self, dx, dy):
        '''
        Translates this box by dx units along the x axis and dy units along
        the y axis.
        '''
        self.x += dx
        self.y += dy

    def contains(self, b):
        '''
        Assumes b is another instance of the box class.

        Returns true if and only if the box b is entirely contained
        within box self (they can share edges).
        '''
        return (self.x <= b.x and self.y <= b.y and
                self.x + self.w >= b.x + b.w and
                self.y + self.h >= b.y + b.h)

    def unionWith(self, b):
        '''
        Assumes b is another instance of the box class.

        Returns the smallest box that contains both self and box b.
        '''
        new_x = min(self.x, b.x)
        new_y = min(self.y, b.y)
        new_w = max(self.x + self.w, b.x + b.w) - new_x
        new_h = max(self.y + self.h, b.y + b.h) - new_y
        return Box(new_x, new_y, new_w, new_h)

    def __str__(self):
        return "Box({}, {}, {}, {})".format(self.x, self.y,
                                            self.w, self.h)


def longest_sequence(boxes, i, memo = None):
    '''
    Assumes boxes is a list of boxes and that no two boxes have identical
    (x,y,w,h) (i.e. no two boxes are the same). Also, 0 <= i < len(boxes) is an index.

    Returns the largest value m such that it is possible to find a list of length m
    of distinct boxes starting at boxes[i] where each box in the list contains
    the next box in the list (according to the contains() method).

    Note, the boxes in "chain" don't have to be in the same order as they
    appeared in boxes.

    Example:
    boxes = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 5, 5)]
    longest_sequence(boxes, 1) returns 2

    boxes2 = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 8, 8)]
    longest_sequence(boxes, 1) returns 3

    For full marks, your algorithm should run in O(n^2) time where
    n = len(boxes). Use dynamic programming to achieve this.
    '''

    if memo is None:
        memo = {}
    if boxes[i] in memo:
        return memo[boxes[i]]
    contain = False
    big = 0
    for j in range(len(boxes)):
        if boxes[i] != boxes[j]:
            if boxes[i].contains(boxes[j]):
                loc_big = 1+longest_sequence(boxes,j,memo)
                big = max(big,loc_big)
                memo[boxes[i]] = big
                contain = True

    if contain is False:
        big = 1
        memo[boxes[i]] = big
        return 1
    return memo[boxes[i]]
    # now you finish it

boxes = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 5, 5)]
print(longest_sequence(boxes, 1))
boxes2 = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 8, 8)]
print(longest_sequence(boxes2, 1))
# State the running time of your algorithm below here. Justify it in 2-3
# The runing time should be 0(n^2) since I used memo here.
# When I have the result of longest_sequence(boxes,i,memo) in memo, I could
# use it immediately(line77-78). So when I check the longest_sequence(boxes,j,memo)
# in line 85 I don't need to do the work again. Instead, I will have the result immediately
# sentences. Hint, remember the "running time analysis template" for dynamic
# programming problems from the lectures.
