# -*- coding: utf-8 -*-

from model.contact import *


# @pytest.mark.parametrize('contact', test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, db, json_contacts, check_ui):  # второй параметр указывает на источник тестовых данных
    contact = json_contacts
    old_conts = db.get_contact_list()
    app.contact.create_new_(contact)
    # assert len(old_conts)+1 == app.contact.count()
    new_conts = db.get_contact_list()
    old_conts.append(contact)
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_conts, key=Contact.id_or_max) == sorted(app.contact.get_conts_lst, key=Contact.id_or_max)