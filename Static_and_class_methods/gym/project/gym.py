class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = ""
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                result += subscription.__repr__()+"\n"
        for customer in self.customers:
            if customer.id == subscription_id:
                result += customer.__repr__()+"\n"
        for trainer in self.trainers:
            if trainer.id == subscription_id:
                result += trainer.__repr__()+"\n"
        for equipment in self.equipment:
            if equipment.id == subscription_id:
                result += equipment.__repr__()+"\n"
        for plan in self.plans:
            if plan.id == subscription_id:
                result += plan.__repr__()

        return result
