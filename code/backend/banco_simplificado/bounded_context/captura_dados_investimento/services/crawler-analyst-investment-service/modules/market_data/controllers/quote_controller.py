from modules.market_data.services.quote_service import quote_service

class QuoteController:

    async def get_quote(self, ticker: str):
        return 'teste'

    async def teste_function(self):
        return self.quote_service.get_quote(ticker)

quote_controller = QuoteController()