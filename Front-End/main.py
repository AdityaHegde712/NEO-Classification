from nicegui import ui, app
import asyncio
import tempfile
import os
from model import predict

@ui.page('/index')
def index_page():
    # Function definitions
    async def on_upload(e):
        if str(e.name).endswith('csv'):
            with open(os.path.join('C:/Users/hifia/Projects/ML Semester project/Front-End/uploads', e.name), mode='wb') as f:
                f.write(e.content.read())
            ui.notify(f"Uploaded and saved {e.name}")
            return
        await display_error_message()

    async def display_error_message():
        label = ui.label('Error: Invalid File Type!').classes('error')
        await asyncio.sleep(3)
        label.delete()
    
    async def processCSV():
        ui.notify("The model will now work")
        print(predict())

    # Styling
    ui.add_head_html('''
                    <link href="https://fonts.googleapis.com/css?family=Cairo+Play&display=swap" rel="stylesheet">
                    <style>
                        .subtitle {
                            font-family: 'Cairo Play', sans-serif;
                            font-size: 24px;
                            font-weight: bold;
                            margin-top: 50px;
                        }
                        .upload {
                            margin-left: auto;
                            margin-right: auto;
                            text-align: center;  
                        }
                        .error {
                            font-size: 18px;
                            font-family: 'Cairo Play', sans-serif;
                            font-color: red;
                            padding-left: 80px;
                            font-weight: bold;
                        }
                        .form {
                            font-family: 'Cairo Play', sans-serif;
                            font-size: 20px;
                            font-weight: bold;
                            justify-content: center;
                            width: 50%;
                            margin-left: 380px;
                            margin-top: 20px;
                            margin-right: 400px;
                        }
                    </style>       
             ''')
    
    # Navbar
    with ui.header(elevated=True).style('background-color: #4861f0; padding: 20px;').classes('items-center justify-between'):
        with ui.row().style('align-items: center;'):
            ui.image('C:/Users/hifia/Projects/ML Semester project/Front-End/resources/1.png').classes('w-10')
            ui.label("NEO Classification").style('font-size: 24px; font-weight: bold; color: #ffffff;')
        with ui.row():
            ui.button('Home', on_click=lambda: ui.notify('Go back home')).style('color: ##4861f0; text-decoration: none; margin-right: 20px;')
            ui.button('About', on_click=lambda: ui.notify('Go to footer')).style('color: ##4861f0; text-decoration: none;')
    
    # Content
    with ui.tabs().classes('w-full').style('margin-top: -120px; margin-left: auto; margin-right: auto; text-align: center;') as tabs:
        csv = ui.tab('CSV Report')

    with ui.tab_panels(tabs, value=csv).classes('w-full'):

        with ui.tab_panel(csv): # CSV Tab
            ui.label("Upload the CSV Reports here\n").classes('subtitle').style('text-align: center;'); ui.html('<br>')
            ui.upload(on_upload=on_upload, 
                    multiple=True, 
                    max_file_size=100000000, 
                    label="CSV file"
                    ).classes('upload')
            ui.add_body_html('<br><br>')
            ui.button(text="Get Probabilities", on_click=processCSV).classes('items-center upload').style('margin-top: 50px; display: flex; justify-content: center;')

index_page()
ui.run(favicon='Front-End\\resources\\1.png', port=5000)