from flask import Blueprint, make_response, jsonify
from .controller import MainController


main_bp = Blueprint('main', __name__)
main_controller = MainController()

@main_bp.route('/', methods=['GET'])
def index():
    result=main_controller.index()
    return result

@main_bp.route('/resume', methods=['GET'])
def resume():
    result=main_controller.resume()
    return result
