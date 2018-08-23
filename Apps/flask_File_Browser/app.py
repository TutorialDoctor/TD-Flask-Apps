from flask import Flask,jsonify,url_for,render_template,request,abort,send_file,send_from_directory
import os,fnmatch

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',e=e), 404
  
@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):
  cwd = os.getcwd()
  BASE_DIR = cwd
  #BASE_DIR = '/Users/RamonSuthers/Desktop/File_Browser'
  # Joining the base and the requested path
  #dir_path = os.path.dirname(os.path.realpath(req_path)
  abs_path = os.path.join(BASE_DIR,req_path)
  # Return 404 if path doesn't exist
  if not os.path.exists(abs_path):
    full_path = BASE_DIR+'/documents/'+req_path
    directory = os.path.dirname(abs_path)
    with open(full_path,'r') as infile:
      return render_template('index.html',content=infile.read(),directory=directory)
    #return abort(404)
  
  # Check if path is a file and serve
  if os.path.isfile(abs_path):
    return request.url
    #return send_file(BASE_DIR+'/templates/'+req_path)
    
  # Show directory contents
  files = os.listdir(abs_path)
  return render_template('files.html', files=files)

if __name__ == '__main__':
  app.run(debug=True,port=5000)