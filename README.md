# chat

This is an small chat app based on Flask microframework.
It uses SqlAlchemy as ORM and SQlite as Database and pytest for unittesting

1. Currently only supports one chat room
2. It supports one session per browser, so to test the chat with different users you must start a session
    with different users on different browser.
3. To register a user only is required an email and password
4. If a user was already registered it must provide a valid password.
5. To test the bot write /stock=stock_code as a command in the input box. The "StockBot" should answer with a stock quote in the case the stock_code is valid. In other case the Bot answer with a polite message.
6. Only the last 50 messages are displayed ordered by date

## Dependencies

1. Be sure of having python3 and virualenv
2. create virtual environment
    py -3 -m virtualenv venv
3. active virtualenv
    (linux): source venv/bin/active
    (windows): source venv/Scripts/activate
4. pip install -r requirements-dev.txt

## Running on localhost

1. python main.py -> The application will be running on localhost:5000

## Tests

1. pytest -> by default pytest will look for files with the sufix test_ into the tests folder.
