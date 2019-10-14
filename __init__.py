import json
import requests

from mycroft import MycroftSkill, intent_file_handler


class GoogleSearchKnowledgeGraph(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.api_key = self.settings.get("api_key", "")
        self.limit = 1

    @intent_file_handler('search.intent')
    def handle_graph_knowledge_search_google(self, message):
        if not self.api_key:
            self.speak_dialog('no.api.key')

        if not message.data['query']:
            # no query
            return False

        self.log.info(message.data)
        api_key = self.api_key
        query = message.data['query']
        service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
        params = {
            'query': query,
            'limit': self.limit,
            'indent': True,
            'key': api_key,
            'languages': self.lang[:2]
        }
        #url = service_url + '?' + urllib.parse.urlencode(params)
        response = requests.get(service_url, params=params).json()
        self.log.info(response)
        if not response['itemListElement']:
            self.speak_dialog("no.result")
            return
        if len(response['itemListElement']) != self.limit:
            self.speak_dialog("no.result")
            return
        element = response['itemListElement'][0]
        data = {'header': element['result']['name'],
                'body': element['result']['detailedDescription']['articleBody']}
        self.speak_dialog("result", data=data)


def create_skill():
    return GoogleSearchKnowledgeGraph()

