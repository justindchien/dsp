[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
import random, thinkstats2, thinkplot

#Creating 1,000 random numbers
numbers = []
for i in range(1000):
    numbers.append(random.random())

#Creating PMF and CDF
pmf = thinkstats2.Pmf(numbers, label='PMF')
cdf = thinkstats2.Cdf(numbers, label='CDF')

#Plot PMF
thinkplot.PrePlot(2)
thinkplot.Pmf(pmf)
thinkplot.Show(xlabel='Number',ylabel='PMF')

#Plot CDF
thinkplot.PrePlot(2)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='Number',ylabel='CDF')
```

#PMF Graph

![Rand_Num_PMF](https://github.com/justindchien/dsp/blob/master/statistics/rand_num_PMF.png?raw=true)

#CDF Graph

![Rand_Num_CDF](https://github.com/justindchien/dsp/blob/master/statistics/rand_num_CDF.png?raw=true)

The PMF graph is not a good visualization tool for the data. CDF line is relatively straight and seems to reflect a uniform distribution from 0 to 1.
