from odoo import api,fields,models, _
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

class Student(models.Model):

    _rec_name = 'f_name'
    _name='student.details'

    # name=fields.Char("Name")
    f_name = fields.Char(string= "First Name", required= True)
    l_name = fields.Char("Last Name")
    dob=fields.Date("Date of Birth")
    age=fields.Integer('Age', default=12)
    gender = fields.Selection([('M', 'Male'), ('F', 'Female')], string='Gender')
    roll_number = fields.Integer("Roll Number")
    entry_fee = fields.Float("Entree Fee")
    is_minor = fields.Boolean("Minor")

    address = fields.Char(string='Address')
    father_name = fields.Char(string="Father's Name")
    mother_name = fields.Char(string="Mother's Name")
    no_sibling = fields.Integer(string='Siblings')


    # dept = fields.Many2one("department.details", "Department")
    #
    # dep_id = fields.Many2one("department.details", "Department")

    # @api.depends('dob')
    # def get_age(self):
    #  for record in self:
    #      agee = relativedelta(datetime.now().date(), fields.Datetime.from_string(record.dob)).years
    #      record.age = str(agee)



    # @api.onchange('f_name', 'l_name')
    # def generate_fullname(self):
    #     for record in self:
    #         record.name = str(record.f_name)+' '+str(record.l_name)


class Department(models.Model):

    _name='department.details'

    name=fields.Char("Department Name")

    dept_head_id = fields.Many2one(comodel_name='res.partner', string='Department Head')

    sale_id = fields.Many2one('sale.order', string='Sale Order')

    dept_line_ids = fields.One2many(comodel_name='department.details.line', inverse_name='dept_id', string='Department Details')

    teacher_ids = fields.Many2many('teacher.details', 'department_teacher_rel', 'dept_id', 'teach_id',
                                   string='Teachers')





class DepartmentLine(models.Model):

    _name='department.details.line'

    student_id = fields.Many2one('student.details', 'Student Name')
    fee_status = fields.Char('Fee Status')


    dept_id = fields.Many2one('department.details', 'Dept Detail')



class Teacher(models.Model):

    _name='teacher.details'

    name=fields.Char("Name")
    salary=fields.Float("salary")


class Book(models.Model):

    _name='book.details'
    # _rec_name = 'book_name'
    price=fields.Float("Price")
    name=fields.Char("Book Name")
    genre=fields.Char("Book Genre")
    book_desc=fields.Text("Description")

    # lib_id = fields.Many2one("library.details", "lib ref")

# class Library(models.Model):
#
#     _name='library.details'
#
#     book=fields.Many2one("book.details",'Book')
#     student_details=fields.Many2one("student.details","Issued By")
#     book_date=fields.Datetime("Book Issue Date")
#     book_ids = fields.One2many("book.details", "lib_id", "Library Book")


