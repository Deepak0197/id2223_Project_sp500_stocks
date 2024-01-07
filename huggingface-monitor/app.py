import gradio as gr
from PIL import Image
import hopsworks

project = hopsworks.login()
fs = project.get_feature_store()

dataset_api = project.get_dataset_api()

dataset_api.download("Resources/images/latest_sp500.png", overwrite=True)
dataset_api.download("Resources/images/actual_sp500.png", overwrite=True)
dataset_api.download("Resources/images/df_recent.png", overwrite=True)

with gr.Blocks() as demo:
    with gr.Row():
      with gr.Column():
          gr.Label("Today's Predicted Stock Direction")
          input_img = gr.Image("latest_sp500.png", elem_id="predicted-img")
      with gr.Column():          
          gr.Label("Today's Actual Stock Direction")
          input_img = gr.Image("actual_sp500.png", elem_id="actual-img")        
    with gr.Row():
      with gr.Column():
          gr.Label("Recent Prediction History")
          input_img = gr.Image("df_recent.png", elem_id="recent-predictions")      

demo.launch()