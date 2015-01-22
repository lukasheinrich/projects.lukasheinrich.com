from flask import Blueprint, send_from_directory, jsonify

blueprint = Blueprint('fileserver', __name__,template_folder='templates')

import os
import subprocess
from flask import Response

@blueprint.route('/')
def list():
  p = subprocess.Popen(['find','.'],stdout = subprocess.PIPE)
  return Response(p.stdout.readlines(), mimetype='text/plain')

@blueprint.route('/<path:filepath>')
def serve_file(filepath):
  return send_from_directory(os.path.dirname(filepath),os.path.basename(filepath))

