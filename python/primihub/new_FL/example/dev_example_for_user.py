from .dev_example_submit_task import Dev_example

node_config = {
    'task_manager' : '127.0.0.1:124',
    'guest': '127.0.0.1:1234',
    'host': '127.0.0.1:123'
}

data_path = {
    'guest':{
    'X':'guest_X',
    'y':'guest_y',
    },
    'host':{'X': 'host1_X'},
}


model = Dev_example(node_config = node_config, num_iter=10)


model.train(data = data_path)