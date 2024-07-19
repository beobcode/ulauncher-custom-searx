import unittest
from unittest.mock import Mock
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from main import searxExtension, KeywordQueryEventEventListener, ICON_FILE  # Adjust import if necessary

class TestSearxExtension(unittest.TestCase):
    def setUp(self):
        self.extension = searxExtension()

    def test_on_event_with_empty_query(self):
        event_listener = KeywordQueryEventEventListener()
        mock_event = Mock(spec=KeywordQueryEvent)
        mock_event.get_data.return_value = ""
        
        result = event_listener.on_event(mock_event, self.extension)
        
        self.assertIsInstance(result, RenderResultListAction)
        self.assertEqual(len(result.get_items()), 1)
        self.assertEqual(result.get_items()[0].name, "No input")
        self.assertIsInstance(result.get_items()[0].on_enter, DoNothingAction)

    def test_on_event_with_non_empty_query(self):
        event_listener = KeywordQueryEventEventListener()
        mock_event = Mock(spec=KeywordQueryEvent)
        mock_event.get_data.return_value = "test query"
        
        result = event_listener.on_event(mock_event, self.extension)
        
        self.assertIsInstance(result, RenderResultListAction)
        self.assertEqual(len(result.get_items()), 1)
        self.assertEqual(result.get_items()[0], "test")

if __name__ == "__main__":
    unittest.main()
