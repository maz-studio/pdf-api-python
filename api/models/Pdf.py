# -*- coding: utf-8 -*-
# IMPORT ==============================================================================================
import os
import subprocess
import pdfkit
# CALSS ===============================================================================================
class Pdf:

    __content__             = None
    __url__                 = None
    __options__             = None
    """
        Change path windows or linux
    """ 
    wkhtmltopdf_path = subprocess.check_output(['which', 'wkhtmltopdf']).decode('utf-8').strip()
    __configuration__       = pdfkit.configuration(wkhtmltopdf = wkhtmltopdf_path)

    def __init__(self, url : str = None, content : str = None, options : dict = None):
        """
            Setter data
            args            : [
                content     : int
                options     : dict
            ]
        """
        self.__url__            = url
        self.__content__        = content
        self.__options__        = options

    def generation(self):
        """
            Pdf generation, check data
            Return          : dict or object
        """
        try:
            if self.__content__ != None:
                return pdfkit.from_string(self.__content__, False, options = self.__options__, configuration = self.__configuration__)
            
            if self.__url__ != None:
                return pdfkit.from_url(self.__url__, False, options = self.__options__, configuration = self.__configuration__)

            return {
                "error"     : True,
                "response"  : "'url' and 'content' is NULL"
            }

        except BaseException as ex:
            return {
                "error"     : True,
                "response"  : str(ex)
            }
