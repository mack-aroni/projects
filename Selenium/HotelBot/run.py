from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.select_currency("USD")
        bot.select_destination("New York")
        bot.select_dates("2025-05-29", "2025-05-30")
        bot.select_adults_rooms(5, 2)
        bot.select_children(2, [12, 13])
        bot.search()
        bot.apply_filters()
        print("Exiting Booking Bot...")
except Exception as e:
    if "in PATH" in str(e):
        print("There was an error executing this program from command line")
    else:
        raise
