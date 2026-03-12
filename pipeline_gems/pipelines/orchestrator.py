from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "orchestrator", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    pipeline_0 = Process(
        name = "Pipeline_0",
        properties = PipelineTrigger(enableMaxTriggers = True, pipelineName = "a", parameterSet = "default")
    )
    trigger_pipeline_b = Process(
        name = "trigger_pipeline_b",
        properties = PipelineTrigger(triggerCondition = "AllSuccess", pipelineName = "b", parameterSet = "default")
    )
    pipeline_0 >> trigger_pipeline_b
