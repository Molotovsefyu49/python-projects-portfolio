# Import the pandas library and load the hotels.csv file as a DataFrame.
import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})

# Load the cards.csv file as a DataFrame and convert it to a list of dictionaries.
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")

# Load the card-security.csv file as a DataFrame.
df_cards_security = pd.read_csv("card-security.csv", dtype=str)


# Define the Hotel class.
class Hotel:
    def __init__(self, hotel_id):
        # Set the hotel ID and name.
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """" Book a hotel by changing its availability to no"""
        # Set the availability of the hotel with the specified ID to "no" in the DataFrame.
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        # Save the updated DataFrame to the hotels.csv file.
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        # Get the availability of the hotel with the specified ID from the DataFrame.
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        # Return True if the hotel is available, False otherwise.
        if availability == "yes":
            return True
        else:
            return False


# Define the SpaHotel class, which inherits from the Hotel class.
class SpaHotel(Hotel):
    def book_spa_package(self):
        # This method is currently not implemented.
        pass


# Define the ReservationTicket class.
class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        # Set the customer name and hotel object.
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        # Generate a reservation ticket message with the customer name and hotel name.
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        
        """
        return content


# Define the CreditCard class.
class CreditCard:
    def __init__(self, number):
        # Set the credit card number.
        self.number = number

    def validate(self, expiration, holder, cvc):
        # Create a dictionary with the credit card data
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        # Check if the card data is in the list of card dictionaries.
        if card_data in df_cards:
            return True
        else:
            return False


# Define the SecureCreditCard class, which inherits from the CreditCard class.
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        # Get the password for the credit card from the card-security.csv file.
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        # Return True if the given password matches the stored password, False otherwise.
        if password == given_password:
            return True
        else:
            return False


# Define the SpaReservationTicket class.
class SpaReservationTicket:
    def __init__(self, customer_name, spa_hotel_object):
        """Create a new SpaReservationTicket object"""
        self.customer_name = customer_name
        self.hotel = spa_hotel_object

    def generate(self):
        """Generate a reservation ticket for a spa hotel"""
        content = f"""
        Thank you for your SPA reservation!
        Here are your SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}

        """
        return content


print(df)

# Prompt user to enter the ID of the hotel they want to book
hotel_ID = input("Enter the id of the hotel: ")
hotel = SpaHotel(hotel_ID)

if hotel.available():
    # Create a new SecureCreditCard object to validate and authenticate the credit card
    credit_card = SecureCreditCard(number='1234567890123456')
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            # Book the hotel
            hotel.book()
            name = input("Enter your name: ")
            # Generate a ReservationTicket for the hotel
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
            spa_package = input("Do you want to book a spa package?")
            if spa_package == 'yes':
                # Book a spa package
                hotel.book_spa_package()
                # Generate a SpaReservationTicket for the spa hotel
                spa_reservation_ticket = SpaReservationTicket(
                    customer_name=name, spa_hotel_object=hotel)
                print(spa_reservation_ticket.generate())
            else:
                print("Thank you for using our services!")

        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not free !")

