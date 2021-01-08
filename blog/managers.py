from django.db.models import Manager


class CategoryManager(Manager):
    def published(self):
        return self.filter(status=True)


class ArticleManager(Manager):
    def drafted(self):
        return self.filter(status='draft')

    def published(self):
        return self.filter(status='publish')

    def archived(self):
        return self.filter(status='archive')
