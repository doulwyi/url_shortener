from db import db


class UrlShortenModel(db.Model):
    __tablename__ = 'url'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2000))
    s_url = db.Column(db.String(8))

    def __init__(self, base_url, url, _hash):
        self.base_url = base_url
        self.url = url
        self.s_url = _hash

    @classmethod
    def find_by_url(cls, url):
        """
        Perform searching into DB filtering by URL.
        :param url: URL
        :return: First item found or None
        """
        return cls.query.filter_by(url=url).first()

    @classmethod
    def find_by_hash(cls, _hash):
        """
        Perform searching into DB filtering by URL.
        :param _hash: hash
        :return: First item found or None
        """
        return cls.query.filter_by(s_url=_hash).first()

    def json(self):
        """
        Returns url in json format.
        """
        return {'url': self.url}

    def shorten_url(self):
        """Returns Service url with shorten url"""
        return ''.join([self.base_url, self.s_url])

    def save_to_db(self):
        """
        Saves the current session into DB.
        """
        db.session.add(self)
        db.session.commit()
