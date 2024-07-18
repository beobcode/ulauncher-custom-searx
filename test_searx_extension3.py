import unittest
from unittest.mock import Mock, patch
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from main import searxExtension, KeywordQueryEventEventListener, ICON_FILE  # Adjust import if necessary

class TestSearxExtension(unittest.TestCase):
    def setUp(self):
        patcher1 = patch('ulauncher.api.client.Extension.Extension.__init__', lambda x: None)
        patcher2 = patch('ulauncher.api.client.EventListener.EventListener.__init__', lambda x: None)
        self.addCleanup(patcher1.stop)
        self.addCleanup(patcher2.stop)
        patcher1.start()
        patcher2.start()

        self.extension = searxExtension()
        self.extension._listeners = {}  # Initialize the _listeners attribute
        self.extension.subscribe = Mock()  # Mock the subscribe method

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
        self.assertEqual(result.get_items()[0], "test")

if __name__ == "__main__":
    unittest.main()
