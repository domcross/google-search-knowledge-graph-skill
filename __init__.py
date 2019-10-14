import json
import urllib

from mycroft import MycroftSkill, intent_file_handler


class GoogleSearchKnowledgeGraph(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.api_key = self.settings.get("api_key", "")

    @intent_file_handler('search.intent')
    def handle_graph_knowledge_search_google(self, message):
        if not self.api_key:
            self.speak_dialog('no.api.key')
        self.log.info(message.data)
        api_key = self.api_key
        query = 'Taylor Swift'
        service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
        params = {
            'query': query,
            'limit': 1,
            'indent': True,
            'key': api_key
        }
        url = service_url + '?' + urllib.parse.urlencode(params)
        response = json.loads(urllib.request.urlopen(url).read())


def create_skill():
    return GoogleSearchKnowledgeGraph()

