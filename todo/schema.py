import graphene
from graphene_django import DjangoObjectType
from mainapp.models import User
from todoapp.models import TODO, Project


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_todos = graphene.List(TODOType)
    all_projects = graphene.List(ProjectType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    todo_by_id = graphene.Field(TODOType, id=graphene.Int(required=True))
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
    todos_by_user_name = graphene.List(TODOType, name=graphene.String(required=False))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_todos(root, info):
        return TODO.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def resolve_todo_by_id(self, info, id):
        try:
            return TODO.objects.get(id=id)
        except TODO.DoesNotExist:
            return None

    def resolve_project_by_id(self, info, id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            return None

    def resolve_todos_by_user_name(self, info, name=None):
        todos = TODO.objects.all()
        if name:
            todos = todos.filter(user__last_name=name)
        return todos


class UserMutation(graphene.Mutation):
    class Arguments:
        last_name = graphene.String(required=True)
        uid = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, last_name, uid, first_name, email):
        user = User.objects.get(pk=uid)
        user.last_name = last_name
        user.uid = uid
        user.first_name = first_name
        user.email =email
        user.save()
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()


schema = graphene.Schema(query=Query)
