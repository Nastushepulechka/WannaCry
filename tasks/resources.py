from import_export import resources
from models import Tasks

class TasksResource(resources.MoodelResource):
    class Meta:
        model = Tasks