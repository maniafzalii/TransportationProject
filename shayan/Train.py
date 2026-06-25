class Train():
    def __init__(self, name, move_line, speed: int, waiting_time: int, stars, ticket_price: int, capacity: int):
        self.name = name
        self.moveline = move_line
        self.speed = speed
        self.waiting_time = waiting_time
        self.stars = stars
        self.ticket_price = ticket_price
        self.capacity = capacity
        self.id = 1  # default for now - you can change it

    def __str__(self):
        return f"{BLUE}{self.id}---->{RESET}     name: {self.name} -- move_line: {self.moveline} -- average speed:{self.speed}" \
               f" -- waiting_time: {self.waiting_time} -- stars : {self.stars} -- ticket_price: {self.ticket_price} -- capacity : {self.capacity}"


trains = {}

BLUE = '\033[94m'
RESET = '\033[0m'
RED = '\033[91m'
