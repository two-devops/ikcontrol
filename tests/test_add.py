from cmds.add import Add

class TestAddResources:
    """testing class AddResource"""

    entities = ["kit", "target", "pipeline"]

    def test_entities(self):
        """testing entities function"""

        addresource = Add()

        for entity in self.entities:
            if entity == "kit":
                assert True is addresource.add_entity(entity, "test")
            if entity == "target":
                assert True is addresource.add_entity(entity, "test")
            if entity == "pipeline":
                assert True is addresource.add_entity(entity, "test")
