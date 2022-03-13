#imports
from flask import Blueprint, render_template

#Error blueprint intialization
errors = Blueprint('errors',__name__)



#Error route incase of any 404 error this will run
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404