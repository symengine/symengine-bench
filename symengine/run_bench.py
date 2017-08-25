from subprocess import Popen, PIPE, TimeoutExpired
import json
import os
import signal

test1 = ["expand2", list(range(4, 15, 2))]
test2 = ["expand6", list(range(100, 300, 100))]
test4 = ["expand6b", list(range(100, 300, 100))]
test3 = ["expand7", list(range(10, 50, 3))]
test5 = ["symengine_bench", list(range(10, 15, 2))]

tests = [test1, test2, test3, test4, test5]
for test in tests:
    name = test[0]
    param = test[1][:]
    #for b in range(6):
    for b in range(1):
        lib = ["./%s %s","./%s_ginac %s", "./%s.m %s", "./%s.py %s", "maple -q %s.mpl -D n=%s", "./%s_piranha %s"][b]
        time = [float('inf')] * len(test[1])
        for i in range(len(param)):
            test_name = lib % (name, param[i])
            #command = 'LD_PRELOAD=/usr/lib/libtcmalloc.so '+test_name
            command = test_name
            with Popen(command, shell=True, stdout=PIPE, preexec_fn=os.setsid) as process:
                try:
                    output = process.communicate(timeout=120)[0]
                    #print(output, command)
                    time[i] = float(output.splitlines()[0].decode('utf-8').replace("ms", "").strip())
                    time[i] = max(0.01, time[i])
                except TimeoutExpired:
                    os.killpg(process.pid, signal.SIGINT) # send signal to the process group
                    break
            print(test_name, time[i])
        test.append(time)
        print(time)
with open('data.json', 'w') as f:
    f.write(json.dumps(tests, indent=2))
