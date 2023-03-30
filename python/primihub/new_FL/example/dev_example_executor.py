import sys
import logging
import primihub as ph
import time
LOG_FORMAT = "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s] %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
logger = logging.getLogger("proxy")

# define a remote method
@ph.context.function(role='host', protocol='xgboost', datasets=["psi_client_data"], port="*:5555")
def func1(value=1):
    print("params: ", str(value))
    #print(node.to_string())
    link_context = ph.context.Context.get_link_conext()
    node = ph.context.Context.Node("127.0.0.1", 60051, False)
    #print(node.to_string())
    channel = link_context.getChannel(node)
    send_buf = "1111111111111111111111111111111111111111"
    channel.send("test_key1", send_buf)

    local_node = ph.context.Context.Node("127.0.0.1", 60050, False)
    local_channel = link_context.getChannel(local_node)
    recv_data = local_channel.recv("test_key")


# define a remote method
@ph.context.function(role='guest', protocol='xgboost', datasets=["psi_server_data"], port="localhost:5555")
def func2(value=2):
    logger.debug("params: ", str(value))
    logger.debug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    link_context = ph.context.Context.get_link_conext()
    node = ph.context.Context.Node("127.0.0.1", 60050, False)
    channel = link_context.getChannel(node)
    send_buf = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    channel.send("test_key", send_buf)

    local_node = ph.context.Context.Node("127.0.0.1", 60051, False)
    channel_local = link_context.getChannel(local_node)
    recv_buf = channel_local.recv("test_key1")