Given a permutation∗
 p
 of length n
, you may perform the following operation on it any number of times (possibly zero):

Choose an index i
 where 1≤i≤n−1
, and move pi
 to p1
 (shifting everything in between to the right) and pi+1
 to pn
 (shifting everything in between to the left). Formally, you may transform p=[p1,…,pn]
 into p′=[pi,p1,p2,…,pi−1,pi+2,pi+3,…,pn,pi+1].
Provide a valid sequence of operations of length at most 4n
 to make pi=i
 for all i(1≤i≤n)
, or print −1
 if no sequence exists.

It can be shown that if a valid sequence of operations exists, there is a valid sequence of length at most 4n
 operations.

∗
A permutation of length n
 is an array consisting of n
 distinct integers from 1
 to n
 in arbitrary order. For example, [2,3,1,5,4]
 is a permutation, but [1,2,2]
 is not a permutation (2
 appears twice in the array), and [1,3,4]
 is also not a permutation (n=3
 but there is 4
 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤103
). The description of the test cases follows.

The first line contains an integer n(2≤n≤5000)
 — the length of the permutation.

The second line contains n
 integers p1,p2,…,pn(1≤pi≤n)
.

It is guaranteed that p
 is a permutation.

It is guaranteed that the sum of n
 over all test cases does not exceed 5000
.

Output
If there does not exist a valid sequence of operations, output −1
.

Otherwise, on the first line, output x(0≤x≤4n)
, the number of operations needed to sort the permutation. On the second line, output x
 integers i1,…,ix
 where ij
 (1≤ij≤n−1
) denotes the index corresponding to the j
-th operation.

Example
InputCopy
4
2
2 1
3
3 2 1
5
1 5 4 3 2
4
4 3 2 1
OutputCopy
-1
3
1 2 1
4
2 2 3 2
3
1 3 1
Note
For the first example, it can be shown that no sequence of operations can sort the permutation.

For the second example, one valid sequence of operations is [3,2,1]−→−i1=1[3,1,2]−→−i2=2[1,3,2]−→−i3=1[1,2,3].

For the third example, one valid sequence of operations is [1,5,4,3,2]−→−i1=2[5,1,3,2,4]−→−i2=2[1,5,2,4,3]−→−i3=3[2,1,5,3,4]−→−i4=2[1,2,3,4,5]

For the fourth example, one valid sequence of operations is [4,3,2,1]−→−i1=1[4,2,1,3]−→−i2=3[1,4,2,3]−→−i3=1[1,2,3,4]