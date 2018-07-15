# user should be shown the number of tickets left
# user should have a personalized experience
# user should have errors reported in a friendly manner
# user should be able to request a certain amount of tickets
# user should be presented total cost before purchasing
# user should be able to confirm order
# user should not be offered tickets if there are none available
# user should be able to purchase with credit card or Bitcoin

import sys

TICKET_PRICE = 10
SERVICE_CHARGE = 2.00


def ticket_total(num):
    return num * TICKET_PRICE


def master_ticket():
    num_of_tickets = 10
    print("Welcome to Master Ticket!")

    username = input("Please enter your name: ")

    print("Hello {}, there are {} ticket(s) remaining.".format(username, num_of_tickets))

    while num_of_tickets > 0:

        try:
            purchase_num = input("{}, how many tickets would you like to purchase? ".format(username))

            if purchase_num.lower() == "exit":
                print("Thank you for choosing Master Ticket. Goodbye.")
                sys.exit()

            elif int(purchase_num) > num_of_tickets:
                print("There are only {} tickets available for purchase.".format(num_of_tickets))

            elif int(purchase_num) < 1:
                print("You must purchase at least one ticket.")

            else:
                total = ticket_total(int(purchase_num))
                confirm_order = input("Would you like to purchase {} ticket(s) for ${} [Y/N]? ".format(purchase_num, total))

                order_confirmed = False

                while order_confirmed == False:

                    if confirm_order.lower() == "y" or confirm_order.lower() == "yes":

                        try:
                            payment_method = input("Payment Options: Enter 1 for Credit, 2 for BitCoin: ")

                            if payment_method == "1" or payment_method == "2":
                                charge_confirm = input("There is a $2.00 service charge for each transaction, "
                                                       "do you accept [Y/N]? ")

                                if charge_confirm.lower() == "yes" or charge_confirm.lower() == "y":
                                    print("Your total is ${}0.".format(total + SERVICE_CHARGE))
                                    num_of_tickets -= int(purchase_num)

                                    print("Your payment has been accepted, thank you for your purchase.")

                                    order_confirmed = True

                                elif charge_confirm.lower() == "no" or charge_confirm.lower() == "n":
                                    print("Service charge declined.")
                                    break

                                else:
                                    print("Please enter Yes or No.")

                            elif payment_method.lower() == "cancel":
                                break

                        except ValueError:
                            continue

                    elif confirm_order.lower() == "n" or confirm_order.lower() == "no":
                        break

                    else:
                        print("Please enter Yes or No.")
                        continue

                print("There are {} ticket(s) remaining.".format(num_of_tickets))

        except ValueError:
            print("There are {} ticket(s) remaining, please enter a valid amount.".format(num_of_tickets))

    print("We are currently sold out. Thank you for shopping with Master Ticket.")


master_ticket()
