from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "b", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    b__customer_orders_left_join = Process(
        name = "b__customer_orders_left_join",
        properties = ModelTransform(modelName = "b__customer_orders_left_join"),
        input_ports = ["in_0", "in_1"]
    )

