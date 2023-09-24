# Producer-Consumer-microservice

## Screens
![Screenshot 2023-09-25 at 00.03.07.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Frd%2Fswqwf1q94z11v7m4j9vjcqy00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_acErJo%2FScreenshot%202023-09-25%20at%2000.03.07.png)
![Screenshot 2023-09-25 at 00.13.18.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Frd%2Fswqwf1q94z11v7m4j9vjcqy00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_9ed2r1%2FScreenshot%202023-09-25%20at%2000.13.18.png)

## Fetches
* Creation of "Order" and "Employee" models for order and employee management.
* A Celery task that automatically creates orders every minute.
* Addition of a button to delete orders with deletion notifications.
* Ability to create users with specified chat IDs.
* Integration with Telegram for sending notifications.

### Telegram Integration
To integrate with Telegram, follow these steps:

* Click on the Telegram icon in the admin panel.
* Enter the chat ID for the user.
* The chat ID will be saved in cookies.
* When an order is deleted, a notification will be sent to the specified Telegram chat.

## Getting Started
```
git clone git@github.com:Polyakiv-Andrey/Producer-Consumer-microservice.git 
pip install -r requirements.txt
python manage.py migrate
```
create .env file 
```
python manage.py runserver
redis-server
celery -A Producer_Consumer_microservice worker --loglevel=info 
celery -A Producer_Consumer_microservice beat --loglevel=info   
 ```