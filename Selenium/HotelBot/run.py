from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency("RUB")
    bot.change_destination("New York")
    print("Exiting Booking Bot...")
