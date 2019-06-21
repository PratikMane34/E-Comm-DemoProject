# -*- coding: utf-8 -*-
# Copyright (c) 2018, Stellapps Technologies Private Ltd.
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
@frappe.whitelist()
def email(doc, method=None):
    print "#####################   email function     #####################################"

    # print('Email function call')


def validate(doc,method=None):
    print('++++++++Validation called++++++++++++++++++++++++++++++++++++')
    new_user_create = frappe.new_doc("User")
    #if(doc.email):
    new_user_create.email=doc.email
    #else:
    #   new_user_create.email='-'
    print("Printing new user email")
    print(new_user_create.email)
    full_name = doc.customer_name
    full_name = full_name.split(' ')
    print(full_name)
    print(len(full_name))
    if (len(full_name)>1):
        new_user_create.first_name = full_name[0]
        new_user_create.last_name = full_name[1]
    else:
        new_user_create.first_name = full_name[0]
    new_user_create.insert()
    #
    new_user_create.save()
    #frappe.db.commit()
    print("Full name of customer    =>  "+doc.customer_name)
    print('************************** '+doc.email+ '   **************************')
