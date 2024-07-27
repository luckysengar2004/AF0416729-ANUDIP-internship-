# Q-1 - Calculate the total revenue genrated by two product categories in store.
import numpy as np

category1_revenue=np.array([500,600,700,550])
category2_revenue=np.array([450,700,800,600])
Total_revenue = category1_revenue+category2_revenue
print("Total revenue:-",Total_revenue)

# Q-2 - Calculate the profit made by the company
import numpy as np

revenue=np.array([10000,12000,11000,10500])
expenses=np.array([4000,5000,4500,4800])
profit=revenue - expenses
print("Profit is :- ",profit)

# Q-3 - Determine which the product in a store are out of stock(quantity is 0).
import numpy as np
Inventory=np.array([10,0,5,0,20,0])
print("Out of stock  product are:-",Inventory[Inventory==0])

# Q-4 - Calculate the total cost of items in a shoping cart,considering the quantity and price per item.

import numpy as np

quantity=np.array([2,3,4,1])
price_per_item=np.array([10.0,5.0,8.0,12.0])

print(" Total cost of items:- ",quantity*price_per_item)