import pytest

from app.bot.service import BotService


@pytest.mark.parametrize("stock_code", [('aapl.us', "")])
def test_stock(stock_code):

    def string_isnumeric(quote):
        try:
            float(quote)
            return True
        except ValueError:
            return False

    bot_service = BotService()
    quote = bot_service.quote_stock(stock_code)

    assert string_isnumeric(quote)