# Matt Garcia
# 11/27/22
# CIS 2531
# Final Project
# This program will store information about production levels for a manufacturing process. 
# This is the modual for the Press


# Class for the workstation, a punch press.
class Press:
    """This class will make a Press Object."""
    
    def __init__(self, press_id='', employee_id=0, job_list = []):
        
        self.__press_id = press_id
        self.__employee_id = employee_id
        self.__job_list = list(job_list)

    @property
    def press_id(self):
        """Method to return the __press_id attribute"""
        return self.__press_id

    @press_id.setter
    def press_id(self, press_id):
        """Method to set the __press_id attribute"""
        self.__press_id = press_id

    @property
    def employee_id(self):
        """Method to set the employee_id attribute"""
        return self.__employee_id
    
    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

    def add_job(self, job):
        """Adds job to job list. Expects a Job Object"""
        self.__job_list.append(job)

    def del_job(self):
        """"This will delete the last job added to the list"""
        self.__job_list.pop()

    def job_list(self):
        return self.__job_list

    def __str__(self):
        """Returns object state in string form"""
        displayString = str('Press ID       : {}\nOperator ID    : {}\nNumber of jobs : {}'.format(self.press_id,self.employee_id, str(len(self.__job_list))))
        return displayString

def main():
    press1 = Press()
    press2 = Press(press_id='bl')
    press1.employee_id = 33
    press1.press_id = 'BL-02'
    press1.add_job('a')
    print(press1.job_list())
    print(press2.job_list())
    print(press2)


    #print(type(press1.__job_list))
    #print(type(press2.__job_list))



    input('')

if __name__ == '__main__':
    main()