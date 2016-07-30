#!/usr/bin/env python3

import xor.bf.machine as bf

n = list('.,_+[]<>')
raw_input="a"*1024

for i in n:
  for j in n:
    for k in n:
      for l in n:
        code = "{}{}{}{}".format(i,j,k,l)
        try:
            output = bf.evaluate(code,raw_input=raw_input,max_ticks=100)
            print("G",code,output)
        except Exception as e:
            print("E",code,e)
