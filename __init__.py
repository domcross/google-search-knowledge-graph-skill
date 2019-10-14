from mycroft import MycroftSkill, intent_file_handler


class GoogleSearchKnowledgeGraph(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('graph.knowledge.search.google.intent')
    def handle_graph_knowledge_search_google(self, message):
        self.speak_dialog('graph.knowledge.search.google')


def create_skill():
    return GoogleSearchKnowledgeGraph()

