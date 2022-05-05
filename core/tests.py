from django.test import TestCase

from core.schema import schema


class StudentTestCases(TestCase):
    __doc__ = """ test cases of create and update student graphql endpoint """

    def test_create_student(self):
        query = """mutation{createStudent(name:"test_name"){student{id name}}}"""
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.student_id = result.data.get("createStudent")["student"]["id"]
        self.assertEquals(self.student_id, "1")

    def test_update_student(self):
        query = (
            """mutation{updateStudent(id:1, name:"updated_name"){student{id name}}}"""
        )
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertIsNotNone(result.data)


class TeachersTestCases(TestCase):
    __doc__ = """ test cases of create and update teacher graphql endpoint """

    def test_create_teacher(self):
        query = """mutation{createTeacher(name:"test_name"){teacher{id name}}}"""
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.teacher_id = result.data.get("createTeacher")["teacher"]["id"]
        self.assertEquals(self.teacher_id, "1")

    def test_update_teacher(self):
        query = (
            """mutation{updateTeacher(id:1, name:"updated_name"){teacher{id name}}}"""
        )
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertIsNotNone(result.data)


class AssignStudentTestCases(TestCase):
    __doc__ = """test cases of assign student to teacher graphql endpoint"""

    def test_assign_student_to_teacher(self):
        schema.execute(
            """mutation{createStudent(name:"test_name"){student{id name}}}"""
        )
        schema.execute(
            """mutation{createTeacher(name:"test_name"){teacher{id name}}}"""
        )
        assigned_student_query = """ mutation{
             assignStudent(teacherId:1 studentId:1){
              studentsOfTeacher{
                id                
              }
            }
            }"""
        result = schema.execute(assigned_student_query)
        self.assertIsNone(result.errors)
        self.assertIsNotNone(result.data)


class AddOrRemoveStarTestCases(TestCase):
    __doc__ = """test cases of added a star to exception student"""

    def test_assign_student_to_teacher(self):
        schema.execute(
            """mutation{createStudent(name:"test_name"){student{id name}}}"""
        )
        schema.execute(
            """mutation{createTeacher(name:"test_name"){teacher{id name}}}"""
        )
        schema.execute(
            """ mutation{
             assignStudent(teacherId:1 studentId:1){
              studentsOfTeacher{
                id                
              }
            }
            }"""
        )
        query = """ mutation{
                  addOrRemoveStar(id:1){
                    studentsOfTeacher{
                      id 
                    }
                  }
                }"""
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertIsNotNone(result.data)
