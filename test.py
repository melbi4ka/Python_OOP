from project.team import Team

import unittest

class TeamTest(unittest.TestCase):

    def setUp(self) -> None:
        self.team = Team("Levski")

    def test_initialize_properties(self):
        self.members = {}
        self.assertEqual("Levski", self.team.name)
        self.assertEqual({}, self.members)

    def test_name_invalid_with_number_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name = "Levski1994"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member_if_not_exist(self):
        result = self.team.add_member(gogo = 25, pepi  = 26)
        self.assertEqual({"gogo": 25, "pepi": 26}, self.team.members)
        self.assertEqual("Successfully added: gogo, pepi", result)

    def test_remove_member_if_not_exist(self):
        self.team.members = {"gogo": 25, "pepi": 26}
        result = self.team.remove_member("dani")
        self.assertEqual({"gogo": 25, "pepi": 26}, self.team.members)
        self.assertEqual("Member with name dani does not exist", result)

    def test_remove_member_if_exist(self):
        self.team.members = {"gogo": 25, "pepi": 26, "dani": 24}
        result = self.team.remove_member("dani")
        self.assertEqual({"gogo": 25, "pepi": 26}, self.team.members)
        self.assertEqual("Member dani removed", result)

    def test_greater_than_other_team_is_greater(self):
        self.team.members = {"gogo": 25, "pepi": 26, "dani": 24}
        self.other_team = Team("CSKA")
        self.other_team.members = {"gogi": 24, "pepo": 25, "danim": 24, "mitko": 23}
        result = self.team.__gt__(self.other_team)
        self.assertEqual(False, result)

    def test_greater_than_our_team_is_greater(self):
        self.team.members = {"gogo": 25, "pepi": 26, "dani": 24}
        self.other_team = Team("CSKA")
        self.other_team.members = {"gogi": 24, "pepo": 25}
        result = self.team.__gt__(self.other_team)
        self.assertEqual(True, result)

    def test_len(self):
        self.team.members = {"gogo": 25, "pepi": 26, "dani": 24}
        result = len(self.team)
        self.assertEqual(3, result)

    def test_add_two_teams(self):
        self.team.members = {"gogo": 25, "pepi": 26, "dani": 24}
        self.other_team = Team("CSKA")
        self.other_team.members = {"gogi": 24, "pepo": 25}

        self.merge_team = self.team.__add__(self.other_team)
        self.assertEqual("LevskiCSKA", self.merge_team.name)
        self.assertEqual({"gogo": 25, "pepi": 26,
                          "dani": 24, "gogi": 24, "pepo": 25}, self.merge_team.members)


    def test_str(self):
        self.team.members = {"gogo": 25, "pepi": 26, "dani": 24, "asen": 24}
        my_result = f"Team name: Levski\nMember: pepi - 26-years old\n" \
                 f"Member: gogo - 25-years old\n" \
                 f"Member: asen - 24-years old\nMember: dani - 24-years old"
        self.assertEqual(my_result, str(self.team))



if __name__ == "__main__":
    unittest.main()