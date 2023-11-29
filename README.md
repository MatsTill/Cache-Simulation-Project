## Project Description & Specifications:
The cache simulation system implemented in this project is designed to emulate a fully associated (FA) cache with a first-in-first-out (FIFO) replacement policy. The system provides a user-friendly GUI, ensuring a seamless experience for users. It is implemented in Python, utilizing the Tkinter library for the graphical interface.

The common specifications for the cache system are as follows:
Number of Cache Blocks: 32 blocks
Cache Line: 64 words
Read Policy: Load-Through
Number of Memory Blocks: User-input, allowing flexibility in the simulated memory size.

## Features Implemented
- Memory Access Simulation: Users can choose from various test cases, including Sequential Sequences, Random Sequences, and Mid-Repeat Blocks Sequences.

- FIFO Replacement Policy: The system employs the FIFO replacement policy to manage cache contents when a cache miss occurs.

- GUI Visualization: The graphical interface provides a real-time representation of the cache memory, allowing users to observe cache hits, misses, and memory access traces.

![App](https://github.com/MatsTill/Cache-Simulation-Project/blob/main/app.png)


## GUI Output
1. Cache Memory Snapshot: Users can choose between a step-by-step animated tracing option or a final memory snapshot. The system generates a visual representation of the cache memory, aiding in understanding cache dynamics.
2. Text Log: A detailed text log is provided, capturing the cache memory trace.
3. Performance Metrics: The system outputs key performance metrics, including memory access count, cache hit count, cache miss count, cache hit rate, cache miss rate, average memory access time, and total memory access time.

## Video Walkthrough:
[Google Drive Link](https://drive.google.com/file/d/12dVWclUbrTgqcWuqQj91zjiugZn7YoHA/view?usp=sharing)

## Detailed Analysis:

### Test Case #1: Sequential Sequence

Analysis:
1. In a Sequential sequence, each memory block is accessed in order.
2. Initially, there are cache misses, but once the cache is filled, subsequent accesses result in cache hits.
3. The cache hit rate is 75%, and the average memory access time is 1.25 cycles.
   
```
Number of Memory Blocks: 2

Simulation Results:
Number of Cache Blocks: 32
Cache Line Size: 64 words
Read Policy: Load-Through
Number of Memory Blocks: 2
Memory Access Count: 16
Cache Hit Count: 12
Cache Miss Count: 4
Cache Hit Rate: 75.00%
Cache Miss Rate: 25.00%
Average Memory Access Time: 1.25 cycles
Total Memory Access Time: 20.00 cycles

Step 1:
Memory Access Count: 1
Cache Hit Count: 0
Cache Miss Count: 1
Cache Memory: [0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 2:
Memory Access Count: 2
Cache Hit Count: 0
Cache Miss Count: 2
Cache Memory: [0, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 3:
Memory Access Count: 3
Cache Hit Count: 0
Cache Miss Count: 3
Cache Memory: [0, 1, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 4:
Memory Access Count: 4
Cache Hit Count: 0
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 5:
Memory Access Count: 5
Cache Hit Count: 1
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 6:
Memory Access Count: 6
Cache Hit Count: 2
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 7:
Memory Access Count: 7
Cache Hit Count: 3
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 8:
Memory Access Count: 8
Cache Hit Count: 4
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 9:
Memory Access Count: 9
Cache Hit Count: 5
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 10:
Memory Access Count: 10
Cache Hit Count: 6
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 11:
Memory Access Count: 11
Cache Hit Count: 7
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 12:
Memory Access Count: 12
Cache Hit Count: 8
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 13:
Memory Access Count: 13
Cache Hit Count: 9
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 14:
Memory Access Count: 14
Cache Hit Count: 10
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 15:
Memory Access Count: 15
Cache Hit Count: 11
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 16:
Memory Access Count: 16
Cache Hit Count: 12
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
```


### Test Case #2: Random Sequence

Analysis:
1. Due to the random nature, in this test case, there are more cache misses, resulting in a lower cache hit rate (12.50%). 
2. It is notable that a random sequence would be more unpredicatable in terms of cache performance
3. The average memory access time is higher compared to the sequential case (1.88 cycles).

```
Number of Memory Blocks: 2

Simulation Results:
Number of Cache Blocks: 32
Cache Line Size: 64 words
Read Policy: Load-Through
Number of Memory Blocks: 2
Memory Access Count: 8
Cache Hit Count: 1
Cache Miss Count: 7
Cache Hit Rate: 12.50%
Cache Miss Rate: 87.50%
Average Memory Access Time: 1.88 cycles
Total Memory Access Time: 15.00 cycles

Step 1:
Memory Access Count: 1
Cache Hit Count: 0
Cache Miss Count: 1
Cache Memory: [1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 2:
Memory Access Count: 2
Cache Hit Count: 0
Cache Miss Count: 2
Cache Memory: [1, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 3:
Memory Access Count: 3
Cache Hit Count: 0
Cache Miss Count: 3
Cache Memory: [1, 5, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 4:
Memory Access Count: 4
Cache Hit Count: 0
Cache Miss Count: 4
Cache Memory: [1, 5, 2, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 5:
Memory Access Count: 5
Cache Hit Count: 0
Cache Miss Count: 5
Cache Memory: [1, 5, 2, 4, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 6:
Memory Access Count: 6
Cache Hit Count: 1
Cache Miss Count: 5
Cache Memory: [1, 5, 2, 4, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 7:
Memory Access Count: 7
Cache Hit Count: 1
Cache Miss Count: 6
Cache Memory: [1, 5, 2, 4, 6, 7, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 8:
Memory Access Count: 8
Cache Hit Count: 1
Cache Miss Count: 7
Cache Memory: [1, 5, 2, 4, 6, 7, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
```


### Test Case #3: Mid-Repeat Blocks Sequence

Analysis:
1. In this test case of Mid-Repeat Blocks Sequence, the cache hit rate is higher (82.61%) due to the reuse of some memory blocks.
2. The average memory access time is lower compared to the two other patterns (1.17 cycles).

```
Number of Memory Blocks: 8

Simulation Results:
Number of Cache Blocks: 32
Cache Line Size: 64 words
Read Policy: Load-Through
Number of Memory Blocks: 8
Memory Access Count: 92
Cache Hit Count: 76
Cache Miss Count: 16
Cache Hit Rate: 82.61%
Cache Miss Rate: 17.39%
Average Memory Access Time: 1.17 cycles
Total Memory Access Time: 108.00 cycles

Step 1:
Memory Access Count: 1
Cache Hit Count: 0
Cache Miss Count: 1
Cache Memory: [0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 2:
Memory Access Count: 2
Cache Hit Count: 0
Cache Miss Count: 2
Cache Memory: [0, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 3:
Memory Access Count: 3
Cache Hit Count: 0
Cache Miss Count: 3
Cache Memory: [0, 1, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 4:
Memory Access Count: 4
Cache Hit Count: 0
Cache Miss Count: 4
Cache Memory: [0, 1, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 5:
Memory Access Count: 5
Cache Hit Count: 0
Cache Miss Count: 5
Cache Memory: [0, 1, 2, 3, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 6:
Memory Access Count: 6
Cache Hit Count: 0
Cache Miss Count: 6
Cache Memory: [0, 1, 2, 3, 4, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 7:
Memory Access Count: 7
Cache Hit Count: 0
Cache Miss Count: 7
Cache Memory: [0, 1, 2, 3, 4, 5, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 8:
Memory Access Count: 8
Cache Hit Count: 1
Cache Miss Count: 7
Cache Memory: [0, 1, 2, 3, 4, 5, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 9:
Memory Access Count: 9
Cache Hit Count: 2
Cache Miss Count: 7
Cache Memory: [0, 1, 2, 3, 4, 5, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 10:
Memory Access Count: 10
Cache Hit Count: 3
Cache Miss Count: 7
Cache Memory: [0, 1, 2, 3, 4, 5, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 11:
Memory Access Count: 11
Cache Hit Count: 4
Cache Miss Count: 7
Cache Memory: [0, 1, 2, 3, 4, 5, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 12:
Memory Access Count: 12
Cache Hit Count: 5
Cache Miss Count: 7
Cache Memory: [0, 1, 2, 3, 4, 5, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 13:
Memory Access Count: 13
Cache Hit Count: 6
Cache Miss Count: 7
Cache Memory: [0, 1, 2, 3, 4, 5, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 14:
Memory Access Count: 14
Cache Hit Count: 7
Cache Miss Count: 7
Cache Memory: [0, 1, 2, 3, 4, 5, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 15:
Memory Access Count: 15
Cache Hit Count: 7
Cache Miss Count: 8
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 16:
Memory Access Count: 16
Cache Hit Count: 7
Cache Miss Count: 9
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 17:
Memory Access Count: 17
Cache Hit Count: 7
Cache Miss Count: 10
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 18:
Memory Access Count: 18
Cache Hit Count: 7
Cache Miss Count: 11
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 19:
Memory Access Count: 19
Cache Hit Count: 7
Cache Miss Count: 12
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 20:
Memory Access Count: 20
Cache Hit Count: 7
Cache Miss Count: 13
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 21:
Memory Access Count: 21
Cache Hit Count: 7
Cache Miss Count: 14
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 22:
Memory Access Count: 22
Cache Hit Count: 7
Cache Miss Count: 15
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 23:
Memory Access Count: 23
Cache Hit Count: 7
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 24:
Memory Access Count: 24
Cache Hit Count: 8
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 25:
Memory Access Count: 25
Cache Hit Count: 9
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 26:
Memory Access Count: 26
Cache Hit Count: 10
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 27:
Memory Access Count: 27
Cache Hit Count: 11
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 28:
Memory Access Count: 28
Cache Hit Count: 12
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 29:
Memory Access Count: 29
Cache Hit Count: 13
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 30:
Memory Access Count: 30
Cache Hit Count: 14
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 31:
Memory Access Count: 31
Cache Hit Count: 15
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 32:
Memory Access Count: 32
Cache Hit Count: 16
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 33:
Memory Access Count: 33
Cache Hit Count: 17
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 34:
Memory Access Count: 34
Cache Hit Count: 18
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 35:
Memory Access Count: 35
Cache Hit Count: 19
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 36:
Memory Access Count: 36
Cache Hit Count: 20
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 37:
Memory Access Count: 37
Cache Hit Count: 21
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 38:
Memory Access Count: 38
Cache Hit Count: 22
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 39:
Memory Access Count: 39
Cache Hit Count: 23
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 40:
Memory Access Count: 40
Cache Hit Count: 24
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 41:
Memory Access Count: 41
Cache Hit Count: 25
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 42:
Memory Access Count: 42
Cache Hit Count: 26
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 43:
Memory Access Count: 43
Cache Hit Count: 27
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 44:
Memory Access Count: 44
Cache Hit Count: 28
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 45:
Memory Access Count: 45
Cache Hit Count: 29
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 46:
Memory Access Count: 46
Cache Hit Count: 30
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 47:
Memory Access Count: 47
Cache Hit Count: 31
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 48:
Memory Access Count: 48
Cache Hit Count: 32
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 49:
Memory Access Count: 49
Cache Hit Count: 33
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 50:
Memory Access Count: 50
Cache Hit Count: 34
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 51:
Memory Access Count: 51
Cache Hit Count: 35
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 52:
Memory Access Count: 52
Cache Hit Count: 36
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 53:
Memory Access Count: 53
Cache Hit Count: 37
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 54:
Memory Access Count: 54
Cache Hit Count: 38
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 55:
Memory Access Count: 55
Cache Hit Count: 39
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 56:
Memory Access Count: 56
Cache Hit Count: 40
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 57:
Memory Access Count: 57
Cache Hit Count: 41
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 58:
Memory Access Count: 58
Cache Hit Count: 42
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 59:
Memory Access Count: 59
Cache Hit Count: 43
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 60:
Memory Access Count: 60
Cache Hit Count: 44
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 61:
Memory Access Count: 61
Cache Hit Count: 45
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 62:
Memory Access Count: 62
Cache Hit Count: 46
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 63:
Memory Access Count: 63
Cache Hit Count: 47
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 64:
Memory Access Count: 64
Cache Hit Count: 48
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 65:
Memory Access Count: 65
Cache Hit Count: 49
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 66:
Memory Access Count: 66
Cache Hit Count: 50
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 67:
Memory Access Count: 67
Cache Hit Count: 51
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 68:
Memory Access Count: 68
Cache Hit Count: 52
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 69:
Memory Access Count: 69
Cache Hit Count: 53
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 70:
Memory Access Count: 70
Cache Hit Count: 54
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 71:
Memory Access Count: 71
Cache Hit Count: 55
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 72:
Memory Access Count: 72
Cache Hit Count: 56
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 73:
Memory Access Count: 73
Cache Hit Count: 57
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 74:
Memory Access Count: 74
Cache Hit Count: 58
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 75:
Memory Access Count: 75
Cache Hit Count: 59
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 76:
Memory Access Count: 76
Cache Hit Count: 60
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 77:
Memory Access Count: 77
Cache Hit Count: 61
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 78:
Memory Access Count: 78
Cache Hit Count: 62
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 79:
Memory Access Count: 79
Cache Hit Count: 63
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 80:
Memory Access Count: 80
Cache Hit Count: 64
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 81:
Memory Access Count: 81
Cache Hit Count: 65
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 82:
Memory Access Count: 82
Cache Hit Count: 66
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 83:
Memory Access Count: 83
Cache Hit Count: 67
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 84:
Memory Access Count: 84
Cache Hit Count: 68
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 85:
Memory Access Count: 85
Cache Hit Count: 69
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 86:
Memory Access Count: 86
Cache Hit Count: 70
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 87:
Memory Access Count: 87
Cache Hit Count: 71
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 88:
Memory Access Count: 88
Cache Hit Count: 72
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 89:
Memory Access Count: 89
Cache Hit Count: 73
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 90:
Memory Access Count: 90
Cache Hit Count: 74
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 91:
Memory Access Count: 91
Cache Hit Count: 75
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Step 92:
Memory Access Count: 92
Cache Hit Count: 76
Cache Miss Count: 16
Cache Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
```

The cache hit rate is influenced by the access pattern. In these test cases, a sequential access pattern tends to have a higher cache hit rate than the Random one. Due to the unpredictability of the random sequence, if a user wants more constant cache performance, the Sequential and Mid-Repeat Block sequence may be the better choice. 

## Contributors
- Leon Pablo
- Jan Relucio
- Sophia Perez
- Earl Guevara
