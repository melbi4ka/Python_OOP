class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def _find_by_id(self, collection, obj_id):
        for el in collection:
            if el.id == obj_id:
                return el

    def edit_category(self, category_id, new_name):
        category = self._find_by_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self._find_by_id(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self._find_by_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self._find_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self,topic_id):
        topic = self._find_by_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self._find_by_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return  self._find_by_id(self.documents, document_id)

    def __repr__(self):
        result = "\n".join([repr(document) for document in self.documents])
        return result



