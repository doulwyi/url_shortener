from flask_restful import Resource, reqparse, request
from sqlalchemy.orm.exc import NoResultFound

from models.url_shortener import UrlShortenModel
from .utils import create_hash, is_valid_url


class UrlShorten(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url',
                        type=str,
                        required=True,
                        help='This field cannot be left blank.')

    def post(self):
        data = UrlShorten.parser.parse_args()
        url = data['url']
        url_base = request.url_root # Base URL from service

        # Adding http protocol if needed.
        if not url.startswith('http'):
            url = 'http://{}'.format(url)

        if is_valid_url(url) is False:
            return {'message': 'URL is not valid.'}, 500

        # Creates an unique hash for URL
        hash_ = create_hash()

        find_exist_url = UrlShortenModel.find_by_url(url)
        if find_exist_url:
            return {'shortened_url': ''.join([url_base, find_exist_url.s_url])}, 201

        url_model = UrlShortenModel(url_base, url, hash_)
        s_url = url_model.shorten_url()
        try:
            url_model.save_to_db()
        except NoResultFound:
            return {'message': 'An error occurred inserting the item.'}, 500

        return {'shortened_url': s_url}, 201


class GetUrlShorten(Resource):
    def get(self, _hash):
        find_exist_url = UrlShortenModel.find_by_hash(_hash)
        if find_exist_url:
            res = find_exist_url.json()
            return res
        return {'message': 'URL not found'}, 404
