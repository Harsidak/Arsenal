E. lce4113 and Security Game
time limit per test4 seconds
memory limit per test256 megabytes

This is an interactive problem. Additionally, hacks are disabled for this problem.

There are two hidden integers b
 and v
 such that b∈{0,1}
 and 0≤v<230.
 There is also a hidden operation ty,
 which is either &
 or |.
 Here, &
 denotes the bitwise AND operation. Additionally, |
 denotes the bitwise OR operation.

Your goal is to guess b.

The interaction proceeds as follows:

First, you send a value x
 to the interactor, such that 0≤x<230
.
The interactor sends back vtyx
. Formally, it will send back o(v,x)
, where
o(v,x)={v&xv|xty=&ty=|.
You then send two numbers m0
 and m1
, where 0≤m0,m1<230.
Finally, the interactor will send back mb⊕v,
 where ⊕
 denotes the bitwise XOR operation.
After the interaction, you have to output b
.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤105
). The description of the test cases follows. Note that this is the only initial input given.

Interaction
First, you need to output a single integer x(0≤x<230)
 — the initial value to send to the interactor.

In response, you will receive a single integer o(0≤o<230)
 — the result o(v,x)
 of the operation vtyx.

Next, you will send a single line containing two integers m0,m1(0≤m0,m1<230).

Finally, receive a single integer r(0≤r<230)
 — the value of mb⊕v.

Note that the interactor is partially adaptive — in particular, the choice of v
 may be determined by the initial input x
, but all hidden values will be fixed after.

After printing each query do not forget to output the end of line and flush∗
 the output. Otherwise, you will get Idleness limit exceeded verdict.

If, at any interaction step, you read −1
 instead of valid data, your solution must exit immediately. This means that your solution will receive Wrong answer because of an invalid query or any other mistake. Failing to exit can result in an arbitrary verdict because your solution will continue to read from a closed stream.

∗
To flush, use:

fflush(stdout) or cout.flush() in C++;
sys.stdout.flush() in Python;
see the documentation for other languages.
Example
InputCopy
3

0

315

3

35

5

5
OutputCopy
2

314 159

0

3

12 34

1

0

0 0

1
Note
The example interaction proceeds as follows:

Solution	Interactor	Explanation
3
There are 3
 test cases.
2
The solution chooses x=2
.
0
The interactor sends back xtyv=2&1=0.
314
 159
The solution sends m0=314
 and m1=159.
315
The interactor responds with mb⊕v=m0⊕v=315.
0
The solution determines b=0.
3
The next test case begins. The solution chooses x=3
.
3
The interactor sends back xtyv=3|1=3.
12
 34
The solution sends m0=12
 and m1=34.
35
The interactor responds with mb⊕v=m1⊕v=35.
1
The solution determines b=1.
0
The final test case begins. The solution chooses x=0
.
5
The interactor sends back xtyv=0|5=5.
0
 0
The solution sends m0=0
 and m1=0.
5
The interactor responds with mb⊕v=m1⊕v=5.
1
The solution determines b=1.
Note that the queries made by the example solution may not yield enough information to determine the hidden bit b.
 Additionally the empty lines in the example interaction are given for readability and need not be outputted in the solution.

The hidden values in the test cases are given below.

Test #	v
b
ty
1
1
0
&
2
1
1
|
3
5
1
|

