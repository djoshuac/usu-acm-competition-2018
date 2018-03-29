# A Strange Doubling

Tommy works for a biomedical company and has been tasked with building a machine which will duplicate an entire sequence of DNA (a string *S*). However, his boss informs him that there are some very strange requirements enforced by the customer.

The machine begins with no DNA inside and can perform the following operations:

- Duplicate the current DNA sequence in the machine and append it to the end of the current DNA sequence in the machine.

- Append a single nucleobase (character) to the end of the current DNA sequence in the machine.

Tommy is nearly finished prototyping the machine when his boss comes to him with additional requirements:

- The machine loves powers of two and can only perform the duplicate operation when the length of the current DNA sequence in the machine is a power of two.


Output the minimum number of operations required to construct the DNA sequence (string *S*) following Tommy's requirements.

### Input

A single string *S*.

### Output

A single integer denoting the number of moves required to reconstruct the given DNA sequence *S*.