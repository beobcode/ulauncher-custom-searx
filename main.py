import logging

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

logger = logging.getLogger(__name__)

ICON_FILE = "images/searxng-wordmark.png"

class searxExtension(Extension):
  def __init__(self):
    super(searxExtension, self).__init__()
    self.subscribe(KeywordQueryEvent, KeywordQueryEventEventListener()) 
    logger.info('Subdcribed to keywords and event listener')

class KeywordQueryEventEventListener(EventListener):
  def on_event(self, event, extension):
    logger.debug('Keyword event has been detected')
    search_query = event.get_data()
    
    if len(search_query.strip()) == 0:
      return RenderResultListAction(ExtensionResultItem(icon=ICON_FILE, name="No input", on_enter=DoNothingAction()))

    return_list = list()
    return_list.insert(0,"test")

    return RenderResultListAction(return_list)
  

if __name__ == "__main__":
  searxExtension().run()