# goit-algo-hw-09
# 📊 Performance report

This experiment compares the performance of the greedy algorithm and dynamic programming.

## ⚙️ Finding functions

- `find_coins_greedy()` — function to find the change with the greedy algorithm
- `find_min_coins()` — function to find the change with dynamic programing

---

## 🔬 Tests results:

```
Test for amount - 113
    - find_coins_greedy duration - 2.5700777769088745e-05s.
    - find_min_coins duration - 0.009883379098027945s.
The dynamic programming function is 384.55564212204666 times slower than the greedy algorithm function in the current test

Test for amount - 1137
    - find_coins_greedy duration - 2.5980640202760696e-05s.
    - find_min_coins duration - 0.003240075893700123s.
The dynamic programming function is 124.71116448299966 times slower than the greedy algorithm function in the current test

Test for amount - 11379
    - find_coins_greedy duration - 2.0952895283699036e-05s.
    - find_min_coins duration - 0.060588985215872526s.
The dynamic programming function is 2891.676037870033 times slower than the greedy algorithm function in the current test

Test for amount - 113797
    - find_coins_greedy duration - 1.5086028724908829e-05s.
    - find_min_coins duration - 0.4626582432538271s.
The dynamic programming function is 30667.99432046177 times slower than the greedy algorithm function in the current test

Test for amount - 1137979
    - find_coins_greedy duration - 1.81589275598526e-05s.
    - find_min_coins duration - 5.76198846520856s.
The dynamic programming function is 317308.8524207611 times slower than the greedy algorithm function in the current test
```

---

## ✅ Conclusion

##### Greedy algorithm:
 - Very fast, regardless of the amount.

 - The time is almost unchanged - it works in O(n), where n is the number of denominations.

 - But it may not give the optimal answer if the set of coins is "non-standard".

##### Dynamic programming (DP):
 - Guarantees the optimal result - the minimum number of coins.

 - The time increases proportionally to the amount (O(amount × len(coins))), that is, linearly with the amount.

 - For large values, it becomes slow, as can be seen from the tests (tens of thousands of times).
