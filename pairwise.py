#!/usr/bin/env python
# -*- coding: UTF-8 –*-

from mrjob.protocol import RawValueProtocol
from mrjob.protocol import RawProtocol
from mrjob.job import MRJob
from mrjob.compat import get_jobconf_value
import sys
import os
import datetime
import time

# 基本思路如下:
# 对于第i行，输出<i,1> <i,2>, .. <i,i-1>, <i+1,i>, <i+2,i>,<n,i>
# 输入数据格式为 index \t line
# 全部行
class PairwiseCmpTask(MRJob):
	OUTPUT_PROTOCOL = RawProtocol
	def mapper(self, _, l):
		t = l.strip('\n').split('\t')
		text = t[1]
		i = int(t[0])
		n = int(get_jobconf_value("total"))
		for j in range(1, i):
			yield(("%d,%d" % (i, j)), text)
		for j in range(i + 1, n + 1):
			yield(("%d,%d" % (j, i)), text)

	def reducer(self, ij, texts):
		text_l = []
		for text in texts:
			text_l.append(text)
		yield(ij, ','.join(text_l))

if __name__ == "__main__":
	j = PairwiseCmpTask()
	j.run()
