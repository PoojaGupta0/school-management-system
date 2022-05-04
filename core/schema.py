import graphene
from graphene_django import DjangoObjectType

from core.models import Teacher, TeachersOfStudent


class StudentsOfTeachersType(DjangoObjectType):
    class Meta:
        model = TeachersOfStudent


class TeachersType(DjangoObjectType):
    class Meta:
        model = Teacher


class AddOrRemoveStar(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    students_of_teacher = graphene.Field(StudentsOfTeachersType)

    def mutate(self, info, id):
        students_of_teacher = TeachersOfStudent.objects.get(pk=id)
        if students_of_teacher is not None:
            students_of_teacher.is_stared = (
                False if students_of_teacher.is_stared == True else True
            )
            students_of_teacher.save()
        return AddOrRemoveStar(students_of_teacher=students_of_teacher)


class CreateTeacher(graphene.Mutation):
    __doc__ = "This class is used to create a new teacher"

    class Arguments:
        name = graphene.String()

    teacher = graphene.Field(TeachersType)

    def mutate(self, info, name):
        teacher = Teacher.objects.create(name=name)
        return CreateTeacher(teacher=teacher)


class Mutation(graphene.ObjectType):
    add_or_remove_star = AddOrRemoveStar.Field()
    create_teacher = CreateTeacher.Field()


schema = graphene.Schema(mutation=Mutation)
