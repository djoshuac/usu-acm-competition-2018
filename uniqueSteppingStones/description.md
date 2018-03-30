# Unique Stepping Stones

Edsger has a love for problem solving. One day, he comes upon a magical rectangular pond. The pond is divided into N rows and M columns. At each square in the pond is a stone and each stone has a number written on it. What makes this pond magical is that while standing on any stone in a column, Edsger can magically teleport to any stone in the next column. Edsger wants to know if he can cross the pond without stepping on any number more than once.

The stones are presented in rows and columns. From any stone at column *i*, Edgser can reach any other stone at column *i+1*.

Help Edsger determine if such a unique path exists from the beginning of the pond (first column) to the end of the pond (last column).

### Input

The first line will contain two integers, N and M.

The next N lines will contain M space separated integers. These M integers given are the stone numbers.

### Output

Output **Yes** if Edgser can make it from one end to the other following some unique path.

Ouput **No** otherwise.