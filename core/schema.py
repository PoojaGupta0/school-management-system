import graphene
from graphene_django import DjangoObjectType

from core.models import TeachersOfStudent


class StudentsOfTeachersType(DjangoObjectType):
    class Meta:
        model = TeachersOfStudent


class Query(graphene.ObjectType):
    all_student_of_teachers = graphene.List(StudentsOfTeachersType)

    def resolve_all_student_of_teachers(self, info, **kwargs):
        return TeachersOfStudent.objects.all().order_by('-id')


class AddOrRemoveStar(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    students_of_teacher = graphene.Field(StudentsOfTeachersType)

    def mutate(self, info, id):
        students_of_teacher = TeachersOfStudent.objects.get(pk=id)
        if students_of_teacher is not None:
            students_of_teacher.is_stared = False if students_of_teacher.is_stared == True else True
            students_of_teacher.save()
        return AddOrRemoveStar(students_of_teacher=students_of_teacher)


class Mutation(graphene.ObjectType):
    add_or_remove_star = AddOrRemoveStar.Field()


schema = graphene.Schema(mutation=Mutation)