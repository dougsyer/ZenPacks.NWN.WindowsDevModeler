This zenpack adds three new roles

ZenPowerUser - designed to allow event management as well
               as ability to remodel devices and remove components
               and edit zproperties

ZenNocOperator - ability to view devices, manage events, 
                 and edit maintenance windows

ZenCustomerPowerUser - designed to allow View priviliges
                       and ability to set maintenance windows on devices
                       Note, this is not to be used as a global role
                       It should be assigned as documented below:


To set up a Customer for Portal Use:

1.  Create a NEW OU in Ad for customer
2.  Create a Group under the customer
3.  Create customer users in AD and assign to the group created
4.  For any customer-specific groups or locations do the following:
	4.1  in zenoss admin, go to manage users, select the group created
        4.2  under manage admin roles, add the user group to specific
             device groups or locations housing cusotmer devices
             and select the "ZenNWNCustomers" role


