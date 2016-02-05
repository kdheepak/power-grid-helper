# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, session, request
from flask_login import login_required, current_user

from data import lookup

import traceback

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

@blueprint.route('/', methods=['GET', 'POST'])
@login_required
def members():
    """List members."""
    errors = []
    if request.method == "POST":
        print(request.form)
        if request.form['btn'] == 'transaction-btn':
            try:
                print("Transaction value to bank = {}".format(request.form['transaction']))
                if request.form['transaction'] == '':
                    transaction = 0.0
                    errors.append("Please enter a transaction value")
                else:
                    transaction = float(request.form['transaction'])
                    # if transaction < 0:
                        # errors.append("Negative transaction requested")
                        # raise Exception("Transaction less than zero")
                current_user.update_balance(transaction)
            except Exception, e:
                errors.append("Unable to update balance")
                traceback.print_exc()
        elif request.form['btn'] == 'payment-btn':
            try:
                if request.form['payment'] == '':
                    payment = 0
                    errors.append("Please enter number of houses")
                else:
                    number_of_houses = float(request.form['payment'])
                    payment = lookup[number_of_houses]
                    print("Payment from bank = {}".format(payment))
                    current_user.update_balance(-1 * payment)
            except Exception, e:
                errors.append("Unable to update balance")
                traceback.print_exc()

    return render_template('users/members.html', errors=errors)
