# Using the `time` Unix command

The Unix `time` utility may be useful as an external Python measure.

To run the `time` utility type:
```bash
time -p python 01_simple_timer.py
```

which gives the output:
```
Total time running 'expensive_function': 0.4853651523590088 seconds
real 0.53
user 0.52
sys 0.01
```

The first line comes from the decorator we defined, and the other three:

- Real indicates the total time spent executing the script.
- User indicates the amount of time the CPU spent executing the script
- Sys indicates the amount of time spent in kernel-level functions.

The difference between the real time and the sum of user+sys may indicate the time spent waiting for input/output
or that the system is busy running other external tasks.
