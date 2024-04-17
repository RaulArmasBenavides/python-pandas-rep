import pandas as pd
import statsmodels.formula.api as smf
data  = pd.read_csv('advertising/advertising.csv')
data.head()

lm = smf.ols(formula="Sales~TV", data=data).fit()
print(lm)
print(lm.params)
print(lm.pvalues)
print(lm.rsquared)