import base64
import hashlib
import json
from typing import Any, Dict, Tuple

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519


class Ed25519Signer:
    """Sign and verify JSON payloads with Ed25519. Not a statutory certificate issuer."""

    @staticmethod
    def generate_keypair() -> Tuple[str, str]:
        private_key = ed25519.Ed25519PrivateKey.generate()
        public_key = private_key.public_key()
        priv_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption(),
        )
        pub_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        return base64.b64encode(priv_bytes).decode("utf-8"), base64.b64encode(pub_bytes).decode("utf-8")

    @staticmethod
    def canonicalize_json(data: Dict[str, Any]) -> bytes:
        return json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")

    @classmethod
    def sign_payload(cls, payload: Dict[str, Any], private_key_b64: str) -> str:
        private_key = ed25519.Ed25519PrivateKey.from_private_bytes(base64.b64decode(private_key_b64))
        signature = private_key.sign(cls.canonicalize_json(payload))
        return base64.b64encode(signature).decode("utf-8")

    @classmethod
    def verify_signature(cls, payload: Dict[str, Any], signature_b64: str, public_key_b64: str) -> bool:
        public_key = ed25519.Ed25519PublicKey.from_public_bytes(base64.b64decode(public_key_b64))
        try:
            public_key.verify(base64.b64decode(signature_b64), cls.canonicalize_json(payload))
            return True
        except Exception:
            return False

    @classmethod
    def compute_sha256(cls, payload: Dict[str, Any]) -> str:
        return hashlib.sha256(cls.canonicalize_json(payload)).hexdigest()
