#!/usr/bin/env python3
"""To recognize models as a module"""

from models.engine.file_storage import FileStorage


storage = FileStorage
storage.reload()
