#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) That while loop will run `n^3` times - Time Complexity `O(n^3)` - Space Complexity `O(1)`

b) `range(n)` \* `while(j < n)` - Time Complexity `O(n^2)` - Space Complexity `O(1)`

c) `bunnyEars()` will be added to the call stack `n` times, hence the `O(n)` space complexity - Time Complexity `O(n)` - Space Complexity `O(n)`

## Exercise II

```
n = number of stories
f = first floor at which egg will break
dropped_eggs = the number of eggs dropped
middle_floor = floor(n/2)
start_floor = 0
end_floor = n - 1
current_floor
```

This seems like a binary-search problem at first glance. Technically, the floors of the building (f) are sorted, since they go from the first floor to the last floor — in order, presumably.

So, you could start at the middle floor `current_floor = middle_floor` and drop your first egg `dropped_eggs += 1`.

If the egg breaks, you know that `f` is on a floor somewhere below the `current_floor`. So, you would find/update the middle floor:

```
end_floor = middle_floor - 1
middle_floor = floor((end_floor - start_floor) / 2)
current_floor = middle_floor
```

If the egg didn't break, you know that `f` is on a floor somewhere above `current_floor`.

```
start_floor = middle_floor + 1
middle_floor = floor((end_floor - start_floor) / 2)
current_floor = middle_floor
```

You would repeat this sequence until you found `f`. At worst, the number of eggs dropped will be `log n`. So, the worst-case, runtime complexity for this algorithm will be `O(log n)` — same as a binary search.

The worst-case, space complexity for this algorithm will be `O(1)` if a pigeon lays an egg on your hand ad-hoc and `O(log n)` if a deity blessed you with a bag of the perfect amount of eggs at the beginning of your journey. In the unlikely case that neither of those ordinary phenomena occur, you'll need to carry `log n` eggs with you up and down the stairs of this godforsaken, pigeon-deterring building.
