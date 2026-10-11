# Why Odd Squares Always Leave Remainder One Modulo Eight

*A small observation that makes several number-theory questions much easier.*

Squares seem unpredictable until you ask a much smaller question: **what remainder can a square have when divided by 8?**

Start with an odd integer. We can write it as $2n+1$, so its square is

$$(2n+1)^2=4n(n+1)+1.$$

The crucial fact isn't the multiplication. It is that $n$ and $n+1$ are consecutive—**one of them must be even**. Hence $n(n+1)$ is divisible by 2, and $4n(n+1)$ is divisible by 8.

So every odd square has the same remainder:

$$(2n+1)^2\equiv 1\pmod 8.$$

## Why is that useful?

Suppose somebody claims that a number congruent to 3 modulo 8 is a perfect square. It cannot be the square of an odd number (those leave 1); and it cannot be the square of an even number either (those leave 0 or 4).

This technique is useful because **you don't need to know the square root to rule out a square**. You only need one impossible remainder.

One small caveat: if a number has remainder 1 modulo 8, it *might* be a square—but that condition by itself does not prove it is one.

*An original short explainer on modular arithmetic, included alongside my Quora mathematics archive rather than presented as an exact transcription of a screenshot.*
