from unittest import TestCase
from bytehold.handlers.base import *

class MockHandler(BaseHandler):
    pass

class HandlerManagerTest(TestCase):
    def test_singleton(self):
        hm1 = HandlerManager()
        hm2 = HandlerManager()
        self.assertEqual(id(hm1), id(hm2))

    def test_register(self):
        mock_handler = MockHandler()
        hm = HandlerManager()
        hm.register(mock_handler)
        self.assertTrue(mock_handler in hm.handlers)


class BaseHandlerTest(TestCase):
    def setUp(self):
        self.hm = HandlerManager()
        self.mock_handler = MockHandler()

    def test___init__(self):
        raise NotImplementedError

    def test___del__(self):
        raise NotImplementedError

    def test_sched_for_delete(self):
        raise NotImplementedError

    def test_handler_name(self):
        self.assertEqual(self.mock_handler.handler_name, 'MockHandler')

    def test_validate_config(self):
        self.assertEqual(self.mock_handler.validate_config(), None)
    
    def test_run(self):
        with self.assertRaises(NotImplementedError):
            self.mock_handler.run()

    def test_execute(self):
        raise NotImplementedError

    def test_compress(self):
        raise NotImplementedError

    def test_tar(self):
        raise NotImplementedError

    def test_print_output(self):
        raise NotImplementedError

    def test_timestamp(self):
        raise NotImplementedError
    
    def test_scp_put(self):
        raise NotImplementedError

    def test_rsync(self):
        raise NotImplementedError
