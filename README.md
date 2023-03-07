## Microservices example with three models: user, product, transaction

Services: 
1. A new transaction every minute.
2. Read all transactions from the database and multiplies price by quantity and stores it in amount and change status to "sending". 
3. Sending email to user with the total amount, and changing status to "sent".
4. Printing all transactions