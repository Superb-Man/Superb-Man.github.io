# When Can an Integer Be Written as a Sum of Consecutive Positive Integers?

*An interesting number-theory question that eventually turns into a factorization problem.*

Suppose we want to write a positive integer $n$ as a sum of **$k$ distinct positive integers**, and their remainders modulo $k$ must also be distinct. How large can $k$ be?

At first this looks like two constraints: one about the sum, another about remainders. The nice observation is that **consecutive integers satisfy the remainder condition automatically**. So let's look for representations of $n$ as a sum of consecutive positive integers.

## 1. Why consecutive integers?

For instance,

$$3+4+5=12.$$

Their remainders modulo $3$ are $0,1,2$: every residue appears exactly once. More generally, any $k$ consecutive integers have all $k$ distinct residues modulo $k$.

That gives a particularly clean way to construct a valid answer; it is not a claim that every valid collection must be consecutive.

## 2. Turn the sum into an equation

Suppose the run begins at $a$ and has length $k$:

$$n=a+(a+1)+\cdots+(a+k-1).$$

Summing the progression gives

$$n=\frac{k(2a+k-1)}{2},$$

or equivalently,

$$\boxed{2n=k(2a+k-1).}$$

This is the key: **a scheduling-looking problem about picking numbers is now a factorization problem**.

Here's another way to arrive at the same equation. Write the run as the difference of two triangular numbers:

$$n=\sum_{i=1}^{x}i-\sum_{i=1}^{y}i
=\frac{x(x+1)-y(y+1)}{2},$$

where $x>y\ge0$. Factoring:

$$\boxed{(x-y)(x+y+1)=2n.}$$

Since the run contains $k=x-y$ numbers, this is the same formula. The factors $x-y$ and $x+y+1$ have **opposite parity**.

## 3. Why does an odd factor matter?

If $n$ is odd and $n\ge3$, it is itself an odd factor. More generally, take any odd divisor $d>1$ of $n$ and put $q=n/d$. There are two useful cases:

- If $q\ge(d+1)/2$, we get a run of **$d$** positive consecutive integers centered at $q$:

  $$q-\frac{d-1}{2},\ldots,q+\frac{d-1}{2}.$$

- If $q<(d+1)/2$, we get a run of **$2q$** positive consecutive integers, starting at $(d-2q+1)/2$.

Either way, we get a representation using more than one positive consecutive integer.

For example,

$$15=7+8=4+5+6=1+2+3+4+5.$$

Different factorizations lead to different run lengths. If the goal is to **maximize $k$**, we should examine the possible factor pairs, not merely find the first odd divisor.

## 4. What goes wrong for a power of two?

Suppose $n=2^m$. Then

$$2n=2^{m+1}.$$

But in the factored equation

$$k(2a+k-1)=2n,$$

one factor must be odd and the other even (their sum is $2a+2k-1$, which is odd). Since every odd factor of $2^{m+1}$ is $1$, the odd factor must be $1$.

For a run with $k\ge2$ and $a\ge1$, however, **both factors exceed 1**: $k\ge2$ and $2a+k-1\ge3$. That's impossible.

So a power of two has **no representation as a sum of two or more consecutive positive integers**.

The qualification matters: every positive integer still has the trivial one-term representation $n=n$.

## 5. Finding the longest run

We can look for valid values of $k$ directly from the factorization:

$$m=\frac{2n}{k},\qquad a=\frac{m-k+1}{2}.$$

A candidate length $k\ge2$ works if:

1. $k$ divides $2n$;
2. $m-k+1$ is positive and even, making $a$ a positive integer.

We can test those candidates and retain the largest valid length. This is clearer than relying on a special-purpose factorization shortcut before proving it.

```cpp
#include <algorithm>
#include <cstdint>

std::int64_t longestRun(std::int64_t n) {
    if (n <= 2) return -1; // require at least two terms

    const std::int64_t twice = 2 * n; // ensure no overflow for your input bounds
    std::int64_t best = -1;

    for (std::int64_t k = 2; k <= twice / k; ++k) {
        if (twice % k != 0) continue;
        const auto m = twice / k;
        // a = (m - k + 1) / 2 must be a positive integer.
        if (m >= k + 1 && (m - k + 1) % 2 == 0)
            best = std::max(best, k);
    }
    return best;
}
```

For positive consecutive terms, the maximum length satisfies $k(k+1)/2\le n$, so the loop need not examine larger $k$. The code assumes `2*n` fits in `int64_t`; a production implementation should validate that bound or use a wider integer.

## 6. A small but important distinction

**This construction establishes a consecutive-integer solution.** The original problem also allows *nonconsecutive* collections whose residues are distinct. To prove that the longest consecutive run is the globally largest valid $k$, one needs an additional argument; that stronger statement is not established by the factorization alone.

Distinct integers need not have distinct remainders. For instance, $1$ and $3$ are distinct but both leave remainder $1$ modulo $2$. The residue condition must be checked separately, and proving the unrestricted maximum requires its own argument.

The insight I like is the move from **an arithmetic progression to the factors of $2n$**. Suddenly the special role of powers of two becomes intuitive, not mysterious.

*Adapted into an explanatory note from my original Quora reasoning. The original screenshot includes a partial implementation; the standalone example above is a newly written demonstration for consecutive runs.*
