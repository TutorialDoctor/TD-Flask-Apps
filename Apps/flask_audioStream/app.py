from flask import Flask, Response,redirect
#https://gist.github.com/hosackm/289814198f43976aff9b

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/mp3')

@app.route("/mp3")
def stream_mp3():
    def generate():
        # add your file to the music folder and change 'yourfile' the name of your file.
        with open("music/yourfile.mp3", "rb") as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)
    return Response(generate(), mimetype="audio/x-mp3")

if __name__ == "__main__":
    app.run(debug=True)