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


class DeleteTeacher(graphene.Mutation):
    __doc__ = "This class is used to remove the teacher"

    class Arguments:
        id = graphene.ID()

    teacher = graphene.Field(TeachersType)

    def mutate(self, info, id):
        teacher = Teacher.objects.get(id=id)
        if teacher:
            teacher.delete()
        return "Record deleted successfully"


class UpdateTeacher(graphene.Mutation):
    __doc__ = "This class is used to update the teacher name"

    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    teacher = graphene.Field(TeachersType)

    def mutate(self, info, id, name):
        teacher = Teacher.objects.filter(id=id).first()
        if teacher:
            teacher.name = name
            teacher.save()
        return "Record Updated successfully"


class Mutation(graphene.ObjectType):
    add_or_remove_star = AddOrRemoveStar.Field()
    create_teacher = CreateTeacher.Field()
    delete_teacher = DeleteTeacher.Field()
    update_teacher = UpdateTeacher.Field()


schema = graphene.Schema(mutation=Mutation)
