# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, session, request
from flask_login import login_required, current_user
import traceback

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

@blueprint.route('/', methods=['GET', 'POST'])
@login_required
def members():
    """List members."""
    errors = []
    if request.method == "POST":
        try:
            print("Transaction value to bank = {}".format(request.form['transaction']))
            current_user.update_balance(request.form['transaction'])
        except Exception, e:
            errors.append("Unable to update balance")
            traceback.print_exc()

    return render_template('users/members.html', errors=errors)
