from openerp import fields, models


class Student(models.Model):

	_name = "student.student"

	image = fields.Binary()
	name = fields.Char(string="Student Name")
	city = fields.Char(string="City Name")
	email = fields.Char(string="E-Mail Address")
	mobile = fields.Char(string="Mobile No.")
	birthday = fields.Date(string="Birth Day")
	age = fields.Integer(string="Age")
