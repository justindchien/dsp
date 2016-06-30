[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```python
import scipy.stats

#Creating normal distribution based on mu and sigma given
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

#5'10" = 177.8 cm and 6'1" = 185.42 cm
fiveten = dist.cdf(177.8) # % people up to 5'10"
sixone = dist.cdf(185.42) # % people up to 6'1"
print(sixone - fiveten) # difference gives % between 5'10" and 6'1"
```

About 34.27% of the US male population is within the acceptable range of heights to join the Blue Man Group.
