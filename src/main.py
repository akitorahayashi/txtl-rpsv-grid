from app import HelloWorldApp

CSS_PATH = "static/css/main.css"

if __name__ == "__main__":
    app = HelloWorldApp()
    app.theme = "nord"
    app.run()
