from dev_example_guest import Dev_example_guest
from dev_example_host import Dev_example_host
from client import Client, generate_task
class Dev_example:
    def __init__(self, node_config, num_iter = 10):
        
        #choose the task_manager to submit the task. 
        self.client = Client.init(node_config['task_manager'])
        self.node_config = node_config
        self.param = dict()
        self.param['num_iter'] = num_iter

    def train(self, data):
        #init the task_list
        task_list = []

        #set commom paramerter
        task_parameter = dict()
        task_parameter['param'] = self.param
        task_parameter['data'] = data
        task_parameter['process'] = 'train'
        

        #submit task for guest
        task_parameter['role'] = 'guest'
        task_list.append(generate_task(func = Dev_example_guest.run, node_config = self.node_config, task_parameter = task_parameter))


        #submit task for host
        task_parameter['role'] = 'host'
        task_list.append(generate_task(func = Dev_example_host.run, node_config = self.node_config, task_parameter = task_parameter))

        #submit the task and get the task ID
        task_ids = self.client.submit(task_list)

        #query the status of the task if needed
        #status = self.client.get_status(task_ids[0])
            


