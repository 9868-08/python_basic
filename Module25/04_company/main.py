class Person:
    def __init__(self, worth=100):  # worth - стоимость
        self.__name = "anonymous"
        self.__last_name = "anonymous"
        self.__age = 30


class Employee:
    def __init__(self):
        pass


class Manager(Employee):  # менеджер

    def __init__(self, manager_name):
        self.manager_name = manager_name
        self.salary = None  # Фиксированная, обычно ежемесячная оплата работы, оклад

    def def_salary(self):
        self.salary = 13000
        return self.salary

    def __str__(self):
        return self.manager_name


class Agent(Employee):  # агент

    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.salary = None

    def def_salary(self, def_sales):
        self.salary = 5000 + def_sales * 0.05
        return self.salary

    def __str__(self):
        return self.agent_name


class Worker(Employee):  # рабочий

    def __init__(self, worker_name):
        self.worker_name = worker_name
        self.salary = 0  # Фиксированная, обычно ежемесячная оплата работы, оклад

    def def_salary(self, def_work_time):
        self.salary = 100 * work_time
        return self.salary

    def __str__(self):
        return self.worker_name

from random import randint
sales = 5000
work_time = 100
manager_1 = Manager('manager number:' + str(randint(0, 9)))
manager_2 = Manager('manager number:' + str(randint(10, 19)))
manager_3 = Manager('manager number:' + str(randint(20, 29)))
managers = (manager_1, manager_2, manager_3)
for manager in managers:
    print(manager.__str__(), "sallary", manager.def_salary())

agent1 = Agent('agent number:' + str(randint(0, 9)))
agent2 = Agent('agent number:' + str(randint(10, 19)))
agent3 = Agent('agent number:' + str(randint(20, 29)))
agents = (agent1, agent2, agent3)
for agent in agents:
    print(agent.__str__(), "sallary", agent.def_salary(sales))

worker_1 = Worker('worker number:' + str(randint(0, 9)))
worker_2 = Worker('manager number:' + str(randint(10, 19)))
worker_3 = Worker('manager number:' + str(randint(20, 29)))
wokers = (worker_1, worker_2, worker_3)
workers = (worker_1, worker_2, worker_3)
for worker in workers:
    print(worker.__str__(), "salary", worker.def_salary(work_time))
