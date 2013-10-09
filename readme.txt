1, 使用mapred实现输入文件行的两两比较，相当于生成了所有行的组合
2. 如何运行？
依赖mrjob， 安装pip install mrjob
上传input到hdfs，修改run.sh文件中的输入输出路径
3. 结果为output文件所示
4. 原理
例如对
1 a
2 b
3 c
4 d

map阶段：
读取a, 输出<2,1 a> <3,1 a> <4,1 a>
读取b，输出<2,1 b> |||| <2,3 b> <2,4 b>
读取c，输出<3,1 c> <3,2, c> |||| <4,3 c>
读取d，输出<4,1 d> <4,2 d> <4,3 d>

reduce阶段：
相同的key技能得到组合，执行compare方法即可，demo中只做了输出

5. 局限
需要预先知道总行数，通过total参数传入

6. 参考
http://dynamicorange.com/2012/12/31/pairwise-comparisons-of-large-datasets/

