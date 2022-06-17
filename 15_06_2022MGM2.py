'''ARS Gems Store sells different varieties of gems to its customers.

Write a Python program to calculate the bill amount to be paid by a customer based on 
the list of gems and
 quantity purchased. 
Any purchase with a total bill amount above Rs.30000 is entitled for 5% discount.
 If any gem required
 by the customer is not available in the store,
 then consider total bill amount to be -1.

Assume that quantity required by the customer for any gem will always be greater than 0.

Perform case-sensitive comparison wherever applicable.'''

def calculate_bill(req_gems, req_quantity, gems_list, price_list):
    bill_amount = 0
    for gem in req_gems:
        if gem in gems_list:
            i1 = gems_list.index(gem)
            i2 = req_gems.index(gem)
            bill_amount = bill_amount+(price_list[i1]*req_quantity[i2])
            if bill_amount>=30000:
                bill_amount = bill_amount*0.95
        else:
            return -1
    return bill_amount

req_quantity = [2,1,3]
req_gems = ['amber', 'opal','topaz']
gems_list = ['amber', 'opal','topaz','diamond']
price_list = [4392, 1342, 8734, 6421]
bill_amount = calculate_bill(req_gems, req_quantity, gems_list, price_list)
print(bill_amount)
