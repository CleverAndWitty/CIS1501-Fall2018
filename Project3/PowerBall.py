import random

class PowerBallTicket:
    TICKET_PRICE = 2

    def __init__(self, white_balls = [], red_ball = 0):
        if len(white_balls) > 0:
            self._white_balls = white_balls
        else:
            self._white_balls = random.sample(range(1, 60), 5)
        if red_ball != 0:
            self._red_ball = red_ball
        else:
            self._red_ball = random.randint(1, 26)

    def __str__(self):
        return "{} PowerBall: {}"\
            .format(" ".join(str(ball) for ball in self._white_balls), str(self._red_ball))

    def get_winnings(self, winning_ticket):
        matching_white_balls = 0
        for white_ball in self._white_balls:
            if white_ball in winning_ticket._white_balls:
                matching_white_balls += 1
        red_ball_matches = self._red_ball == winning_ticket._red_ball

        if matching_white_balls == 0 and not red_ball_matches:
            return 0
        elif matching_white_balls == 1 and not red_ball_matches:
            return 0
        elif matching_white_balls == 2 and not red_ball_matches:
            return 0
        elif matching_white_balls == 0 and red_ball_matches:
            return 4
        elif matching_white_balls == 1 and red_ball_matches:
            return 4
        elif matching_white_balls == 2 and red_ball_matches:
            return 7
        elif matching_white_balls == 3 and not red_ball_matches:
            return 7
        elif matching_white_balls == 3 and red_ball_matches:
            return 100
        elif matching_white_balls == 4 and not red_ball_matches:
            return 100
        elif matching_white_balls == 4 and red_ball_matches:
            return 50000
        elif matching_white_balls == 5 and not red_ball_matches:
            return 1000000
        elif matching_white_balls == 5 and red_ball_matches:
            return 1000000000


total_spent = 0
total_won = 0

tickets_to_buy = int(input("How many tickets to buy? 0 to quit"))
winning_ticket = PowerBallTicket()
while tickets_to_buy != 0:
    total_spent += tickets_to_buy * PowerBallTicket.TICKET_PRICE
    for ticket in range(tickets_to_buy):
        ticket = PowerBallTicket()
        total_won += ticket.get_winnings(winning_ticket)
    print("Total Spent: ${} Total Won : ${} Net Loss: ${}".format(
        total_spent, total_won, total_spent - total_won))
    tickets_to_buy = int(input("How many tickets to buy? 0 to quit"))

winning_ticket = PowerBallTicket([1,2,3,4,5], 6)
ticket = PowerBallTicket([5,4,3,2,1], 6)
print("Expecting $1,000,000,000 - Got: {}".format(str(ticket.get_winnings(winning_ticket))))

winning_ticket = PowerBallTicket([1,2,3,4,5], 7)
ticket = PowerBallTicket([5,4,3,2,1], 6)
print("Expecting $1,000,000 - Got: {}".format(str(ticket.get_winnings(winning_ticket))))
