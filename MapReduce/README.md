Homework 05
===========
In your README.md, respond to the following prompts:

Describe how you implemented the hulk.py script. In particular, briefly discuss:

How you generated all the candidate password combinations.
How you filtered the candidates to only contain valid passwords.
How you handled processing on multiple cores.
How you verified that your code works properly.

I start by creating a generator using the permutation function of all the possible permutations
of the alphabet with the length having been given. Then I create the she1sum of these
permutations and compare them to the encrypted passwords. If I find a match, then return
the original password from my permutation generator. This is being done using a
list comprehension without generating a list comprehension without forming a list
By using prefixes to divide up the work in to different portions, I am able to process these portions using the multiprocessing ability to divide up the work and combine the results. I was able to verify my
work by using the make, test function. I also ran into memory problems which
I was able to solve later. I was able to know that I completed the assignment
as I was able to put a score on the leaderboard.



Complete the following table for passwords of length 5:

Processes	Time
1 189.493u 2.310s 3:30.22
2 188.957u 2.287s 3:15.20
4 183.146u 2.303s 1:33.27
6 185.385u 2.244s 1:15.00
8 189.786u 2.384s 0:53.18
How does the number of processes utilized affect the amount of time required to crack passwords?

By increasing the number of processes, the time required to crack passwords significantly
decreased. It divides up the work and thus completes the work more efficiently

From your experience in this project and recalling your Discrete Math knowledge, what would make a password more difficult to brute-force: more complex alphabet or longer password? Explain.

I want to say having more complex alphabet and longer password both make passwords
harder to brute-force. However, increasing the password length increases permutations
exponentially. From a discrete math standpoint, having longer password would
make a password more difficult to brute-force.
