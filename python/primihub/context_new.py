'''
Generally, to run a task there are several important parts for a task.
1. The task configure (format fix): for the task, i.e. the task type, ID, also the function
2. The node configure (format fix): mainly for the communcation, the node configuraion is used
    communcation with other nodes and check the node info.
3. The task parametes (format is defined by user): The parameter fo the special algorithm.
Note, the dataset is also included in this parameter.
'''

class ContextAll:
    '''
    All the parameter is included in this context.
    '''
    def __init__(self, task_config=dict(), node_config=dict(), task_parameter=dict()) -> None:
        self.task_config = task_config
        self.node_config = node_config
        self.task_parameter = task_parameter

Context = ContextAll()

def set_task_config(key, val):
    Context.task_config[key] = val


def set_node_config(key, val):
    Context.node_config[key] = val

def set_task_parameter(key, val):
    Context.task_parameter[key] = val



