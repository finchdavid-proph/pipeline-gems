from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "a", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    a__customer_orders_left_join = Process(
        name = "a__customer_orders_left_join",
        properties = ModelTransform(modelName = "a__customer_orders_left_join"),
        input_ports = ["in_0", "in_1"]
    )

