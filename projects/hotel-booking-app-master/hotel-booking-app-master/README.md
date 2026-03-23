# What is this project?

This Python script demonstrates a simple booking system for hotels with some basic features like booking a hotel, checking availability, generating a reservation ticket, validating credit cards, and booking spa packages.

The script uses the pandas library to read data from three CSV files: "hotels.csv", "cards.csv", and "card-security.csv". It then defines several classes:

Hotel: A class that represents a hotel with a name, ID, and availability status. It also has methods to book the hotel and check if it's available.

SpaHotel: A subclass of Hotel that adds a method to book a spa package.

ReservationTicket: A class that generates a reservation ticket with the customer's name and the name of the hotel they booked.

CreditCard: A class that validates credit card information, including the card number, expiration date, cardholder name, and CVC code.

SecureCreditCard: A subclass of CreditCard that adds a method to authenticate the card with a password.

SpaReservationTicket: A subclass of ReservationTicket that generates a reservation ticket for a spa package booking.

The script prompts the user to enter the ID of the hotel they want to book, then checks if it's available. If it's available, it prompts the user to enter their name and credit card information. If the credit card information is valid and authenticated, it books the hotel and generates a reservation ticket. If the user wants to book a spa package, it books the package and generates a spa reservation ticket. If the hotel is not available, it informs the user.
