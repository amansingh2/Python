# Synchronous Operations!


# Asynchronous!
- single process, single thread that does the work!
- suppose we are reading from a disk, here the thread is not doing anything than waiting , and it is blocked, and rest 
    of the code can not be executed because of that! 
- The above waiting is known by application!
- Here callback (call-me-back functions) comes into the picture!
- so every code that is blocking, we write an await on top of it,
- it will act asynchronously but looks synchronously!

# Multi-processing!
- so it is the idea of spin-up instead of splitting up threads in a single process which shares the same resource of 
  the process, spin up just unique processes with their own memory structure and their own resource , and then use communicate between them using inter-process communication!
  or we can use centralized-redis-db or we may use sockets as well
- think like containers in kubernetes!