class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        customer_capacity = 10
        return customer_capacity

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd.is_rented:
                            if dvd in customer.rented_dvds:
                                return f"{customer.name} has already rented {dvd.name}"
                            return "DVD is already rented"
                        if not dvd.is_rented and customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            for dvd in self.dvds:
                if customer.id == customer_id and dvd.id == dvd_id and dvd in customer.rented_dvds:
                    dvd.is_rented = False
                    customer.rented_dvds.remove(dvd)
                    return f"{customer.name} has successfully returned {dvd.name}"
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        # return "\n".join([repr(x) for x in self.customers]) + "\n" + "\n".join([repr(x) for x in self.dvds])
        result = []
        for customer in self.customers:
            result.append(customer.__repr__())
        for dvd in self.dvds:
            result.append(dvd.__repr__())
        return "\n".join(result)











