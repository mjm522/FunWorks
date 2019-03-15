import numpy as np
# from sklearn import linear_model

class MarketingCosts:

    # param marketing_expenditure list. Expenditure for each previous campaign.
    # param units_sold list. The number of units sold for each previous campaign.
    # param desired_units_sold int. Target number of units to sell in the new campaign.
    # returns float. Required amount of money to be invested.
    @staticmethod
    def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
        
        Y = np.vstack([ np.array([marketing_expenditure]), np.ones(len(marketing_expenditure)) ] )
        X = np.vstack([ np.array([units_sold]), np.ones(len(units_sold)) ] )

        model = Y.dot(Y.T).dot(np.linalg.inv(X.dot(Y.T)))
        
        pred = model.dot(np.array([ [desired_units_sold], [1] ] ))
        
        return pred[0]

#For example, with the parameters below the function should return 250000.0.
print(MarketingCosts.desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))