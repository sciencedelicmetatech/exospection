import hashlib
import hmac
import os
import time

class AuthorityService:
    def __init__(self):
        self.secret = os.urandom(32)
        self.revoked_records = set()

    def revoke(self, record_id: str):
        """The deployment calls this to cancel a record."""
        self.revoked_records.add(record_id)

    def _sign(self, payload: str) -> str:
        return hmac.new(self.secret, payload.encode(), hashlib.sha256).hexdigest()

    def check_approval(self, record_id: str) -> dict:
        """The caller asks: Is this record still approved?"""
        timestamp = time.time()
        is_approved = record_id not in self.revoked_records
        status = "1" if is_approved else "0"
        
        payload = f"{record_id}|{status}|{timestamp}"
        signature = self._sign(payload)
        
        return {
            "record_id": record_id,
            "approved": is_approved,
            "timestamp": timestamp,
            "signature": signature,
            "error": None if is_approved else "Revoked"
        }