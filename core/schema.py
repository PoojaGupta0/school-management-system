import graphene
from graphene_django import DjangoObjectType

from core.models import Student, Teacher, TeachersOfStudent


class StudentsOfTeachersType(DjangoObjectType):
    class Meta:
        model = TeachersOfStudent


class TeachersType(DjangoObjectType):
    class Meta:
        model = Teacher


class StudentsType(DjangoObjectType):
    class Meta:
        model = Student


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


class CreateStudent(graphene.Mutation):
    __doc__ = "This class is used to create a new student"

    class Arguments:
        name = graphene.String()

    student = graphene.Field(StudentsType)

    def mutate(self, info, name):
        student = Student.objects.create(name=name)
        return CreateStudent(student=student)


class DeleteStudent(graphene.Mutation):
    __doc__ = "This class is used to remove the student"

    class Arguments:
        id = graphene.ID()

    student = graphene.Field(StudentsType)

    def mutate(self, info, id):
        student = Student.objects.get(id=id)
        if student:
            student.delete()
        return "Record deleted successfully"


class UpdateStudent(graphene.Mutation):
    __doc__ = "This class is used to update the student name"

    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    student = graphene.Field(StudentsType)

    def mutate(self, info, id, name):
        student = Student.objects.filter(id=id).first()
        if student:
            student.name = name
            student.save()
        return "Record Updated successfully"


class Mutation(graphene.ObjectType):
    add_or_remove_star = AddOrRemoveStar.Field()
    create_teacher = CreateTeacher.Field()
    delete_teacher = DeleteTeacher.Field()
    update_teacher = UpdateTeacher.Field()
    create_student = CreateStudent.Field()
    delete_student = DeleteStudent.Field()
    update_student = UpdateStudent.Field()


schema = graphene.Schema(mutation=Mutation)
