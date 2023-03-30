from primihub.client.ph_grpc.src.primihub.protos import common_pb2
from primihub.client.ph_grpc.worker import WorkerClient


from cloudpickle import dumps
import uuid
import json


def generate_task(func, node_config, task_parameter):
    '''
    Generate the context and feed to the server.
    Note there are 3 parts in the context, task_config, node_config and the task_parameter.
    In the submit process, the the task_config should be processed by the server, while the 
    node_config and task_parameter is transmit directly to the executor.
    '''


    #initialize the context
    #Note there are 3 parts in the context, 
    context = dict()

    #set the task_config, note the task config should be process by the scheduler 
    task_id = uuid.uuid1().hex
    context['task_config']['task_id'] = task_id

    dump_func = dumps(func)
    context['task_config']['func'] = dump_func

    role = task_parameter['role'] 

    context['task_config']['role'] = role #copy once in case of need in the task process
    context['task_config']['target_node'] = role

    #set the node_config
    context['node_config'] = node_config

    #set the task_parameter
    context['task_parameter'] = task_parameter

    return context



class FL_client:
    def __init__(self, node, cert) -> None:
        self.client = WorkerClient(node, cert)
    
    
    def submit(contexts):
        job_id = uuid.uuid1().hex
        task_ids = []
        submit_info = ""
        if not isinstance(contexts, list):
            task = [task]

        for context in contexts:
            context['task_config']['job_id'] = job_id
            t = dumps(context)
            submit_info += (t+",")
            task_ids.append({context['task_config']['role']: context['task_config']['task_id']})
        
        print(f'The job_id is {job_id}\n')
        print(f'The task_ids are {task_ids}')

        submit_info = submit_info[:-1] #remove the final ','

        self.client.submit(submit_info)

        return task_ids

    def get_status(task_id):
        self.client.get_status(task_id)
