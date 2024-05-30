from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency("RUB")
    bot.change_destination("New York")
    bot.change_dates("2025-05-29", "2025-05-30")
    print("Exiting Booking Bot...")
