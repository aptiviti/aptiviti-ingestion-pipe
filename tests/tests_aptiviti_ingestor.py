import sys
sys.path.append('.')
from aptiviti_ingestor import aptiviti_data_ingestor
import unittest
from unittest.mock import Mock, MagicMock
from unittest.mock import patch, call

@patch ('aptiviti_ingestor.analytics')

class TestAptivitiIngestor(unittest.TestCase):

    ingestor = None
    name = 'mockName'
    user_id = 'mockUser'
    previous_id = 'mockPreviousId'
    group_id = 'mockGroup'
    event = 'mockEvent'
    properties = 'mockProperties'
    traits = 'mockTraits'
    context = 'mockContext'
    timestamp = 'mockTimestamp'
    anonymous_id = 'mockAnon'
    integrations = 'mockInt'
    category = 'mockCategory'
    SEGMENT_WRITE_KEY = 'mockKey'

    def setUp(self):
      self.ingestor = aptiviti_data_ingestor(self.SEGMENT_WRITE_KEY)

    def test_write_key(self, mock_analytics):
      self.assertEqual(self.ingestor.write_key, self.SEGMENT_WRITE_KEY)

    def test_identify(self, mock_analytics):
      self.ingestor.identify(user_id=self.user_id, traits=self.traits, context=self.context, timestamp=self.timestamp, anonymous_id=self.anonymous_id, integrations=self.integrations)
      
      self.assertTrue(mock_analytics.identify.called)
      self.assertEqual(mock_analytics.identify.call_count, 1)
      
      self.assertEqual(mock_analytics.identify.call_args[0][0], self.user_id)
      self.assertEqual(mock_analytics.identify.call_args[0][1], self.traits)
      self.assertEqual(mock_analytics.identify.call_args[0][2], self.context)
      self.assertEqual(mock_analytics.identify.call_args[0][3], self.timestamp)
      self.assertEqual(mock_analytics.identify.call_args[0][4], self.anonymous_id)
      self.assertEqual(mock_analytics.identify.call_args[0][5], self.integrations)

    def test_track(self, mock_analytics):
      self.ingestor.track(self.user_id, self.event, self.properties, self.context, self.timestamp, self.anonymous_id, self.integrations)
           
      self.assertEqual(mock_analytics.track.call_args[0][0], self.user_id)
      self.assertEqual(mock_analytics.track.call_args[0][1], self.event)
      self.assertEqual(mock_analytics.track.call_args[0][2], self.properties)      
      self.assertEqual(mock_analytics.track.call_args[0][3], self.context)
      self.assertEqual(mock_analytics.track.call_args[0][4], self.timestamp)
      self.assertEqual(mock_analytics.track.call_args[0][5], self.anonymous_id)
      self.assertEqual(mock_analytics.track.call_args[0][6], self.integrations)

    def test_page(self, mock_analytics):
      self.ingestor.page(self.user_id, self.category, self.name, self.properties, self.context, self.timestamp, self.anonymous_id, self.integrations)
      
      self.assertEqual(mock_analytics.page.call_args[0][0], self.user_id)
      self.assertEqual(mock_analytics.page.call_args[0][1], self.category)
      self.assertEqual(mock_analytics.page.call_args[0][2], self.name)      
      self.assertEqual(mock_analytics.page.call_args[0][3], self.properties)
      self.assertEqual(mock_analytics.page.call_args[0][4], self.context)
      self.assertEqual(mock_analytics.page.call_args[0][5], self.timestamp)
      self.assertEqual(mock_analytics.page.call_args[0][6], self.anonymous_id)
      self.assertEqual(mock_analytics.page.call_args[0][7], self.integrations)
    
    def test_screen(self, mock_analytics):
      self.ingestor.screen(self.user_id, self.category, self.name, self.properties, self.context, self.timestamp, self.anonymous_id, self.integrations)

      self.assertEqual(mock_analytics.screen.call_args[0][0], self.user_id)
      self.assertEqual(mock_analytics.screen.call_args[0][1], self.category)
      self.assertEqual(mock_analytics.screen.call_args[0][2], self.name)      
      self.assertEqual(mock_analytics.screen.call_args[0][3], self.properties)
      self.assertEqual(mock_analytics.screen.call_args[0][4], self.context)
      self.assertEqual(mock_analytics.screen.call_args[0][5], self.timestamp)
      self.assertEqual(mock_analytics.screen.call_args[0][6], self.anonymous_id)
      self.assertEqual(mock_analytics.screen.call_args[0][7], self.integrations)


    def test_group(self, mock_analytics):
      self.ingestor.group(self.user_id, self.group_id, self.traits, self.context, self.timestamp, self.anonymous_id, self.integrations)

      self.assertEqual(mock_analytics.group.call_args[0][0], self.user_id)
      self.assertEqual(mock_analytics.group.call_args[0][1], self.group_id)
      self.assertEqual(mock_analytics.group.call_args[0][2], self.traits)      
      self.assertEqual(mock_analytics.group.call_args[0][3], self.context)
      self.assertEqual(mock_analytics.group.call_args[0][4], self.timestamp)
      self.assertEqual(mock_analytics.group.call_args[0][5], self.anonymous_id)
      self.assertEqual(mock_analytics.group.call_args[0][6], self.integrations)  

    def test_alias(self, mock_analytics):
      self.ingestor.alias(self.previous_id, self.user_id, self.context, self.timestamp, self.integrations)

      self.assertEqual(mock_analytics.alias.call_args[0][0], self.previous_id)
      self.assertEqual(mock_analytics.alias.call_args[0][1], self.user_id)
      self.assertEqual(mock_analytics.alias.call_args[0][2], self.context)
      self.assertEqual(mock_analytics.alias.call_args[0][3], self.timestamp)
      self.assertEqual(mock_analytics.alias.call_args[0][4], self.integrations) 