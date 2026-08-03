import logging

from fastapi import APIRouter, HTTPException, Request
from fastapi_sqlalchemy import db

from models.base import User
from utils.consts import REVENUECAT_WEBHOOK_SECRET

logger = logging.getLogger(__name__)

route = APIRouter()

SUBSCRIBE_EVENTS = {
    "INITIAL_PURCHASE",
    "RENEWAL",
    "UNCANCELLATION",
    "PRODUCT_CHANGE",
    "NON_RENEWING_PURCHASE",
}

UNSUBSCRIBE_EVENTS = {
    "EXPIRATION",
    "BILLING_ISSUE",
}


@route.post("/revenuecat")
async def revenuecat_webhook(request: Request):
    return {"ok": True}
