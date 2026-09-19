"""Demo codecs for a 16-byte seal frame and a hash-binding helper.

Not a hardware driver. Not iris/biometrics. Not a TEE attestation verifier.
"""

from __future__ import annotations

import hashlib
import struct
from datetime import datetime, timezone
from typing import Any


class SmartSealTelemetryParser:
    @staticmethod
    def decode_frame(binary_data: bytes) -> dict[str, Any]:
        if len(binary_data) != 16:
            raise ValueError(f"expected 16 bytes, got {len(binary_data)}")
        ts, raw_temp, seal_byte, raw_shock, raw_lat, raw_lon = struct.unpack(">IhBBii", binary_data)
        return {
            "timestamp": datetime.fromtimestamp(ts, tz=timezone.utc).isoformat(),
            "temp_celsius": raw_temp / 100.0,
            "seal_intact": seal_byte == 0x01,
            "shock_g": raw_shock / 10.0,
            "latitude": raw_lat / 1e6,
            "longitude": raw_lon / 1e6,
            "source": "DEMO_FRAME_CODEC",
        }

    @staticmethod
    def encode_frame(
        ts: int, temp_c: float, seal_intact: bool, shock_g: float, lat: float, lon: float
    ) -> bytes:
        return struct.pack(
            ">IhBBii",
            ts,
            int(temp_c * 100),
            0x01 if seal_intact else 0x00,
            int(shock_g * 10),
            int(lat * 1e6),
            int(lon * 1e6),
        )


class ProofOfGazeValidator:
    """Hash-binds caller-supplied fields. Does not validate optics, gaze, or identity."""

    @staticmethod
    def construct_pog_digest(
        raw_frame: bytes,
        vslam_coordinates: tuple[float, float, float],
        atomic_timestamp: str,
        auditor_did: str,
        scanned_sscc: str,
    ) -> bytes:
        frame_hash = hashlib.sha256(raw_frame).hexdigest()
        coord_str = f"{vslam_coordinates[0]:.4f},{vslam_coordinates[1]:.4f},{vslam_coordinates[2]:.4f}"
        canonical_str = f"{frame_hash}|{coord_str}|{atomic_timestamp}|{auditor_did}|{scanned_sscc}"
        return hashlib.sha256(canonical_str.encode("utf-8")).digest()
