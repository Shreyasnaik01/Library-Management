# Copyright (c) 2021,  Faris Ansari and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
from frappe.model.document import Document
#import frappe

class LibraryMember(Document):
	 # this method will run every time a document is saved
	 def before_save(self):
		 self.full_name = f'{self.first_name} {self.last_name or ""}'
		 