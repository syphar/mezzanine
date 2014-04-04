from __future__ import absolute_import, division, unicode_literals

from django.core.files.storage import FileSystemStorage


class ThumbnailStorage(FileSystemStorage):
    """
    default Mezzanine thumbnail storage, for backwards compatiblity
    with users adding {{ MEDIA_URL }} manually in their templates
    """

    def __init__(self, location=None, base_url=None):
        super(ThumbnailStorage, self).__init__(
            location=location,
            base_url='',
        )
