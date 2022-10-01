
from booking.booking import booking

with booking() as bot:
    bot.homepage()
    bot.choose_currency(currency="USD")
    bot.select_place(place='台中')
    bot.check_date(check_in='2022-06-27',check_out='2022-06-28')
    bot.select_adults(1)
    bot.search_page()
    bot.apply_filter(3,4,5)
    bot.sort_score_and_price()
    bot.refresh()
    bot.report()
