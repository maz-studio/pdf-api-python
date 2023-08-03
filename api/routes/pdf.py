# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from flask                                  import Blueprint, request, jsonify, make_response
from api.models.Pdf                         import Pdf
# BLUEPRINT =====================================================================================================================
pdf                                         = Blueprint("pdf", __name__)
# ROUTE =========================================================================================================================
@pdf.route("/pdf", methods = ["POST"])
def pdf_pdf() -> dict:
    """
        Get request as json, return pdf
        Return      : application/pdf, json
    """
    pdf                     = Pdf(**request.json)
    pdf                     = pdf.generation()
    
    if isinstance(pdf, dict):
        return jsonify(pdf)

    response                                    = make_response(pdf)
    response.headers["Content-Type"]            = "application/pdf"
    response.headers["Content-Disposition"]     = f"attachment; filename={hash(pdf)}.pdf".replace('-', '')
    return response