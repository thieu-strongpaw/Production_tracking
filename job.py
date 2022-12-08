# Matt Garcia
# CIS-2531
# 11/27/22
# Final Project
# This is the modual for the jobs

class Job:
    """This class will make Job Objects to store info for jobs"""

    def __init__(self, job_id=0, part='', production_rate=0, order_quantity=0):

        self.__job_id = job_id
        self.__part = part
        self.__production_rate = production_rate
        self.__order_quantity = order_quantity

    @property
    def job_id(self):
        """Returns job_id attribute"""
        return self.__job_id
    
    @job_id.setter
    def job_id(self, job_id):
        """Sets job_id attribute"""
        self.__job_id = job_id

    @property
    def part(self):
        """Returns part attribute"""
        return self.__part
    
    @part.setter
    def part(self, part):
        """Sets part attribute"""
        self.__part = part

    @property
    def production_rate(self):
        """Returns production_rate attribute"""
        return self.__production_rate
    
    @production_rate.setter
    def production_rate(self, production_rate):
        """sets production_rate attribute"""
        self.__production_rate = production_rate

    @property
    def order_quantity(self):
        """Returns order_quantity attribute"""
        return self.__order_quantity
    
    @order_quantity.setter
    def order_quantity(self, order_quantity):
        """Sets order_quantity attribute"""
        self.__order_quantity = order_quantity

    def projected_run_time(self):
        """Returns the projected time needed to complete this order."""
        run_time = self.__order_quantity / self.__production_rate
        return run_time

    def __str__(self):
        """Returns object state in string form"""
        displayString = str('Job ID :{:>14}\nPart :{:>16}\nOrder Quantity : {:}\nProduction Rate :{:}'.format(self.__job_id, self.__part, self.__order_quantity, self.__production_rate))
        return displayString

def main():
    job1 = Job()
    job1.job_id = 95895
    job1.part = 'R8558'
    job1.order_quantity = 6000
    job1.production_rate = 6000
    print(job1)

if __name__ == '__main__':
    main()