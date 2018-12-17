from flask import Blueprint, render_template, flash

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    flash('404', 'danger')
    return render_template('errors/404.html'), 404
