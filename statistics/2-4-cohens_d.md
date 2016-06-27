[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>
'''
Exercise 4   Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?
'''
import nsfg, math

```python
#Data for pregnancies
preg = nsfg.ReadFemPreg()

#Only want live births
live = preg[preg.outcome == 1]
#Separate first births vs after first
first = live[live.birthord == 1]
after = live[live.birthord != 1]

#Cohens Effect
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

#Cohens Effect on total weight of first vs after first babies
CohenEffectSize(first.totalwgt_lb, after.totalwgt_lb)
```

Cohen's effect size is -0.08867
