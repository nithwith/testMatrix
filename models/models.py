from odoo import fields, models

class testMatrix(models.TransientModel):
   _name = 'test.matrix'

   def _default_task_ids(self):
       # your list of project should come from the context, some selection
       # in a previous wizard or wherever else
       projects = self.env['project.project'].browse([1, 2, 3])
       # same with users
       users = self.env['res.users'].browse([1, 2, 3])
       return [
           (0, 0, {
               'project_id': p.id,
               'user_id': u.id,
               'planned_hours': 0,
               'message_needaction': False,
               'date_deadline': fields.Date.today(),
           })
           # if the project doesn't have a task for the user, create a new one
           if not p.task_ids.filtered(lambda x: x.user_id == u) else
           # otherwise, return the task
           (4, p.task_ids.filtered(lambda x: x.user_id == u)[0].id)
           for p in projects
           for u in users
       ]

   task_ids = fields.Many2many('project.task', default=_default_task_ids)
