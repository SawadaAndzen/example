#Проста програма FastAPI - сайт, робота з git

import fastapi


app = fastapi.FastAPI()

@app.get("/")
def read_main_page():
    
    return "Main page was successfully read!"

#Ця програма просто передасть текст у головну сторінку програми, без йього просто б виводилося detail: Not Found