"""Firebase factory script."""

from config import FIRE_BASE_JSON, FIREBASE_URL
import firebase_admin
from firebase_admin import credentials, db


class FireBase(object):  # noqa: D103
    service_: object = firebase_admin.initialize_app(
        credentials.Certificate(f'venv37/{FIRE_BASE_JSON}'),
        {'databaseURL': FIREBASE_URL},
    )

    def get_data(self, path: str = '', key: str = None) -> dict:  # noqa: D103
        if not key:
            return {'message': 'No search data provided.'}
        root: object = db.reference(path=path, app=self.service_)
        ref = root.child(key.replace('@', '_at_').replace('.', '_dot_'))
        res = ref.get()
        return list(res.values())[-1] if res else {}

    def post_data(self, path: str = '', key: str = None, data: dict = None) -> any:  # noqa: D103
        if not all((path, key, data,)):
            return {'message': 'No search data provided.'}
        root: object = db.reference(path=path, app=self.service_)
        ref = root.child(key.replace('@', '_at_').replace('.', '_dot_'))
        push_ref = ref.push()
        push_ref.set(data)


f_base: object = FireBase()
