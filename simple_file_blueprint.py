from flask import Blueprint, send_from_directory, jsonify

blueprint = Blueprint('fileserver', __name__,template_folder='templates')

import os

@blueprint.route('/<path:filepath>')
def serve_file(filepath):
  return send_from_directory(os.path.dirname(filepath),os.path.basename(filepath))

