# Producer-Consumer-microservice

## Screens
![Screenshot 2023-09-25 at 00.32.23.png](README_images%2FScreenshot%202023-09-25%20at%2000.32.23.png)
![Screenshot 2023-09-25 at 00.31.13.png](README_images%2FScreenshot%202023-09-25%20at%2000.31.13.png)

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