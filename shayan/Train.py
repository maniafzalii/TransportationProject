class Train():
    def __init__(self, name, move_line, speed: int, waiting_time: int, stars, ticket_price: int, capacity: int,
                 id: int):
        self.name = name
        self.moveline = move_line
        self.speed = speed
        self.waiting_time = waiting_time
        self.stars = stars
        self.ticket_price = ticket_price
        self.capacity = capacity
        self.id = id

    def __str__(self):
        return f"ID: {self.id}   name: {self.name}    move_line: {self.moveline}    average speed: {self.speed}" \
               f"    waiting_time: {self.waiting_time}    stars: {self.stars}    ticket_price: {self.ticket_price} " \
               f"   capacity: {self.capacity}"


trains = {}
train_id = 1
