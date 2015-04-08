from django.test import TestCase
from restclients.myplan import get_plan

class MyPlanTestData(TestCase):
    def test_javerage(self):
        plan = get_plan(regid="9136CCB8F66711D5BE060004AC494FFE", year=2013, quarter="spring", terms=4)
        self.assertEquals(len(plan.terms), 4)

        self.assertEquals(plan.terms[0].year, 2013)
        self.assertEquals(plan.terms[1].year, 2013)
        self.assertEquals(plan.terms[2].year, 2013)
        self.assertEquals(plan.terms[3].year, 2014)

        self.assertEquals(plan.terms[0].quarter, 'Spring')
        self.assertEquals(plan.terms[1].quarter, 'Summer')
        self.assertEquals(plan.terms[2].quarter, 'Autumn')
        self.assertEquals(plan.terms[3].quarter, 'Winter')

        self.assertEquals(len(plan.terms[0].courses), 2)
        self.assertEquals(len(plan.terms[1].courses), 1)
        self.assertEquals(len(plan.terms[2].courses), 0)
        self.assertEquals(len(plan.terms[3].courses), 0)

        self.assertEquals(plan.terms[0].courses[0].registrations_available, True)
        self.assertEquals(plan.terms[0].courses[0].curriculum_abbr, 'CSE')
        self.assertEquals(plan.terms[0].courses[0].course_number, '101')
        self.assertEquals(len(plan.terms[0].courses[0].sections), 3)
        self.assertEquals(plan.terms[0].courses[0].sections[0].section_id, 'A')
        self.assertEquals(plan.terms[0].courses[0].sections[1].section_id, 'AA')
        self.assertEquals(plan.terms[0].courses[0].sections[2].section_id, 'AB')

    def test_json(self):
        plan = get_plan(regid="9136CCB8F66711D5BE060004AC494FFE", year=2013, quarter="spring", terms=4)
        json_data = plan.json_data()
        self.assertEquals(json_data["terms"][0]["courses"][0]["sections"][1]["section_id"], "AA")