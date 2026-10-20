import hashlib
import hmac
import os
import time

class NormService:
    def __init__(self):
        self.secret = os.urandom(32)
        # Example policy: Contexts allowed for a record
        self.policies = {
            "medical_record_1": {"allowed_contexts": ["doctor", "nurse"]},
            "financial_record_1": {"allowed_contexts": ["accountant", "auditor"]}
        }

    def _sign(self, payload: str) -> str:
        return hmac.new(self.secret, payload.encode(), hashlib.sha256).hexdigest()

    def check_policy(self, record_id: str, context: str) -> dict:
        """The caller asks: Is this record allowed in this context?"""
        timestamp = time.time()
        
        if record_id not in self.policies:
            return {"error": "No policy found", "decision": "DENY"}
            
        allowed = self.policies[record_id]["allowed_contexts"]
        is_allowed = context in allowed
        
        decision = "ALLOW" if is_allowed else "DENY"
        reason_code = "CTX_001" if is_allowed else "CTX_002"
        
        payload = f"{record_id}|{context}|{decision}|{reason_code}|{timestamp}"
        signature = self._sign(payload)
        
        return {
            "record_id": record_id,
            "context": context,
            "decision": decision,
            "reason_code": reason_code,
            "signature": signature,
            "note": "This is a PROPOSER. The caller must verify against real deployment rules."
        }