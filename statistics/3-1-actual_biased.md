[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python

import chap01soln, thinkstats2, thinkplot

#Data of responses
resp = chap01soln.ReadFemResp()

#Make PMF of observed responses
pmf = thinkstats2.Pmf(resp.numkdhh, label = 'Observed')

#Define biased pmf w/ oversampling proportional to value
def BiasPmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

#Making biased pmf
a = BiasPmf(pmf, label='Biased')

#Plotting both PMFs on same axis
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, a])
thinkplot.Show(xlabel='# Kids < 18 years old', ylabel='PMF')

#Compute means of both PMFs
print ('mean of observed: ', pmf.Mean())
print ('mean of biased: ', a.Mean())
```
PMF Graph

![PMF](https://github.com/justindchien/dsp/blob/master/statistics/PMF_graph.png?raw=true)

mean of observed:  1.02420515504
mean of biased:  2.40367910066

Makes sense because the biased mean would be higher due to none of the families without children having any responses.
