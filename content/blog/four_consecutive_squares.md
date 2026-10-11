# Four Consecutive Squares and One Surprising Remainder

*An intuition-first number-theory note, inspired by a problem I discussed on Quora.*

Can four consecutive integers have squares that add up to a perfect square—or even to **any** perfect power greater than the first power?

Try the first four positive integers:

$$1^2+2^2+3^2+4^2=30.$$

The number 30 is not a perfect square, but checking examples won't prove the statement. The useful insight is simpler: **look at remainders modulo 4.**

## Why modulo 4?

Any even integer has a square divisible by 4. Any odd integer has a square congruent to 1 modulo 4. Four consecutive integers always contain **exactly two even and two odd numbers**.

So their squares leave remainders:

$$0+1+0+1\equiv 2\pmod 4.$$

In other words, for every integer $n$,

$$n^2+(n+1)^2+(n+2)^2+(n+3)^2\equiv 2\pmod4.$$

## What about perfect powers?

A perfect power $a^k$ with integers $a$ and $k\ge 2$ is either odd (and hence has odd remainder modulo 4) or has an even base. But if $a$ is even, then $a^k$ is divisible by 4.

Therefore a perfect power with exponent at least 2 can **never** be congruent to 2 modulo 4.

And that is the whole proof: the sum always lands in the one remainder class that perfect powers cannot occupy.

## A pattern worth keeping

When a question says “for *every* consecutive group of integers,” try a small modulus before expanding large polynomials. Here the local pattern **even, odd, even, odd** is all the structure needed.

*This is a newly written explanatory adaptation of the mathematical problem, not a transcription of the original Quora answer.* [Original question on Quora](https://mathquestions.quora.com/Show-that-sum-of-squares-of-any-four-consecutive-numbers-cant-be-a-perfect-power-Copied-Question).
