"""ALRPCV2 XML parser unit test."""
import os
import unittest

import generator.Model
import generator.parsers.ALRPCV2


class TestALRPCV2Parser(unittest.TestCase):

    """Test for ALRPCV2 xml parser."""

    class _Issue:
        def __init__(self, creator, value):
            self.creator = creator
            self.value = value

        def __eq__(self, other):
            return self.creator == other.creator and self.value == other.value

    def setUp(self):
        """Test initialization."""
        self.valid_xml_name = os.path.dirname(os.path.realpath(__file__)) + \
            "/valid_ALRPCV2.xml"
        self.parser = generator.parsers.ALRPCV2.Parser()

    def test_valid_xml(self):
        """Test parsing of valid xml."""
        interface = self.parser.parse(self.valid_xml_name)

        self.assertEqual(2, len(interface.params))
        self.assertDictEqual({"attribute1": "value1", "attribute2": "value2"},
                             interface.params)

        # Enumerations

        self.assertEqual(3, len(interface.enums))

        # Enumeration "FunctionID"

        self.assertIn("FunctionID", interface.enums)
        enum = interface.enums["FunctionID"]
        self.verify_base_item(item=enum,
                              name="FunctionID",
                              description=["Description string 1",
                                           "Description string 2"],
                              todos=['Function id todo'])
        self.assertIsNone(enum.internal_scope)

        self.assertEqual(2, len(enum.elements))

        self.assertIn("Function1_id", enum.elements)
        element = enum.elements["Function1_id"]
        self.verify_base_item(
            item=element,
            name="Function1_id",
            design_description=["Function1 element design description"])
        self.assertIsNone(element.internal_name)
        self.assertEqual(10, element.value)

        self.assertIn("Function2_id", enum.elements)
        element = enum.elements["Function2_id"]
        self.verify_base_item(
            item=element,
            name="Function2_id")
        self.assertEqual("Function2_internal", element.internal_name)
        self.assertIsNone(element.value)

        # Enumeration "messageType"

        self.assertIn("messageType", interface.enums)
        enum = interface.enums["messageType"]
        self.verify_base_item(
            item=enum,
            name="messageType",
            design_description=["messageType design description",
                                "messageType design description 2"],
            issues=[TestALRPCV2Parser._Issue(
                creator="messageType issue creator",
                value="Issue text")])
        self.assertIsNone(enum.internal_scope)

        self.assertEqual(3, len(enum.elements))

        self.assertIn("request", enum.elements)
        element = enum.elements["request"]
        self.verify_base_item(item=element,
                              name="request",
                              todos=["request todo 1", "request todo 2"],
                              issues=[TestALRPCV2Parser._Issue(
                                  creator="issue creator",
                                  value="request issue")])
        self.assertIsNone(element.internal_name)
        self.assertEqual(0, element.value)

        self.assertIn("response", enum.elements)
        element = enum.elements["response"]
        self.verify_base_item(item=element, name="response")
        self.assertIsNone(element.internal_name)
        self.assertEqual(1, element.value)

        self.assertIn("notification", enum.elements)
        element = enum.elements["notification"]
        self.verify_base_item(item=element, name="notification")
        self.assertIsNone(element.internal_name)
        self.assertEqual(2, element.value)

        # Enumeration "enum1"

        self.assertIn("enum1", interface.enums)
        enum = interface.enums["enum1"]
        self.verify_base_item(item=enum, name="enum1")
        self.assertEqual("scope", enum.internal_scope)

        self.assertEqual(3, len(enum.elements))

        self.assertIn("element1", enum.elements)
        element = enum.elements["element1"]
        self.verify_base_item(item=element, name="element1")
        self.assertIsNone(element.internal_name)
        self.assertEqual(10, element.value)

        self.assertIn("element2", enum.elements)
        element = enum.elements["element2"]
        self.verify_base_item(item=element, name="element2")
        self.assertEqual("element2_internal", element.internal_name)
        self.assertEqual(11, element.value)

        self.assertIn("element3", enum.elements)
        element = enum.elements["element3"]
        self.verify_base_item(
            item=element,
            name="element3",
            design_description=["Element design description"])
        self.assertIsNone(element.internal_name)
        self.assertIsNone(element.value)

        # Structures

        self.assertEqual(2, len(interface.structs))

        # Structure "struct1"

        self.assertIn("struct1", interface.structs)
        struct = interface.structs["struct1"]
        self.verify_base_item(
            item=struct,
            name="struct1",
            description=["Struct description"],
            issues=[TestALRPCV2Parser._Issue(creator="creator1",
                                             value="Issue1"),
                    TestALRPCV2Parser._Issue(creator="creator2",
                                             value="Issue2")])

        self.assertEqual(4, len(struct.members))

        self.assertIn("member1", struct.members)
        member = struct.members["member1"]
        self.verify_base_item(
            item=member,
            name="member1",
            description=["Param1 description"])
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, generator.Model.Integer)
        self.assertIsNone(member.param_type.min_value)
        self.assertIsNone(member.param_type.max_value)

        self.assertIn("member2", struct.members)
        member = struct.members["member2"]
        self.verify_base_item(item=member, name="member2")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, generator.Model.Boolean)

        self.assertIn("member3", struct.members)
        member = struct.members["member3"]
        self.verify_base_item(item=member, name="member3")
        self.assertEqual(False, member.is_mandatory)
        self.assertIsInstance(member.param_type, generator.Model.Double)
        self.assertIsNone(member.param_type.min_value)
        self.assertAlmostEqual(20.5, member.param_type.max_value)

        self.assertIn("member4", struct.members)
        member = struct.members["member4"]
        self.verify_base_item(item=member, name="member4")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, generator.Model.Array)
        self.assertIsNone(member.param_type.min_size)
        self.assertIsNone(member.param_type.max_size)
        self.assertIsInstance(member.param_type.element_type,
                              generator.Model.Integer)
        self.assertEqual(11, member.param_type.element_type.min_value)
        self.assertEqual(100, member.param_type.element_type.max_value)

        # Structure "struct2"

        self.assertIn("struct2", interface.structs)
        struct = interface.structs["struct2"]
        self.verify_base_item(item=struct,
                              name="struct2",
                              description=["Description of struct2"])

        self.assertEqual(4, len(struct.members))

        self.assertIn("m1", struct.members)
        member = struct.members["m1"]
        self.verify_base_item(item=member, name="m1")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, generator.Model.String)
        self.assertIsNone(member.param_type.max_length)

        self.assertIn("m2", struct.members)
        member = struct.members["m2"]
        self.verify_base_item(item=member, name="m2")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, generator.Model.Array)
        self.assertEqual(1, member.param_type.min_size)
        self.assertEqual(50, member.param_type.max_size)
        self.assertIsInstance(member.param_type.element_type,
                              generator.Model.String)
        self.assertEqual(100, member.param_type.element_type.max_length)

        self.assertIn("m3", struct.members)
        member = struct.members["m3"]
        self.verify_base_item(item=member, name="m3")
        self.assertTrue(member.is_mandatory)
        self.assertIs(member.param_type, interface.enums["enum1"])

        self.assertIn("m4", struct.members)
        member = struct.members["m4"]
        self.verify_base_item(item=member, name="m4")
        self.assertTrue(member.is_mandatory)
        self.assertIsInstance(member.param_type, generator.Model.Array)
        self.assertIsNone(member.param_type.min_size)
        self.assertEqual(10, member.param_type.max_size)
        self.assertIs(member.param_type.element_type,
                      interface.structs["struct1"])

        # Functions

        self.assertEqual(3, len(interface.functions))

        # Function request "Function1"

        self.assertIn(
            (interface.enums["FunctionID"].elements["Function1_id"],
             interface.enums["messageType"].elements["request"]),
            interface.functions)
        function = interface.functions[
            (interface.enums["FunctionID"].elements["Function1_id"],
             interface.enums["messageType"].elements["request"])]
        self.verify_base_item(
            item=function,
            name="Function1",
            description=["Description of request Function1"],
            todos=["Function1 request todo"])
        self.assertIs(function.function_id,
                      interface.enums["FunctionID"].elements["Function1_id"])
        self.assertIs(function.message_type,
                      interface.enums["messageType"].elements["request"])
        self.assertIsNone(function.platform)

        self.assertEqual(3, len(function.params))

        self.assertIn("param1", function.params)
        param = function.params["param1"]
        self.verify_base_item(
            item=param,
            name="param1",
            issues=[TestALRPCV2Parser._Issue(creator="", value="")])
        self.assertEqual(False, param.is_mandatory)
        self.assertIsInstance(param.param_type, generator.Model.String)
        self.assertIsNone(param.param_type.max_length)
        self.assertIsNone(param.platform)
        self.assertEqual("String default value", param.default_value)

        self.assertIn("param2", function.params)
        param = function.params["param2"]
        self.verify_base_item(
            item=param,
            name="param2",
            description=["Param2 description", ""],
            todos=["Param2 todo"])
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, generator.Model.Integer)
        self.assertIsNone(param.param_type.min_value)
        self.assertIsNone(param.param_type.max_value)
        self.assertEqual("param2 platform", param.platform)
        self.assertIsNone(param.default_value)

        self.assertIn("param3", function.params)
        param = function.params["param3"]
        self.verify_base_item(item=param, name="param3")
        self.assertEqual(False, param.is_mandatory)
        self.assertIs(param.param_type, interface.structs["struct1"])
        self.assertIsNone(param.platform)
        self.assertIsNone(param.default_value)

        # Function response "Function1"

        self.assertIn(
            (interface.enums["FunctionID"].elements["Function1_id"],
             interface.enums["messageType"].elements["response"]),
            interface.functions)
        function = interface.functions[
            (interface.enums["FunctionID"].elements["Function1_id"],
             interface.enums["messageType"].elements["response"])]
        self.verify_base_item(
            item=function,
            name="Function1",
            issues=[TestALRPCV2Parser._Issue(creator="c1", value=""),
                    TestALRPCV2Parser._Issue(creator="c2", value="")])
        self.assertIs(function.function_id,
                      interface.enums["FunctionID"].elements["Function1_id"])
        self.assertIs(function.message_type,
                      interface.enums["messageType"].elements["response"])
        self.assertEqual("", function.platform)

        self.assertEqual(3, len(function.params))

        self.assertIn("p1", function.params)
        param = function.params["p1"]
        self.verify_base_item(item=param, name="p1")
        self.assertTrue(param.is_mandatory)
        self.assertIs(param.param_type, interface.enums["enum1"])
        self.assertIsNone(param.platform)
        self.assertIsNone(param.default_value)

        self.assertIn("p2", function.params)
        param = function.params["p2"]
        self.verify_base_item(item=param, name="p2")
        self.assertTrue(param.is_mandatory)
        self.assertIs(param.param_type, interface.enums["enum1"])
        self.assertIsNone(param.platform)
        self.assertIs(param.default_value,
                      interface.enums["enum1"].elements["element2"])

        self.assertIn("p3", function.params)
        param = function.params["p3"]
        self.verify_base_item(item=param, name="p3", design_description=[""])
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, generator.Model.Boolean)
        self.assertIsNone(param.platform)
        self.assertEqual(False, param.default_value)

        # Function notification "Function2"

        self.assertIn(
            (interface.enums["FunctionID"].elements["Function2_id"],
             interface.enums["messageType"].elements["notification"]),
            interface.functions)
        function = interface.functions[
            (interface.enums["FunctionID"].elements["Function2_id"],
             interface.enums["messageType"].elements["notification"])]
        self.verify_base_item(item=function,
                              name="Function2",
                              description=["Function2 description"])
        self.assertIs(function.function_id,
                      interface.enums["FunctionID"].elements["Function2_id"])
        self.assertIs(function.message_type,
                      interface.enums["messageType"].elements["notification"])
        self.assertEqual("function2 platform", function.platform)

        self.assertEqual(3, len(function.params))

        self.assertIn("n1", function.params)
        param = function.params["n1"]
        self.verify_base_item(item=param, name="n1", todos=["n1 todo"])
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, generator.Model.EnumSubset)
        self.assertIs(param.param_type.enum, interface.enums["enum1"])
        self.assertDictEqual(
            {"element2": interface.enums["enum1"].elements["element2"],
             "element3": interface.enums["enum1"].elements["element3"]},
            param.param_type.allowed_elements)
        self.assertIsNone(param.platform)
        self.assertIsNone(param.default_value)

        self.assertIn("n2", function.params)
        param = function.params["n2"]
        self.verify_base_item(item=param, name="n2", todos=["n2 todo"])
        self.assertTrue(param.is_mandatory)
        self.assertIsInstance(param.param_type, generator.Model.Array)
        self.assertEqual(1, param.param_type.min_size)
        self.assertEqual(100, param.param_type.max_size)
        self.assertIsInstance(param.param_type.element_type,
                              generator.Model.EnumSubset)
        self.assertIs(param.param_type.element_type.enum,
                      interface.enums["enum1"])
        self.assertDictEqual(
            {"element1": interface.enums["enum1"].elements["element1"],
             "element3": interface.enums["enum1"].elements["element3"]},
            param.param_type.element_type.allowed_elements)
        self.assertIsNone(param.platform)
        self.assertIsNone(param.default_value)

        self.assertIn("n3", function.params)
        param = function.params["n3"]
        self.verify_base_item(item=param, name="n3")
        self.assertEqual(False, param.is_mandatory)
        self.assertIs(param.param_type, interface.structs["struct2"])
        self.assertIsNone(param.platform)
        self.assertIsNone(param.default_value)

    def verify_base_item(self, item, name, description=None,
                         design_description=None, issues=None, todos=None):
        """Verify base interface item variables."""
        self.assertEqual(name, item.name)
        self.assertSequenceEqual(self.get_list(description), item.description)
        self.assertSequenceEqual(self.get_list(design_description),
                                 item.design_description)
        self.assertSequenceEqual(self.get_list(issues), item.issues)
        self.assertSequenceEqual(self.get_list(todos), item.todos)

    @staticmethod
    def get_list(list=None):
        """Return provided list or empty list if None is provided."""
        return list if list is not None else []

if __name__ == "__main__":
    unittest.main()
