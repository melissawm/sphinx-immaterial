"""JSON serializer implementation wrapper."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING
from functools import partial
from sphinxcontrib.serializinghtml.jsonimpl import SphinxJSONEncoder
from sphinx_immaterial.nav_adapt import MkdocsNavEntry
from sphinx.locale import _TranslationProxy

if TYPE_CHECKING:
    from typing import Any


class SphinxImmaterialJSONEncoder(SphinxJSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, _TranslationProxy):
            return str(obj)
        if isinstance(obj, MkdocsNavEntry):
            return obj.__dict__
        return super().default(obj)


dump = partial(json.dump, cls=SphinxImmaterialJSONEncoder)
dumps = partial(json.dumps, cls=SphinxImmaterialJSONEncoder)
load = json.load
loads = json.loads
