"""Regression cases for erroneous readiness and missing approval evidence."""
import copy
import importlib.util
from pathlib import Path
import unittest
spec=importlib.util.spec_from_file_location('trip_controls',Path(__file__).resolve().parents[1]/'tools/trip_controls.py')
controls=importlib.util.module_from_spec(spec)
spec.loader.exec_module(controls)

class ReadinessControls(unittest.TestCase):
    def setUp(self): self.data=copy.deepcopy(controls.load(controls.READY_PATH))
    def test_current_tree_is_consistent(self): controls.validate()
    def test_closing_without_evidence_fails(self):
        self.data['gates'][0]['status']='CLOSED'
        with self.assertRaises(AssertionError): controls.derive_status(self.data)
    def test_gate_cannot_be_removed(self):
        self.data['gates'].pop()
        with self.assertRaises(AssertionError): controls.derive_status(self.data)
    def test_gate_cannot_be_hidden_in_another_stream(self):
        self.data['gates'][0]['workstream']='production'
        with self.assertRaises(AssertionError): controls.derive_status(self.data)
    def test_travel_closure_does_not_imply_signing_or_production(self):
        for g in self.data['gates']:
            if g['workstream']=='travel':
                g.update(status='CLOSED',evidence_reference='synthetic-test-reference')
        result=controls.derive_status(self.data)
        self.assertEqual(result['status'],'TRAVEL_READY')
        self.assertEqual(result['signing_status'],'NOT_SIGNING_READY')
        self.assertEqual(result['production_status'],'NOT_PRODUCTION_READY')

if __name__=='__main__': unittest.main()
