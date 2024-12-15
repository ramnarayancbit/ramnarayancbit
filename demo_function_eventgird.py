import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.synapse.artifacts import ArtifactsClient

app = func.FunctionApp()

@app.event_grid_trigger(arg_name="azeventgrid")
def EventGridProcessor(azeventgrid: func.EventGridEvent):
    logging.info("Python EventGrid trigger received an event")

    # Parse Event Data
    event_data = azeventgrid.get_json()
    file_name = event_data.get('data', {}).get('fileName', 'UnknownFile')
    logging.info(f"File received: {file_name}")

    # Trigger Synapse Pipeline
    try:
        synapse_endpoint = "https://synapasedemo.dev.azuresynapse.net"
        pipeline_name = "MetadataBasedIngestionPipeline_Aqwe"

        # Authenticate using Managed Identity
        credential = DefaultAzureCredential()
        client = ArtifactsClient(endpoint=synapse_endpoint, credential=credential)

        # Trigger the pipeline
        run_response = client.pipeline.create_pipeline_run(
            pipeline_name=pipeline_name,
            parameters={"fileName": file_name}
        )
        logging.info(f"Pipeline triggered successfully. Run ID: {run_response.run_id}")
    except Exception as e:
        logging.error(f"Error triggering Synapse pipeline: {e}")
