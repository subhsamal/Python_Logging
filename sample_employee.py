import logging

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')


class Employee:
    """ A sample Employee class """

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info("Created Employee: {} {}".format(first, last))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Jus', 'Preet')
emp2 = Employee('Tom', 'Hardy')
emp3 = Employee('Michael', 'Ross')
