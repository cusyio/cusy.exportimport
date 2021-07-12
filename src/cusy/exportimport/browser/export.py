# -*- coding: utf-8 -*-
from collective.exportimport.export_content import ExportContent


class CusyExportContent(ExportContent):
    """Customized content export view."""

    def dict_hook_collection(self, item, obj):
        """Use this to modify or skip the serialized data by type.
        Return the modified dict (item) or None if you want to skip this particular object.
        """
        export_url = item["@id"]
        item_url = obj.absolute_url()

        # Check if c.exportimport already contains the correct url
        if export_url == item_url:
            return item

        # Fix the id for collections, which is set to “@@export-content” because of the HypermediaBatch in plone.restapi
        item["@id"] = item_url


        if "batching" in item:
            try:
                batching = item["batching"].items()
            except TypeError:
                batching = []
            for batch_key, batch_url in batching:
                item["batching"][batch_key] = batch_url.replace(export_url, item_url)

        return item
