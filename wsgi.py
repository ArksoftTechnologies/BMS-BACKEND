"""Application entry point."""
from API import create_app

app = create_app()

if __name__ == "__main__":
    #run on local server
    app.run(host="0.0.0.0")

    # run on wifi
    # app.run(host="192.168.43.7", port=5000)
