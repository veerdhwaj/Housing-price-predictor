
# The below code is for the most basic prediction that can be done on the data without any changes to the train set

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

train = pd.read_csv('../input/house-prices-advanced-regression-techniques/train.csv')
housing_price=train.SalePrice
X=['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']
deciding_factor=train[X]
forest_model=RandomForestRegressor()
forest_model.fit(deciding_factor,housing_price)

test=pd.read_csv('../input/house-prices-advanced-regression-techniques/test.csv')
test_predictors=test[X]
predicted_price=forest_model.predict(test_predictors)
my_submission = pd.DataFrame({'Id': test.Id, 'SalePrice': predicted_price})
my_submission.to_csv('../submission.csv', index=False)
