# CollatzConjectureCUDA
Searching for loops in the Collatz Conjecture using CUDA

Uses Numba python library for CUDA acceleration. Current efficiency is ~ 10 million numbers tested per second on an RTX 3000 series GPU.

Options for optimization include: improving the algorithm/storage of extra variables, optimizing the functions used for math.

[Wikipedia article describing Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
