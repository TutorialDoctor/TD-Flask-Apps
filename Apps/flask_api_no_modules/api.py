from app import app,request


@app.route('/people',methods=["get","post"])
def People():
    if request.method == "GET":
        return "people"
    if request.method == 'POST':
        return "posted"
    if request.method == 'PUT':
        return "puted"
    if request.method == "DELETE":
        return "delted"
    # Couldn't use ELIFS without a view type-error
