//Implementing MD5 

/*
MD5 algorithm follows the following steps 

1. Append Padding Bits: In the first step, we add padding bits in the original message in such a way that the total length of the message is 64 bits less than the exact multiple of 512.  

Suppose we are given a message of 1000 bits. Now we have to add padding bits to the original message. Here we will add 472 padding bits to the original message.  After adding the padding bits the size of the original message/output of the first step will be 1472 i.e. 64 bits less than an exact multiple of 512 (i.e. 512*3 = 1536).

Length(original message + padding bits) =  512 * i – 64 where i = 1,2,3 . . . 

2. Append Length Bits: In this step, we add the length bit in the output of the first step in such a way that the total number of the bits is the perfect multiple of 512. Simply, here we add the 64-bit as a length bit in the output of the first step. 
i.e. output of first step = 512 * n – 64 
length bits = 64. 

After adding both we will get 512 * n i.e. the exact multiple of 512.

3. Initialize MD buffer: Here, we use the 4 buffers i.e. J, K, L, and M. The size of each buffer is 32 bits.  
    - J = 0x67425301
    - K = 0xEDFCBA45
    - L = 0x98CBADFE
    - M = 0x13DCE476
4. Process Each 512-bit Block: This is the most important step of the MD5 algorithm. Here, a total of 64 operations are performed in 4 rounds. In the 1st round, 16 operations will be performed, 2nd round 16 operations will be performed, 3rd round 16 operations will be performed, and in the 4th round, 16 operations will be performed. We apply a different function on each round i.e. for the 1st round we apply the F function, for the 2nd G function, 3rd for the H function, and 4th for the I function. 
We perform OR, AND, XOR, and NOT (basically these are logic gates) for calculating functions. We use 3 buffers for each function i.e. K, L, M.

     - F(K,L,M) = (K AND L) OR (NOT K  AND M)
     - G(K,L,M) = (K AND L) OR (L AND NOT M)
     - H(K,L,M) = K XOR L XOR M
     - I(K,L,M) = L XOR (K OR NOT M)

Now take input as initialize MD buffer i.e. J, K, L, M. Output of  K will be fed in L, L will be fed into M, and M will be fed into J. After doing this now we perform some operations to find the output for J.

In the first step, Outputs of K, L, and M are taken and then the function F is applied to them. We will add modulo 232  bits for the output of this with J.
In the second step, we add the M[i] bit message with the output of the first step.
Then add 32 bits constant i.e. K[i] to the output of the second step. 
At last, we do left shift operation by n (can be any value of n) and addition modulo by 232.
After all steps, the result of J will be fed into K. Now same steps will be used for all functions G, H, and I. After performing all 64 operations we will get our message digest.

Output:
After all, rounds have been performed, the buffer J, K, L, and M contains the MD5 output starting with the lower bit J and ending with Higher bits M
*/